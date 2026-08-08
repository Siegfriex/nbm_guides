# MBN GUIDE 증거 인덱스

## 한눈에 찾기

| 질문 | 공개 근거 |
| --- | --- |
| 수치가 실제 artifact와 연결되는가 | [`portfolio_claims.json`](../reports/portfolio_claims.json) |
| 공개·로컬 source가 왜 다른가 | [`EVIDENCE_RECONCILIATION.md`](../reports/EVIDENCE_RECONCILIATION.md) |
| release bytes를 재검증할 수 있는가 | [`nbm_guide_py`](https://github.com/Siegfriex/nbm_guide_py/tree/agent/portfolio-final-evidence) |
| 제품에서 실제 보이는가 | [Vercel GUIDE](https://mbn-guide-front.vercel.app/guide), [`assets/vercel`](../assets/vercel/) |
| 원천 알고리즘과 milestone은 어디인가 | [`mbN_GUIDE/nbM_GUIDE_PY`](https://github.com/Siegfriex/mbN_GUIDE/tree/nbM_GUIDE_PY) |

## 공개 release

- releaseId: `mbn-guide-701011c9608e4524`
- profile: `MINIMAL_SAFE_RELEASE_V1_1`
- source lineage commit: `afe4d570cea3aa17ac05fe98e85cf5cc0a6a8439`
- local-only build commit: `69cb89918134455c6031b62ab6d200c4b9c0daeb`
- manifest SHA-256: `7e082df9ee9e8a0b1328c951b8df915fa2bc73a8bbc9c6eaf1b5733d967ef4da`
- sanitized bundle: `nbm_guide_py/data/public_release/mbn-guide-701011c9608e4524/`

## Stage별 근거

| Stage | 공개 evidence | 핵심 QA |
| --- | --- | --- |
| M7 Geo | `geo_quality_report.json`, geo sample | invalid coordinate / broken provenance 0 |
| M8 Embedding | `m8_final_gate.json` | NaN / Inf / zero / metadata mismatch 0 |
| M9 Semantic | gate, quality report, relation sample | self / duplicate / FK / formula mismatch 0 |
| M11–M12 | gate, ranking sample | candidate loss / rank gap / reason mismatch 0 |
| M14R1 | sanitized bundle, validation gate | schema / FK / hash / byte / secret 0 |
| Vercel | 4 route screenshot, bundle SHA | deployed releaseId 확인 |

## 공개에서 제외한 자료

- MBN 전체 기사 본문과 raw HTML
- Provider raw response와 credential
- embedding 전체 vector와 model weight/cache
- 내부 LLM prompt/response와 adjudication trace
- local-only M15 checkpoint의 비공개 artifact

세부 이용 조건은 [`DATA_NOTICE.md`](../DATA_NOTICE.md)를 확인하십시오.
