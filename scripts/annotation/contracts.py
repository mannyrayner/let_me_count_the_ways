"""Shared annotation-contract resolution without extraction dependencies."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from scripts.annotation.validate_classification import validate, validate_v0_2, validate_v0_3

ANNOTATION_FILES = {
    "0.1": (Path("prompts/annotation/classify_passage_v0_1.md"), Path("prompts/annotation/classification_schema_v0_1.json"), validate),
    "0.2": (Path("prompts/annotation/classify_passage_v0_2.md"), Path("prompts/annotation/classification_schema_v0_2.json"), validate_v0_2),
    "0.3": (Path("prompts/annotation/classify_passage_v0_3.md"), Path("prompts/annotation/classification_schema_v0_3.json"), validate_v0_3),
    "0.3.1": (Path("prompts/annotation/classify_passage_v0_3_1.md"), Path("prompts/annotation/classification_schema_v0_3.json"), validate_v0_3),
}

@dataclass(frozen=True)
class AnnotationContract:
    version: str; prompt_path: Path; schema_path: Path
    validator: Callable[[dict, str | None], None]
    prompt: str; schema: str; prompt_sha256: str; schema_sha256: str

def resolve_annotation_contract(version: str, repo_root: Path) -> AnnotationContract:
    try: prompt_path, schema_path, validator = ANNOTATION_FILES[version]
    except KeyError as exc: raise ValueError(f"unsupported annotation version {version!r}") from exc
    prompt=(repo_root/prompt_path).read_text(encoding="utf-8"); schema=(repo_root/schema_path).read_text(encoding="utf-8")
    digest=lambda value: hashlib.sha256(value.encode()).hexdigest()
    return AnnotationContract(version,prompt_path,schema_path,validator,prompt,schema,digest(prompt),digest(schema))
