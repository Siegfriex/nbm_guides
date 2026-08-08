# MBN GUIDE 공개 증거 조정 보고서

검증일: 2026-08-08
정책: 원천 `mbN_GUIDE/nbM_GUIDE_PY`는 읽기 전용, 공개 claim은 source commit·artifact path·SHA-256에 연결

## 판정 기준

- `PUBLIC`: 원격 source 또는 공개 재현 저장소에서 bytes와 SHA를 검증할 수 있음
- `SANITIZED_PUBLIC`: 원천 raw는 비공개지만 안전한 snapshot·aggregate·manifest로 검증 가능
- `LOCAL_ONLY`: 로컬에는 존재하나 공개 release claim으로 승격하지 않음
- `REMOVED`: 실제 source에서 찾을 수 없어 claim에서 제거

## Claim reconciliation

| claim | 기존 portfolio 값 | 공개 source 값 | 로컬 source 값 | source repo / branch | commit | artifact path | SHA-256 | 공개 검증 | 최종 결정과 이유 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| source HEAD | `69cb899`처럼 보일 수 있음 | `09a059859cc42121e96cb266951af91108e577eb` | `69cb89918134455c6031b62ab6d200c4b9c0daeb` | `Siegfriex/mbN_GUIDE` / `nbM_GUIDE_PY` | 양쪽 값 분리 | Git ref | 해당 없음 | PUBLIC | README는 공개 HEAD와 local-only HEAD를 구분한다. |
| M14 baseline release | `mbn-guide-dc9f6a80d54985d6` | 존재 | 존재 | `Siegfriex/mbN_GUIDE` / `nbM_GUIDE_PY` | `402f87d` build, `09a0598` validation | `data/90_exports/frontend/mbn-guide-dc9f6a80d54985d6/manifest.json` | `2d8b33f8919421d1c8f72cf644274d635a137c25a2e8b5cdf6057df2beb177b0` | PUBLIC | 공개 baseline으로 유지하되 최신 제품 화면 기준은 M14R1이다. |
| M14R1 release | `mbn-guide-701011c9608e4524` | 원격 source tree에는 없음 | 존재 | `Siegfriex/mbN_GUIDE` / `nbM_GUIDE_PY` | source lineage `afe4d570cea3aa17ac05fe98e85cf5cc0a6a8439`; local build `69cb89918134455c6031b62ab6d200c4b9c0daeb` | `data/90_exports/frontend/mbn-guide-701011c9608e4524/manifest.json` | `7e082df9ee9e8a0b1328c951b8df915fa2bc73a8bbc9c6eaf1b5733d967ef4da` | SANITIZED_PUBLIC | sanitized bundle과 M14R1 gate, Vercel bundle의 동일 releaseId를 공개한다. local build commit은 공개 HEAD로 주장하지 않는다. |
| M14R1 article | 461 | baseline도 461 | 461 | 동일 | `afe4d57` lineage | M14R1 `manifest.json` | 위 manifest SHA | SANITIZED_PUBLIC | 유지. Claim Registry에서 독립 row count 검증. |
| M14R1 Place | 19 | baseline도 19 | 19 | 동일 | `afe4d57` lineage | M14R1 `places.json` | manifest per-file SHA | SANITIZED_PUBLIC | 유지. 좌표·whyItMatters·FK gate를 공개 Notebook에서 재검증. |
| M14R1 recommendation | 109 | baseline도 109 | 109 | 동일 | `afe4d57` lineage | M14R1 `recommendations.json` | manifest per-file SHA | SANITIZED_PUBLIC | 유지. Article 관계는 recommendation enum으로 강제 변환하지 않음. |
| M14R1 related article | 공개 baseline에는 별도 계약 없음 | 없음 | 4,610 | 동일 | `afe4d57` lineage | M14R1 `related_articles.json` | manifest per-file SHA | SANITIZED_PUBLIC | 유지. Vercel DISCOVER 화면과 공개 payload를 함께 제시. |
| M7 geo | query 265 / resolved 32 / ambiguous 20 / not-found 213 | 동일 | 동일 | `Siegfriex/mbN_GUIDE` / `nbM_GUIDE_PY_M7_GEO` | `76a4d59fe792188453bae72d8632742b267cb1f5` | `data/30_geo/mbn/m7/run_20260808_m7_geo/geo_quality_report.json` | `53ce2d3dbce88572819ce69bb697359a0dc377d639801edc7d05b4a40e6347cb` | PUBLIC | 유지. aggregate gate를 공개 재현 저장소에 보존. |
| M8 embedding | 461 / 1,062 / 32 / 1,024 | 동일 | 동일 | `Siegfriex/mbN_GUIDE` / `nbM_GUIDE_PY_M8_EMBEDDING` | `b8e01c38e571790e453b4e3bffd4ac9c6dcb2fdd` | `data/40_semantic/mbn/m8/run_20260808_m8_embeddings/m8_final_gate.json` | `617efe99e96c074f99eb5784d143605add4320fad756e86dadf1d15de6c18b9c` | PUBLIC | 유지. raw vector는 제외하고 contract·shape·QA만 공개. |
| M9 semantic | 9,220 / 2,305 / Recall@5 1.0 / MRR 0.896666… | 동일 | 동일 | `Siegfriex/mbN_GUIDE` / `nbM_GUIDE_PY_M9_SEMANTIC` | `e5cd8e6` | M9 final gate와 quality report | Claim Registry 참조 | PUBLIC | 유지하되 25-query Silver이고 Human Gold가 아님을 명시. |
| M15 one-year | 744 eligible, 2,297 index 등의 local claim 가능 | 공개 release 아님 | checkpoint 존재 | `Siegfriex/mbN_GUIDE` local / `nbM_GUIDE_PY` | `2f81802` 이후 local work | M15 checkpoint/quality artifacts | 공개 snapshot 없음 | LOCAL_ONLY | Hero·공개 결과 수치에서 제외. 후속 실험이라고만 기록. |
| Vercel release linkage | 과거에는 최신 bundle 소비 여부 불명확 | 배포 URL과 bundle은 공개 | 동일 | `mbn-guide-front.vercel.app` | 배포 bundle `index-DA6F9xmu.js` | `/assets/index-DA6F9xmu.js` | `034c89371783ea2cd7cbc5157254180cd05eea7f3de589d27536c077ff8781a4` | PUBLIC | bundle 내부 releaseId와 profile을 확인했고 실제 route 4개를 캡처. |

## 해결된 충돌

1. **공개 source HEAD와 local HEAD를 분리했습니다.** `69cb899`을 원격 source HEAD라고 쓰지 않습니다.
2. **M14 baseline과 M14R1을 분리했습니다.** baseline은 공개 source에, M14R1은 sanitized evidence와 실제 배포 bundle에 연결했습니다.
3. **M15를 공개 릴리스 성과에서 내렸습니다.** 완료되지 않은 local checkpoint를 1년 production corpus로 주장하지 않습니다.
4. **related article과 recommendation을 분리했습니다.** Article→Article 4,610건을 frontend Place recommendation 109건과 합치지 않습니다.
5. **taxonomy 권위를 세 층으로 분리했습니다.** editorial label, TourAPI classification, product taxonomy를 같은 category로 취급하지 않습니다.

## 공개 검증 위치

- Claim Registry: `Siegfriex/nbm_guide_py/data/evidence/portfolio_claims.json`
- Sanitized release: `Siegfriex/nbm_guide_py/data/public_release/mbn-guide-701011c9608e4524/`
- 공개 Notebook: `Siegfriex/nbm_guide_py/notebooks/`
- 실제 제품 화면: `https://mbn-guide-front.vercel.app/`

결론: 공개 핵심 claim은 source lineage 또는 sanitized bytes와 실제 배포 증거에 연결됩니다. local-only M15는 공개 release에서 제외합니다.
