#!/usr/bin/env python3
"""Derive paper tables and source links from the frozen, unchanged Git records.

No network, model calls, or reannotation. The checked-in generated files also
let the manuscript compile outside the full corpus checkout.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess

DATA_COMMIT = "ef7ea7933d8aa02b176d8fbddc496e55a41a7144"
RUNS = {
    "baseline": "canonical_31_v0_11_v0_3_1",
    "extension": "commitment_extension_5_v0_12_v0_3_1",
}
DIMENSIONS = {
    "T": "truth_conditional", "P": "performative",
    "E": "exclamatory_reflexive", "O": "other",
}
LANGUAGES = {"en": "English", "fr": "French", "no": "Norwegian",
             "sv": "Swedish", "da": "Danish", "de": "German", "it": "Italian"}
PAPER = Path(__file__).resolve().parent
URL = f"https://github.com/mannyrayner/let_me_count_the_ways/blob/{DATA_COMMIT}/"

def tex(s):
    replacements = {"&": r"\&", "%": r"\%", "_": r"\_", "#": r"\#",
                    "$": r"\$", "{": r"\{", "}": r"\}"}
    return "".join(replacements.get(c, c) for c in str(s))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=PAPER.parents[2])
    parser.add_argument("--check", action="store_true",
                        help="Compare with generated artifacts without writing.")
    args = parser.parse_args()
    inputs = {}
    def git(*command):
        return subprocess.check_output(["git", "-C", str(args.repo), *command])
    def read(path):
        raw = git("show", f"{DATA_COMMIT}:{path}")
        inputs[path] = hashlib.sha256(raw).hexdigest()
        return json.loads(raw)
    summaries = {cohort: read(f"results/annotation/{run}/summary.json")
                 for cohort, run in RUNS.items()}
    cohorts = {k: v["cases"] for k, v in summaries.items()}
    for key, summary in summaries.items():
        assert summary["status"] == "complete" and summary["failed"] == 0
        assert summary["valid"] == len(cohorts[key])
        assert len({c["occurrence_id"] for c in cohorts[key]}) == len(cohorts[key])
        for dim, field in DIMENSIONS.items():
            actual = {str(k): v for k, v in Counter(
                c["scores"][field] for c in cohorts[key]).items()}
            assert actual == summary["distributions"][dim], (key, dim)
    cohorts["combined"] = cohorts["baseline"] + cohorts["extension"]
    assert len({c["occurrence_id"] for c in cohorts["combined"]}) == 252
    assert [len(cohorts[k]) for k in cohorts] == [225, 27, 252]
    assert all(c["scores"]["truth_conditional"] == 4 for c in cohorts["extension"])

    metrics = {}
    for key, cases in cohorts.items():
        metrics[key] = {
            "n": len(cases),
            "score_counts": {dim: {str(s): sum(c["scores"][field] == s
                for c in cases) for s in range(5)}
                for dim, field in DIMENSIONS.items()},
            "utterance_status": dict(sorted(Counter(
                c["utterance_status"] for c in cases).items())),
            "patterns": {},
            "direct_patterns": {},
            "strong_P_weak_T": [c["occurrence_id"] for c in cases
                if c["scores"]["performative"] >= 3
                and c["scores"]["truth_conditional"] <= 1],
        }
        for threshold in (2, 3, 4):
            def pattern(c):
                return "".join(dim for dim in ("T", "P", "E")
                    if c["scores"][DIMENSIONS[dim]] >= threshold) or "none"
            metrics[key]["patterns"][str(threshold)] = dict(sorted(Counter(
                pattern(c) for c in cases).items()))
            metrics[key]["direct_patterns"][str(threshold)] = dict(sorted(Counter(
                pattern(c) for c in cases if c["utterance_status"] == "direct").items()))
    assert not metrics["combined"]["strong_P_weak_T"]
    assert metrics["combined"]["utterance_status"]["direct"] == 195

    base_review = read("results/review/canonical_31_v0_11_ai_review_v1/summary.json")
    ext_extract = read("results/extraction/commitment_extension_5_v0_12/summary.json")
    works = {}
    for cohort, rows in (("baseline", base_review["works"]),
                        ("extension", ext_extract["works"])):
        for row in rows:
            wid = row["work_id"]
            work = read(f"corpus/works/{wid}/work.json")
            selected = [c for c in cohorts[cohort] if c["work_id"] == wid]
            works[wid] = {k: work[k] for k in ("title", "author", "language")}
            works[wid].update(cohort=cohort, retained=len(selected),
                P_ge_2=sum(c["scores"]["performative"] >= 2 for c in selected),
                E_ge_2=sum(c["scores"]["exclamatory_reflexive"] >= 2 for c in selected))
    assert len(works) == 35 and sum(w["retained"] for w in works.values()) == 252

    groups = json.loads((PAPER / "case_selection.json").read_text())
    trees = {k: git("ls-tree", "-r", "--name-only", DATA_COMMIT, "--",
        f"results/annotation/{run}/annotations").decode().splitlines()
        for k, run in RUNS.items()}
    register = []
    for group in groups:
        for occurrence in group["occurrences"]:
            paths = [s for s in trees[group["cohort"]]
                if f"/{occurrence}/" in s and s.endswith("/output.json")]
            if len(paths) != 1:
                raise ValueError(f"Expected one output for {occurrence}: {paths}")
            output_path = paths[0]
            request_path = output_path.removesuffix("output.json") + "request.json"
            output = read(output_path)
            request = read(request_path)
            source = json.loads(request["input"].split("## Input\n\n", 1)[1])
            scores = output["core_classification"]["label_support"]
            summary_case = next(c for c in cohorts[group["cohort"]]
                                if c["occurrence_id"] == occurrence)
            assert scores == summary_case["scores"]
            assert source["occurrence_id"] == output["occurrence_id"] == occurrence
            record = {
                "key": group["key"], "label": group["label"],
                "cohort": group["cohort"], "occurrence_id": occurrence,
                "scores": scores, "status": output["utterance_status"]["status"],
                "location": source["METADATA"]["location"],
                "request_path": request_path, "output_path": output_path,
                "request_url": URL + request_path, "output_url": URL + output_path,
            }
            wid = source["METADATA"]["work"]["work_id"]
            if wid.startswith("skram-"):
                page_map = read(f"data/raw/{wid}/page-map.json")
                offset = record["location"]["source_start"]
                page = next(p for p in page_map
                            if p["output_start"] <= offset < p["output_end"])
                record.update(printed_page=page["page"], page_image_url=page["image_url"])
            register.append(record)

    generated = {}
    row_end = r" \\" + "\n"
    score_table = [
        r"\begin{table}[htbp]", r"\centering\small",
        r"\caption{Assigned support scores, with the original corpus and targeted extension reported separately.}",
        r"\label{tab:scores}", r"\begin{tabular}{llrrrrr}", r"\toprule",
        "Stage & Dimension & 0 & 1 & 2 & 3 & 4" + row_end.rstrip(), r"\midrule",
    ]
    for index, (key, label) in enumerate((("baseline", "Original (225)"),
                                        ("extension", "Extension (27)"),
                                        ("combined", "Combined (252)"))):
        if index:
            score_table.append(r"\midrule")
        for j, dim in enumerate(DIMENSIONS):
            counts = metrics[key]["score_counts"][dim]
            score_table.append(" & ".join([label if j == 0 else "", dim]
                + [str(counts[str(s)]) for s in range(5)]) + row_end.rstrip())
    score_table += [r"\bottomrule", r"\end{tabular}", r"\end{table}"]
    generated["score_table.tex"] = "\n".join(score_table) + "\n"

    pattern_table = [
        r"\begin{table}[htbp]", r"\centering\small",
        r"\caption{Dimensions reaching 2. The direct-speech column is a subset of the combined corpus. O is not used to define these combinations.}",
        r"\label{tab:patterns}", r"\begin{tabular}{lrrrr}", r"\toprule",
        "Dimensions & Original & Extension & Combined & Direct speech" + row_end.rstrip(),
        r"\midrule",
    ]
    for pattern, label in (("T", "T"), ("TP", "T and P"), ("TE", "T and E"),
                           ("TPE", "T, P and E"), ("none", "None")):
        values = [metrics[k]["patterns"]["2"].get(pattern, 0)
                  for k in ("baseline", "extension", "combined")]
        values += [metrics["combined"]["direct_patterns"]["2"].get(pattern, 0)]
        pattern_table.append(" & ".join([label] + list(map(str, values))) + row_end.rstrip())
    pattern_table += [r"\midrule", "Total & 225 & 27 & 252 & 195" + row_end.rstrip(),
                      r"\bottomrule", r"\end{tabular}", r"\end{table}"]
    generated["pattern_table.tex"] = "\n".join(pattern_table) + "\n"

    inventory = [
        "B denotes the original stage; X denotes the targeted extension. "
        "Language codes: da Danish, de German, en English, fr French, "
        "it Italian, no Norwegian, sv Swedish. Historical Dano-Norwegian "
        "is coded no, consistently with the original corpus. Retained "
        "counts reproduce provisional AI membership decisions.\n",
        r"\begingroup\small",
        r"\setlength{\tabcolsep}{3pt}",
        r"\begin{longtable}{@{}p{34mm}p{71mm}ccr@{}}",
        r"\caption{The 35 complete works searched, including the zero-yield extension work.}\\",
        r"\toprule",
        "Author & Work & Lang. & Stage & Retained" + row_end.rstrip(),
        r"\midrule\endfirsthead", r"\toprule",
        "Author & Work & Lang. & Stage & Retained" + row_end.rstrip(),
        r"\midrule\endhead",
        r"\midrule\multicolumn{5}{r}{Continued on next page}\\\endfoot",
        r"\bottomrule\endlastfoot",
    ]
    for wid, w in sorted(works.items(), key=lambda item: (
            item[1]["cohort"] == "extension", item[1]["language"], item[0])):
        inventory.append(" & ".join([tex(w["author"]), r"\emph{" + tex(w["title"]) + "}",
            w["language"], "B" if w["cohort"] == "baseline" else "X", str(w["retained"])])
            + row_end.rstrip())
    inventory += [r"\midrule", r"\multicolumn{4}{r}{Total} & 252\\",
                  r"\end{longtable}", r"\endgroup"]
    generated["corpus_inventory.tex"] = "\n".join(inventory) + "\n"

    links = [r"\newcommand{\caseref}[1]{\footnote{\csname case@#1\endcsname}}"]
    regtex = [
        r"\begingroup\footnotesize",
        r"\setlength{\tabcolsep}{4pt}",
        r"\begin{longtable}{@{}p{38mm}p{64mm}p{17mm}p{29mm}@{}}",
        r"\toprule Case & Occurrence and records & T/P/E/O & Status\\",
        r"\midrule\endfirsthead",
        r"\toprule Case & Occurrence and records & T/P/E/O & Status\\",
        r"\midrule\endhead", r"\bottomrule\endlastfoot",
    ]
    for group in groups:
        selected = [r for r in register if r["key"] == group["key"]]
        linktexts = [r"\href{" + r["request_url"] + "}{passage " + str(i + 1) + "}, "
                     + r"\href{" + r["output_url"] + "}{annotation " + str(i + 1) + "}"
                     for i, r in enumerate(selected)]
        links.append(r"\expandafter\def\csname case@" + group["key"] + r"\endcsname{"
                     + tex(group["label"]) + ": " + "; ".join(linktexts) + ".}")
        for r in selected:
            score = "/".join(str(r["scores"][field]) for field in DIMENSIONS.values())
            detail = r"\nolinkurl{" + r["occurrence_id"] + r"}. \href{" + r["request_url"] \
                + r"}{Input}; \href{" + r["output_url"] + "}{output}."
            if "page_image_url" in r:
                detail += r" \href{" + r["page_image_url"] + "}{Scan p. " + r["printed_page"] + "}."
            regtex.append(" & ".join([tex(group["label"]), detail, score,
                                     tex(r["status"].replace("_", " "))]) + row_end.rstrip())
    regtex += [r"\end{longtable}", r"\endgroup"]
    generated["case_links.tex"] = "\n".join(links) + "\n"
    generated["case_register.tex"] = "\n".join(regtex) + "\n"
    generated["case_register.json"] = json.dumps(register, ensure_ascii=False, indent=2) + "\n"
    generated["statistics.json"] = json.dumps({
        "data_commit": DATA_COMMIT, "runs": RUNS, "metrics": metrics, "works": works,
        "input_sha256": inputs,
        "selection_sha256": hashlib.sha256((PAPER / "case_selection.json").read_bytes()).hexdigest(),
    }, ensure_ascii=False, indent=2, sort_keys=True) + "\n"

    dest = PAPER / "generated"
    failures = []
    for name, content in generated.items():
        path = dest / name
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                failures.append(name)
        else:
            dest.mkdir(exist_ok=True)
            with path.open("w", encoding="utf-8", newline="\n") as stream:
                stream.write(content)
    if failures:
        raise SystemExit("Generated content differs: " + ", ".join(failures))
    print(json.dumps({"status": "verified" if args.check else "generated",
        "data_commit": DATA_COMMIT, "baseline": 225, "extension": 27,
        "combined": 252, "works": len(works), "case_register": len(register),
        "generated_files": len(generated)}, indent=2))

if __name__ == "__main__":
    main()
