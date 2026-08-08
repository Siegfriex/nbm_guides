<div align="center">

**Data engineering**

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/) [![pandas](https://img.shields.io/badge/pandas-Parquet%20pipeline-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/) [![BGE--M3](https://img.shields.io/badge/BAAI-BGE--M3-FF6F61)](https://huggingface.co/BAAI/bge-m3) [![Exact cosine](https://img.shields.io/badge/Retrieval-Exact%20cosine-5B4B8A)](#frozen-vector-space-and-matrix-first-retrieval)

**Product handoff**

[![JSON release](https://img.shields.io/badge/Release-Immutable%20JSON-0A7E8C)](#verified-product-snapshot) [![Validation](https://img.shields.io/badge/M14R1-FRONTEND__READY-1F8B4C)](#release-and-runtime-boundary) [![Vercel](https://img.shields.io/badge/Vercel-Live%20UI-000000?logo=vercel)](https://mbn-guide-front.vercel.app)

# MBN GUIDE — 문화 기사에서 검증 가능한 장소·콘텐츠 탐색으로

**MBN 문화 기사 → 근거 기반 Place/Event → 정확한 semantic retrieval → 검증된 frontend data release**

[프로젝트 개요](#what-was-built) · [결과](#verified-product-snapshot) · [파이프라인](#the-engineering-story) · [재현](#reproduce-the-portfolio-checks) · [검증](#evidence-and-validation) · [라이브 UI](#release-and-runtime-boundary)

</div>

> Korean MBN culture articles are turned into a traceable place/event graph,
> exact semantic retrieval, and a minimal safe frontend release. The public
> portfolio deliberately exposes **methods, reproducible checks, and aggregate
> outcomes**—not article bodies, provider responses, credentials, or vectors.

[Live frontend (Vercel)](https://mbn-guide-front.vercel.app) ·
[Data-engine repository](https://github.com/Siegfriex/mbN_GUIDE) ·
[Portfolio reproducibility notebook](notebooks/MBN_GUIDE_PORTFOLIO_REPRODUCIBILITY.ipynb) ·
[Evidence index](docs/EVIDENCE_INDEX.md)

## What was built

MBN GUIDE is a local-first data pipeline and frontend handoff for cultural
content. It starts with MBN article index/body data and ends with a pinned,
hash-verified JSON release that a frontend can consume without receiving raw
corpus text or model internals.

```text
MBN article index + body
  → normalized article / body-block corpus
  → evidence-bound culture-entity candidates
  → provider-backed Place/Event resolution
  → BGE-M3 title, chunk, and entity vectors
  → exact body-first semantic retrieval
  → candidate retrieval and explainable ranking
  → contract-safe frontend projection + release validation
```

The design choice that matters most is provenance: an article mention is not
promoted directly to a map pin. It must retain the chain
`article → block evidence → verification → provider observation → canonical object`.
Ambiguous, not-found, or error states remain visible rather than being silently
converted into coordinates.

## Portfolio index: three surfaces, one evidence chain

| Surface | Public endpoint | Responsibility | What this portfolio verifies |
| --- | --- | --- | --- |
| Data engine | [Siegfriex/mbN_GUIDE](https://github.com/Siegfriex/mbN_GUIDE) | Notebook-first collection, normalization, geo, embeddings, retrieval, ranking, release build | Artifact-level lineage and the M14R1 release snapshot from an authorized local checkout |
| Portfolio hub | [Siegfriex/nbm_guides](https://github.com/Siegfriex/nbm_guides) | This concise, safe-to-share project index | Documentation, reproducibility notebook, snapshot verifier, no sensitive corpus artifacts |
| Product UI | [mbn-guide-front.vercel.app](https://mbn-guide-front.vercel.app) | Mobile GUIDE/DISCOVER interaction surface | URL reachability and deployed UI audit evidence; not an assertion that every route consumes the newest data bundle |

```text
MBN source articles
   ↓  local, notebook-first data engine
mbN_GUIDE: evidence + canonical artifacts + immutable release
   ├── nbm_guides: public method / evidence / reproduction index
   └── Vercel UI: product-consumption surface
```

The point of the split is deliberate: a portfolio should communicate the real
data-engineering work without publishing full copyrighted text, credentials,
provider responses, embeddings, or model caches.

## Verified product snapshot

The latest locally verified frontend projection is the **M14R1** release
`mbn-guide-701011c9608e4524` (`MINIMAL_SAFE_RELEASE_V1_1`). Its validation gate
passed with documented warnings, while all structural/safety counters below
were zero.

| Released asset | Count | What it means |
| --- | ---: | --- |
| Articles | 461 | Release-safe article metadata; no full article body |
| Map-safe places | 19 | Canonical places with coordinate/provenance/why-it-matters gates |
| Place recommendations | 109 | Contract-compatible entity-to-entity recommendations |
| Related articles | 4,610 | 10 exact semantic neighbours for each of 461 article contexts |
| Stories | 0 | Deliberately empty: no canonical StoryBundle producer was fabricated |
| Product taxonomy categories | 8 | DOCS-authoritative product taxonomy, distinct from editorial labels |

The M14R1 audit reported zero JSON parse errors, duplicate IDs, broken FKs,
rank gaps, non-finite scores, missing related-article reasons, manifest/hash/
byte mismatches, and credential leaks. `M14R1_RELEASE_BUILT` and
`FRONTEND_READY` describe the data handoff; they do **not** claim that every
frontend route or future release is automatically deployed.

## Release and runtime boundary

The Vercel UI was reachable with HTTP 200 during the portfolio audit:
[https://mbn-guide-front.vercel.app](https://mbn-guide-front.vercel.app).
Deployed mobile UI captures also recorded no browser console/page/request errors
for the audited routes at that point.

This is intentionally a **two-part claim**:

1. M14R1 validates the release bundle itself—schema, IDs, FKs, reason evidence,
   manifest bytes/hashes, and secret scan.
2. The Vercel URL demonstrates a deployed UI surface.

The portfolio does not claim an unverified deployment pointer or silently say
that the visible Vercel UI consumes `mbn-guide-701011c9608e4524`. Wiring a
pinned release ID into the frontend remains a separately auditable handoff.

## The engineering story

### 1. Corpus and evidence, not keyword-only extraction

The pipeline first collected and normalized MBN index, title, article body, and
body-block records. Candidate extraction uses contextual rules and preserves
mention boundaries, block IDs, confidence, and rejection reasons. This avoids
turning a product name, a work title, or incidental brand mention into a venue.

### 2. Conservative geography

M7 resolved a validated queue through the TourAPI evidence route. In the frozen
V1 milestone it produced 25 `CanonicalPlace` objects, 7 `CultureEvent` objects,
and 32 map-eligible geo objects from a 265-call provider execution. Map
eligibility is separate from identity resolution: a usable coordinate,
why-it-matters evidence, and article relation are all required.

### 3. Frozen vector space and matrix-first retrieval

M8 chose the pinned `BAAI/bge-m3` revision and created 461 title vectors,
1,062 body-chunk vectors, and 32 entity vectors (all 1,024 dimensions). M9
then reused those frozen arrays—no re-embedding or FAISS—and computed exact
matrix similarities. Its selected recipe was body-only:

```text
BodySim(i, j) = 0.70 × max(chunk cosine) + 0.30 × mean(top-3 chunk cosine)
```

The resulting V1 graph contains 9,220 directed article-to-article Top-20
relations and 2,305 article-to-entity Top-5 relations. Formula samples,
vector/metadata alignment, rank continuity, and relation FKs are audited as
separate gates.

### 4. Retrieval is kept separate from ranking

M10 stores observed MBN editorial labels as weak evidence—not as an invented
product taxonomy. M11 unions semantic, direct-source, shared-entity, and
geographic candidate evidence without calculating a final score. M12 applies
candidate-set-specific, missing-feature-aware scoring and MMR only where it is
appropriate. This prevents a missing temporal or taxonomy feature from being
misread as a zero-value feature.

### 5. Contract-safe release projection

M13/M14/M14R1 project only object types allowed by the frontend contract.
Notable non-coercion rules:

- `CultureEvent` is not cast to `Place` when the frontend has no Event schema.
- Article recommendations are not cast to a fake StoryBundle.
- The 58 observed MBN editorial labels are not cast to the eight product
  taxonomy categories.
- Missing stories remain `[]`; automatic clustering is not passed off as an
  editorial story.

Each release is assembled atomically into a deterministic directory, with
manifest rows, byte sizes, and SHA-256 values for each payload.

## Milestones and artifact evidence

| Milestone | Commit / status | Deliverable |
| --- | --- | --- |
| M7 | `76a4d59` · `M7_GEO_READY` | Canonical place/event replay and map-safety QA |
| M8 | `b8e01c3` · `M8_EMBEDDING_READY` | Pinned BGE-M3 embeddings and numerical QA |
| M9 | `e5cd8e6` · `M9_SEMANTIC_READY` | Exact body-first semantic relation graph |
| M10 | `f451043` | Evidence-traceable editorial-label classification |
| M11 | `ea4e24b` | Four candidate sets, evidence separated from candidates |
| M12 | `afe4d57` · `M12_RANKING_READY` | Explainable ranking, MMR, and reason evidence |
| M13 / M14 | `402f87d` / `09a0598` | Immutable release build and validation |
| M14R1 | `69cb899` · `FRONTEND_READY` | Full related-article projection and compact place ranks |

The notebook validates the release from local artifacts rather than relying on
these prose numbers alone.

## Evidence and validation

| Gate | Verified outcome | Why it matters |
| --- | --- | --- |
| M7 geo | Broken FK / invalid coordinate / unsafe pin promotion = 0 | A search hit cannot become a map object without evidence and coordinates |
| M8 vectors | NaN / Inf / zero vector / metadata mismatch = 0 | Retrieval starts from aligned, pinned vector artifacts |
| M9 relations | Formula sample mismatch / self relation / broken FK = 0 | Exact Top-K relations have independently checkable math |
| M12 ranking | Candidate loss / rank gap / reason mismatch = 0 | Retrieval, ranking, and explainability remain separate |
| M14R1 release | JSON parse / duplicate ID / broken FK / manifest+hash+byte mismatch / secret leak = 0 | The release is safe to hand off as a pinned artifact |
| Portfolio notebook | Manifest SHA/bytes recomputed from the local source checkout | README metrics are not the only evidence |

See [the evidence index](docs/EVIDENCE_INDEX.md) for exact artifact paths,
release files, and what each check can—and cannot—establish.

## Reproduce the portfolio checks

This repository is intentionally small. It does not mirror the data engine or
download raw source material. To run the notebook, use an authorized local
`mbN_GUIDE` checkout that contains the M14R1 artifacts and point the environment
variable at that directory.

```bash
git clone https://github.com/Siegfriex/nbm_guides.git
cd nbm_guides
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# Supply a local data-engine snapshot with M14R1 artifacts.
export MBN_GUIDE_PY_ROOT=/absolute/path/to/mbN_GUIDE
jupyter lab notebooks/MBN_GUIDE_PORTFOLIO_REPRODUCIBILITY.ipynb
```

The notebook checks the M14R1 manifest against actual payload bytes and hashes,
loads the M14R1 validation gate, and reports the one-year backfill checkpoint
without re-running crawls, providers, embeddings, or LLM work.

For a non-notebook CI-style check after setting `MBN_GUIDE_PY_ROOT`:

```bash
python scripts/verify_portfolio_snapshot.py
```

## One-year expansion: current boundary

The frozen V1 release above is not retroactively changed by the expansion work.
The deterministic checkpoint is useful but is **not a new production release**:

| Item | Current checked result |
| --- | --- |
| Historical interval | 2025-08-08 to 2025-12-31 |
| New index records | 875 |
| New eligible articles | 283 |
| Combined index / eligible corpus | 2,297 / 744 |
| Parsed body blocks | 16,190 |
| Rule mentions / mappable candidates | 4,523 / 1,615 |
| Combined title / body-chunk vectors | 744 / 1,701 |
| Pre-LLM distribution verdict | `PRE_LLM_STABLE` |
| Independent LLM + provider delta | Not included in this release snapshot |

Gold V2 and Detector V2 are intentionally not claimed here. Their planned
evaluation must remain distinct from the frozen V1 evidence and from the
frontend release.

## Repository map

```text
notebooks/
  MBN_GUIDE_PORTFOLIO_REPRODUCIBILITY.ipynb  # audit-oriented walkthrough
data/
  portfolio_snapshot.json                    # public aggregate evidence card
docs/
  EVIDENCE_INDEX.md                          # paths, gates, limits, release/runtime boundary
scripts/
  verify_portfolio_snapshot.py               # manifest + critical-gate verifier
requirements.txt                             # lightweight notebook deps
README.md                                    # public portfolio narrative
```

## Safety and limitations

- The public portfolio omits API keys, provider raw responses, raw HTML,
  complete article bodies, model weights, embedding vectors, and internal LLM
  prompts/responses.
- M10 labels are editorial weak signals, not human-validated semantic genre
  truth.
- Weak retrieval evidence is not represented as human relevance gold.
- Event projection, StoryBundle production, and article-context recommendation
  enums remain explicit product-contract gaps where unsupported.
- The Vercel URL was reachable at the time this portfolio was updated; the
  deployment itself remains a separate frontend responsibility.

---

Built as an evidence-first local data-engineering project: every user-facing
projection is downstream of a versioned artifact, a manifest, and a validation
gate.
