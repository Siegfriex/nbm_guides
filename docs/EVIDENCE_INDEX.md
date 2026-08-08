# MBN GUIDE portfolio evidence index

This index makes the portfolio claims inspectable without copying sensitive or
copyrighted material into this repository. Paths below are relative to the
authorized local `mbN_GUIDE` checkout supplied through `MBN_GUIDE_PY_ROOT`.

## Pinned release

| Item | Path / value | Check |
| --- | --- | --- |
| Release ID | `data/90_exports/frontend/mbn-guide-701011c9608e4524/` | Immutable frontend payload directory |
| Manifest | `.../manifest.json` | Per-file rows, bytes, SHA-256 |
| Payloads | `articles.json`, `places.json`, `stories.json`, `recommendations.json`, `related_articles.json`, `taxonomy.json`, `quality_report.json` | Recomputed by the notebook and verifier script |
| Projection gate | `data/80_quality/mbn/m14r1/run_20260808_m14r1_frontend_projection_hotfix/m14r1_projection_gate.json` | Build-level projection status |
| Validation gate | `data/80_quality/mbn/m14r1/run_20260808_m14r1_validation/m14r1_final_gate.json` | `PASS_WITH_WARNINGS`, `FRONTEND_READY`, critical counters 0 |

## Data-engine lineage

| Stage | Milestone | Evidence produced |
| --- | --- | --- |
| Geo | M7 | Canonical place/event objects, map eligibility, relations, provider evidence |
| Embedding | M8 | Pinned BGE-M3 vectors, metadata alignment and numerical QA |
| Semantic retrieval | M9 | Exact cosine relation artifacts and independent formula audit |
| Candidate + ranking | M10–M12 | Evidence table, candidate union, feature-aware ranking, reason table |
| Projection + validation | M13–M14R1 | Immutable JSON bundle, manifest, schema/FK/hash/secret checks |

## Frontend boundary

The live Vercel URL is [mbn-guide-front.vercel.app](https://mbn-guide-front.vercel.app).
The portfolio records route reachability and deployed UI audit evidence, but it
does not claim a frontend release pointer that has not been independently
validated against the M14R1 JSON bundle.

## What is intentionally excluded

- raw MBN article body/HTML and provider responses;
- API keys, credentials, and local secret configuration;
- BGE-M3 weights, embedding arrays, matrix caches, and LLM prompts/responses;
- synthetic StoryBundle, Event-to-Place, Article-to-Story, or editorial-label-
  to-product-taxonomy coercions.

## Reproduction contract

Run `notebooks/MBN_GUIDE_PORTFOLIO_REPRODUCIBILITY.ipynb` or
`scripts/verify_portfolio_snapshot.py` against the authorized source checkout.
Both are read-only: no crawl, provider request, embedding, LLM invocation,
release rewrite, or frontend mutation occurs.
