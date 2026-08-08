<div align="center">

**Data & AI**

[![Python](https://img.shields.io/badge/Python-Local%20data-3776AB?logo=python&logoColor=white)](https://www.python.org/) [![pandas](https://img.shields.io/badge/pandas-Parquet-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/) [![BGE--M3](https://img.shields.io/badge/BAAI-BGE--M3-FF6F61)](https://huggingface.co/BAAI/bge-m3) [![Jupyter](https://img.shields.io/badge/Jupyter-Notebook--first-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)

**Frontend & release**

[![React](https://img.shields.io/badge/React-TypeScript-61DAFB?logo=react&logoColor=black)](https://react.dev/) [![Vite](https://img.shields.io/badge/Vite-Frontend-646CFF?logo=vite&logoColor=white)](https://vite.dev/) [![Vercel](https://img.shields.io/badge/Vercel-Live%20UI-000000?logo=vercel)](https://mbn-guide-front.vercel.app) [![Release](https://img.shields.io/badge/M14R1-FRONTEND__READY-1F8B4C)](#-release-validation--runtime-boundary)

# MBN GUIDE

### Discover Korea. Understand the Culture. Act with Confidence.

**MBN 문화 기사 → 근거 기반 Place/Event → 정확한 semantic retrieval → 검증된 frontend data release**

[Product](#-product-thesis) · [Screens](#-prototype-screens) · [Data & AI](#-data--ai-pipeline) · [Release](#-release-validation--runtime-boundary) · [Reproduce](#-reproduce) · [Evidence](docs/EVIDENCE_INDEX.md)

</div>

---

## Product thesis

MBN GUIDE는 흩어진 지도·SNS·기사·영상 정보를 한 번에 “추천”하는
서비스가 아니라, **MBN 콘텐츠의 문화적 맥락을 장소 탐색으로 재구성하고
그 추천의 근거를 보존**하는 location-based culture discovery 프로젝트입니다.

```text
DISCOVER → CONTEXT → TRUST → INTENT → ACTION
```

| Surface | 사용자가 얻는 답 | 현재 데이터 역할 |
| --- | --- | --- |
| GUIDE | 지금 어디를 경험할 수 있는가 | map-safe canonical place, 위치, why-it-matters |
| DISCOVER | 왜 이 장소·콘텐츠가 연결되는가 | MBN article metadata, related-article relation, provenance |
| LIVE | 다음 행동을 무엇으로 연결할 수 있는가 | 현재는 context/UX boundary; 실제 commerce는 별도 가설 |

> Product claim: **문화 탐색과 근거 기반 콘텐츠 연결**. 결제, 재고, 예약,
> Tax Refund, 파트너 계약, 매출 성과는 이 포트폴리오에서 주장하지 않습니다.

## Three surfaces, one evidence chain

| Surface | Link | Responsibility | Portfolio claim |
| --- | --- | --- | --- |
| Data engine | [Siegfriex/mbN_GUIDE](https://github.com/Siegfriex/mbN_GUIDE) | notebook-first collection, entity evidence, geo, embeddings, retrieval, ranking, immutable release build | Authorized local artifact snapshot의 lineage와 M14R1 release를 검증 |
| Portfolio index | [Siegfriex/nbm_guides](https://github.com/Siegfriex/nbm_guides) | 이 공개 프로젝트 허브 | method, aggregate metrics, reproducibility, limitations를 안전하게 공개 |
| Live UI | [mbn-guide-front.vercel.app](https://mbn-guide-front.vercel.app) | GUIDE/DISCOVER/LIVE mobile interaction surface | 배포 UI reachability를 확인; 최신 bundle 소비 여부는 별도 integration gate |

```text
MBN article source
   ↓  local, notebook-first producer
mbN_GUIDE: evidence → canonical objects → vectors → relations → ranking → immutable JSON
   ├── nbm_guides: public portfolio / reproducibility / evidence index
   └── Vercel: frontend-consumption surface
```

이 분리는 의도적입니다. 원문 body/HTML, API key, provider raw response,
model weight, vector, matrix cache, 내부 LLM response를 GitHub 포트폴리오에
넣지 않고도 데이터 엔지니어링 결과를 확인 가능하게 만듭니다.

## Prototype screens

아래 화면은 제품 경험과 인터랙션 가설을 설명하는 prototype asset입니다.
이 화면이 payment·inventory·partner integration의 운영 증거라는 뜻은 아닙니다.

| GUIDE | DISCOVER |
| --- | --- |
| ![MBN GUIDE prototype 1](assets/screens/01-mbn-guide.png) | ![MBN GUIDE prototype 2](assets/screens/02-mbn-guide.png) |

| Place / content context | LIVE concept |
| --- | --- |
| ![MBN GUIDE prototype 3](assets/screens/03-mbn-guide.png) | ![MBN GUIDE prototype 4](assets/screens/04-mbn-guide.png) |

<details>
<summary>Additional prototype screens</summary>

![MBN GUIDE prototype 5](assets/screens/05-mbn-guide.png)

![MBN GUIDE prototype 6](assets/screens/06-mbn-guide.png)

![MBN GUIDE prototype 7](assets/screens/07-mbn-guide.png)

![MBN GUIDE prototype 8](assets/screens/08-mbn-guide.png)

![MBN GUIDE prototype 9](assets/screens/09-mbn-guide.png)

![MBN GUIDE prototype 10](assets/screens/10-mbn-guide.png)

</details>

## Data & AI pipeline

### From articles to a canonical culture graph

```text
MBN index + title + article body
  → normalized article / body-block corpus
  → context-bound culture mention candidates
  → independent verification + provider observation
  → CanonicalPlace / CultureEvent + article evidence relations
  → BGE-M3 title, body-chunk, entity vectors
  → exact body-first semantic matrices
  → candidate retrieval → explainable ranking
  → contract-safe JSON projection → manifest / hash / FK validation
```

The critical engineering rule is provenance:

```text
article → evidence block → verification → provider observation → canonical object
```

A name match alone never becomes a map pin. Ambiguous, not-found, and error
states remain explicit; `ProviderObservation` is not silently collapsed into a
`CanonicalPlace`.

### Extraction and normalization

1. Preserve stable `articleId`, source URL, raw title, publication metadata, and raw hash.
2. Parse body into deterministic blocks; retain parser version, parse status, and body hash.
3. Generate context-aware culture candidates with span/block evidence instead of publishing keyword hits directly.
4. Keep rejection reasons (for example false venue, product-not-place, invalid span) as data quality evidence.

This makes the pipeline inspectable when a candidate is rejected or a provider
result is not promoted.

### Conservative geo resolution (M7)

Frozen V1 M7 executed 265 TourAPI calls and produced:

| Object / state | Count |
| --- | ---: |
| CanonicalPlace | 25 |
| CultureEvent | 7 |
| Map-eligible objects | 32 |
| AUTO_RESOLVED | 32 |
| AMBIGUOUS | 20 |
| NOT_FOUND | 213 |
| ERROR | 0 |

Map eligibility requires valid coordinates, why-it-matters evidence, and a
traceable article relation. A provider search response is therefore an input to
resolution—not frontend truth by itself.

### Frozen vector space and exact retrieval (M8–M9)

M8 selected the pinned `BAAI/bge-m3` revision and audited numerical integrity
before use. M9 loads those arrays once and uses matrix multiplication rather
than re-embedding, FAISS, or Python pairwise cosine loops.

| Frozen V1 input | Shape / count |
| --- | ---: |
| Article title vectors | 461 × 1,024 |
| Body-chunk vectors | 1,062 × 1,024 |
| Culture-entity vectors | 32 × 1,024 |
| Article → Article Top-20 relations | 9,220 |
| Article → Entity Top-5 relations | 2,305 |

Selected article body score:

```text
BodySim(i, j) = 0.70 × max(chunk-pair cosine)
              + 0.30 × mean(top-3 chunk-pair cosine)
```

The score is a retrieval measurement, not a user preference model or a
probability. Formula samples, rank continuity, self-relations, FKs, and vector
metadata alignment are audited independently.

### Retrieval, ranking, and reason evidence (M10–M12)

| Stage | What it does | Important non-claim |
| --- | --- | --- |
| M10 | Stores normalized MBN editorial labels and evidence | The 58 labels are not an authoritative product taxonomy or human genre gold |
| M11 | Unions semantic, direct-source, shared-entity, and geo candidate evidence | It does not calculate a global final score |
| M12 | Applies candidate-set-specific, missing-feature-aware ranking and MMR | No popularity, personalization, sponsored boost, or fabricated reason |

M11 constructed 13,084 candidates and M12 preserved all rankable candidates
while producing 7,522 internal Top-K selections. M13/M14 only project targets
the frontend contract can represent; unsupported candidate types are recorded
as explicit exclusions rather than coercions.

## Release validation & runtime boundary

### Latest locally verified release

The current local evidence snapshot is M14R1 release
`mbn-guide-701011c9608e4524` (`MINIMAL_SAFE_RELEASE_V1_1`).

| Frontend-safe payload | Rows | Purpose |
| --- | ---: | --- |
| `articles.json` | 461 | Safe article metadata; no full body |
| `places.json` | 19 | map-safe canonical place projection |
| `recommendations.json` | 109 | contract-compatible place recommendations |
| `related_articles.json` | 4,610 | 10 exact semantic neighbours for 461 article contexts |
| `stories.json` | 0 | No canonical StoryBundle was fabricated |
| `taxonomy.json` | 8 | DOCS-authoritative product taxonomy |

M14R1 validation is `PASS_WITH_WARNINGS` / `FRONTEND_READY` with these
critical counters at zero: JSON parse errors, duplicate IDs, broken FKs, rank
gaps, non-finite scores, missing relation reasons, manifest/hash/byte mismatch,
and secret leak.

### What the Vercel link proves—and what it does not

[https://mbn-guide-front.vercel.app](https://mbn-guide-front.vercel.app) was
reachable with HTTP 200 during the portfolio audit. Deployed mobile UI capture
records also had no recorded console, page, or request failures for the audited
routes.

That is intentionally not the same claim as “Vercel consumes the newest M14R1
bundle.” The portfolio only claims:

1. the data producer has a manifest-validated immutable release; and
2. the frontend has a reachable deployed UI surface.

A pinned frontend release pointer, real coordinate consumption, and release-ID
ingress are integration work that should have their own audit before being
called complete.

## Evidence ledger

| Gate | Checked outcome | Why it matters |
| --- | --- | --- |
| M7 geo | unsafe promotion / invalid coordinate / broken geo FK = 0 | Search output cannot silently become a map object |
| M8 embeddings | NaN / Inf / zero / metadata mismatch = 0 | Vector artifacts are aligned and pinned |
| M9 semantic | formula mismatch / self relation / broken FK = 0 | Exact Top-K relations are mathematically inspectable |
| M12 ranking | candidate loss / rank gap / reason mismatch = 0 | Retrieval, score, and reason remain separable |
| M14R1 | duplicate / FK / hash / byte / secret failures = 0 | Bundle is safe to hand off as a pinned artifact |
| Portfolio verifier | Manifest bytes and SHA-256 recomputed | README values are not the sole authority |

Exact artifact paths, release file names, exclusions, and limitations are in
[docs/EVIDENCE_INDEX.md](docs/EVIDENCE_INDEX.md).

## Reproduce

This repository is deliberately a lightweight public index. For read-only
reproduction, supply an authorized local `mbN_GUIDE` checkout containing the
M14R1 artifacts. The commands below do not crawl, call providers, load a model,
invoke an LLM, rewrite a release, or mutate the frontend.

```bash
git clone https://github.com/Siegfriex/nbm_guides.git
cd nbm_guides
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

export MBN_GUIDE_PY_ROOT=/absolute/path/to/mbN_GUIDE
jupyter lab notebooks/MBN_GUIDE_PORTFOLIO_REPRODUCIBILITY.ipynb

# Optional non-notebook verification
python scripts/verify_portfolio_snapshot.py
```

The notebook is the primary walkthrough: it recomputes release payload hashes,
reads the M14R1 validation gate, displays product-safe counts, and reports the
one-year checkpoint without promoting it to a release.

## One-year expansion: explicit current boundary

Frozen V1/M14R1 is not retroactively rewritten by the one-year backfill.
Current deterministic checkpoint:

| Item | Result |
| --- | --- |
| Historical interval | 2025-08-08 to 2025-12-31 |
| New index / eligible articles | 875 / 283 |
| Combined index / eligible articles | 2,297 / 744 |
| Parsed body blocks | 16,190 |
| Rule mentions / mappable candidates | 4,523 / 1,615 |
| Combined title / body-chunk vectors | 744 / 1,701 |
| Pre-LLM temporal verdict | `PRE_LLM_STABLE` |
| Release replacement | No |

Gold V2, Detector V2, and full independent LLM/provider replay are not claimed
as a completed public release here. This is a checkpoint, not a hidden quality
upgrade.

## Project map

```text
README.md                                      # product, pipeline, release, boundaries
assets/screens/                                 # prototype screens, not operational commerce proof
notebooks/MBN_GUIDE_PORTFOLIO_REPRODUCIBILITY.ipynb
data/portfolio_snapshot.json                   # public aggregate evidence card
docs/EVIDENCE_INDEX.md                         # artifact paths and limitations
scripts/verify_portfolio_snapshot.py           # read-only release verifier
requirements.txt                               # notebook dependencies
```

## Scope & disclosure

- Public repo excludes raw article body/HTML, provider payloads, credentials,
  vectors, model weights, matrix caches, and internal LLM traces.
- Event → Place, Article → StoryBundle, and editorial label → product taxonomy
  coercion are prohibited; unsupported surfaces remain documented gaps.
- Weak retrieval evidence is not human relevance gold; M10 labels are not
  authoritative semantic taxonomy.
- No claim is made about partner deals, revenue, inventory, payment, reservation,
  fulfillment, or production commerce operations without separate evidence.

---

Built as an evidence-first data-engineering portfolio: every user-facing data
projection is downstream of a versioned artifact, a manifest, and a validation
gate.
