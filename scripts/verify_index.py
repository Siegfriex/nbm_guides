"""MBN GUIDE 포트폴리오 인덱스의 claim, link, 이미지, 공개 경계를 검사한다."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
CLAIMS = ROOT / "reports" / "portfolio_claims.json"


def main() -> int:
    text = README.read_text(encoding="utf-8")
    registry = json.loads(CLAIMS.read_text(encoding="utf-8"))
    failures: list[str] = []

    for claim in registry["claims"]:
        claim_id = claim["claimId"]
        match = re.search(
            rf"<!-- claim:{re.escape(claim_id)} -->(.*?)<!-- /claim -->", text
        )
        if not match:
            failures.append(f"CLAIM_MISSING:{claim_id}")
            continue
        shown = match.group(1).strip()
        expected = str(claim["value"])
        if shown != expected:
            failures.append(f"CLAIM_DRIFT:{claim_id}:{shown}!={expected}")

    local_links = set(re.findall(r"\]\((?!https?://|#|mailto:)([^)]+)\)", text))
    for link in sorted(local_links):
        target = (ROOT / link.split("#", 1)[0]).resolve()
        if not target.exists():
            failures.append(f"BROKEN_LINK:{link}")

    forbidden = {
        "ABSOLUTE_HOME_PATH": r"/home/[A-Za-z0-9._-]+/",
        "WINDOWS_USER_PATH": r"[A-Za-z]:\\Users\\",
        "CREDENTIAL_LITERAL": r"AIza[0-9A-Za-z_-]{20,}|sk-[0-9A-Za-z_-]{20,}",
    }
    corpus = "\n".join(
        path.read_text(encoding="utf-8", errors="ignore")
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts and path.stat().st_size < 5_000_000
    )
    for label, pattern in forbidden.items():
        if re.search(pattern, corpus):
            failures.append(label)

    expected_images = {
        "assets/vercel/home.png",
        "assets/vercel/place-detail.png",
        "assets/vercel/discover.png",
        "assets/vercel/live.png",
        "assets/data/geo_resolution.png",
        "assets/data/embedding_spaces.png",
        "assets/data/release_projection.png",
    }
    for image in sorted(expected_images):
        if not (ROOT / image).is_file():
            failures.append(f"MISSING_IMAGE:{image}")

    result = {
        "claimCount": len(registry["claims"]),
        "localLinkCount": len(local_links),
        "expectedImageCount": len(expected_images),
        "failures": failures,
        "status": "PASS" if not failures else "FAIL",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
