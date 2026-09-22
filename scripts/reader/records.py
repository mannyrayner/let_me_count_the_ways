"""Load saved annotations for public display without revising their content."""
from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIELDS = {"T": "truth_conditional", "P": "performative", "E": "exclamatory_reflexive", "O": "other"}
LANGUAGES = {"en":"English","fr":"French","no":"Norwegian","da":"Danish","sv":"Swedish","de":"German","it":"Italian","ru":"Russian"}
PUBLIC = {"PUBLIC_DOMAIN_FULL_CONTEXT_OK", "PERMISSIONED_CONTEXT_OK"}

def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def text_digest(path):
    # JSON-file line endings may differ on Windows; source-text bytes are hashed separately.
    return hashlib.sha256(Path(path).read_text(encoding="utf-8").encode("utf-8")).hexdigest()

def canonical(root, work):
    path = root / "corpus/works" / work["work_id"] / "canonical.txt"
    if digest(path) != work["canonical_sha256"]:
        raise ValueError("Canonical source hash changed: " + work["work_id"])
    return path.read_text(encoding="utf-8")

def load_collection(root=ROOT, config=None):
    config = config or read(root / "data/reader/collection_v1.json")
    records, seen, hashes, texts, works = [], set(), {}, {}, {}
    for run in config["annotation_runs"]:
        base = root / "results/annotation" / run
        summary = read(base / "summary.json")
        if summary["status"] != "complete" or summary["failed"]:
            raise ValueError("Incomplete annotation run: " + run)
        hashes[(base/"summary.json").relative_to(root).as_posix()] = text_digest(base/"summary.json")
        if summary["valid"] != len(summary["cases"]):
            raise ValueError("Summary count mismatch")
        for case in summary["cases"]:
            oid, wid = case["occurrence_id"], case["work_id"]
            if oid in seen or not re.fullmatch(r"[a-z0-9-]+", oid):
                raise ValueError("Invalid/duplicate occurrence: " + oid)
            paths = sorted((base / "annotations" / oid).glob("*/output.json"))
            if len(paths) != 1:
                raise ValueError(f"{oid}: expected one frozen annotation, found {len(paths)}")
            output_path = paths[0]
            request_path = output_path.with_name("request.json")
            provenance_path = output_path.with_name("provenance.json")
            output, request, provenance = read(output_path), read(request_path), read(provenance_path)
            prepared = json.loads(request["input"].split("## Input\n\n",1)[1])
            if output["occurrence_id"] != oid or prepared["occurrence_id"] != oid:
                raise ValueError("Input/output identity mismatch: " + oid)
            if output["core_classification"]["label_support"] != case["scores"]:
                raise ValueError("Output scores differ from summary: " + oid)
            if wid not in works:
                wp = root / "corpus/works" / wid / "work.json"
                works[wid] = read(wp)
                # Fail closed on a more restrictive current policy.
                if works[wid]["rights"]["public_render_policy"] not in PUBLIC:
                    raise ValueError("Public rendering not allowed: " + wid)
                texts[wid] = canonical(root, works[wid])
                hashes[wp.relative_to(root).as_posix()] = text_digest(wp)
            if prepared["METADATA"]["work"]["rights"]["public_render_policy"] not in PUBLIC:
                raise ValueError("Saved input cannot be publicly rendered: " + oid)
            text, source = texts[wid], prepared["SOURCE_TEXT"]
            location = prepared["METADATA"]["location"]
            start, end = location["source_start"], location["source_end"]
            if text[start:end] != source["exact_match"]:
                raise ValueError("Target offsets differ from canonical source: " + oid)
            for name in ["local_text", "wider_canonical_context"]:
                block = source.get(name)
                if block and text[block["context_start"]:block["context_end"]] != block["text"]:
                    raise ValueError(f"{oid}: {name} offsets differ from source")
            translation = prepared.get("TRANSLATION_ANALYTICAL_AID")
            if case["language"] != "en" and not (translation and translation.get("status")=="provided"):
                raise ValueError("Missing saved translation: " + oid)
            for path in [request_path, output_path, provenance_path]:
                hashes[path.relative_to(root).as_posix()] = text_digest(path)
            prefix = "https://github.com/mannyrayner/let_me_count_the_ways/blob/" + config["data_commit"] + "/"
            records.append({"occurrence_id":oid, "work":works[wid], "source":source, "location":location,
                "translation":translation, "output":output, "provenance":provenance,
                "scores":{k:case["scores"][v] for k,v in FIELDS.items()},
                "run":run, "request_path":request_path.relative_to(root).as_posix(),
                "output_path":output_path.relative_to(root).as_posix(),
                "request_url":prefix+request_path.relative_to(root).as_posix(),
                "output_url":prefix+output_path.relative_to(root).as_posix(),
                "canonical_url":prefix+f"corpus/works/{wid}/canonical.txt",
                "source_summary":prepared.get("MODEL_GENERATED_SOURCE_GROUNDED_SUMMARY")})
            seen.add(oid)
    inventory = read(root / config["work_inventory"])["works"]
    if set(works) - set(inventory):
        raise ValueError("Work inventory does not cover annotation set")
    return sorted(records,key=lambda r:(r["work"]["title"].casefold(),r["location"]["source_start"])), inventory, hashes
