"""Read-only verification of the public MBN GUIDE portfolio snapshot.

Usage:
    MBN_GUIDE_PY_ROOT=/absolute/path/to/mbN_GUIDE \
        python scripts/verify_portfolio_snapshot.py
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path


RELEASE_ID = "mbn-guide-701011c9608e4524"
CRITICAL_ZERO = (
    "jsonParseErrors", "duplicateIds", "duplicateRecommendations",
    "duplicateRelatedArticles", "brokenFK", "relatedCountViolation",
    "relatedRankGap", "relatedNaNInf", "relatedReasonMissing",
    "manifestMismatch", "hashMismatch", "byteMismatch", "secretLeak",
)


def main() -> int:
    root = Path(os.environ.get("MBN_GUIDE_PY_ROOT", "../mbN_GUIDE_PY/mbN_GUIDE")).expanduser().resolve()
    release = root / "data/90_exports/frontend" / RELEASE_ID
    gate_path = root / "data/80_quality/mbn/m14r1/run_20260808_m14r1_validation/m14r1_final_gate.json"
    if not release.exists() or not gate_path.exists():
        print(f"MISSING_REQUIRED_ARTIFACT root={root}", file=sys.stderr)
        return 2

    manifest = json.loads((release / "manifest.json").read_text(encoding="utf-8"))
    failures: list[str] = []
    for item in manifest["files"]:
        payload = (release / item["path"]).read_bytes()
        if len(payload) != item["bytes"]:
            failures.append(f"BYTE_MISMATCH:{item['path']}")
        if hashlib.sha256(payload).hexdigest() != item["sha256"]:
            failures.append(f"HASH_MISMATCH:{item['path']}")

    gate = json.loads(gate_path.read_text(encoding="utf-8"))
    if gate.get("promotionVerdict") != "FRONTEND_READY":
        failures.append("PROMOTION_VERDICT")
    failures.extend(key for key in CRITICAL_ZERO if gate.get(key, 0) != 0)

    print(json.dumps({
        "releaseId": manifest.get("releaseId"),
        "payloadFiles": len(manifest["files"]),
        "validationStatus": gate.get("validationStatus"),
        "promotionVerdict": gate.get("promotionVerdict"),
        "failures": failures,
    }, ensure_ascii=False, sort_keys=True))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
