# 데이터 이용 고지

## MBN 기사

이 포트폴리오는 MBN 기사 원문이나 전체 본문을 재배포하지 않습니다. 공개 범위는
release-safe metadata, ID, hash, provenance, aggregate와 소수 score sample입니다.
기사 링크와 저작권은 원 출처에 귀속됩니다.

## 한국관광공사 TourAPI

TourAPI는 장소 검색·분류·좌표 확인을 위한 외부 Provider입니다. 공개 저장소에는
service key와 raw response를 저장하지 않습니다. `mapX/mapY` WGS84 좌표,
`ContentTypeId`, `lclsSystm1/2/3`, 이미지 저작권 유형 `cpyrhtDivCd`를 서로 다른
근거 필드로 취급하며, 이미지 재사용은 provenance와 저작권 유형을 확인한 경우에만
허용합니다.

## Embedding과 추천

`BAAI/bge-m3` model/revision, vector shape와 QA 통계는 공개하지만 전체 vector,
model weights, matrix cache는 공개하지 않습니다. semantic score는 사용자 선호
확률이 아니며, 추천은 contextual/content-based heuristic입니다.

## 제품 화면

`assets/vercel/` 이미지는 `https://mbn-guide-front.vercel.app/`의 실제 배포 화면을
읽기 전용으로 캡처한 검증 증거입니다. `assets/screens/`는 별도로 표시한 디자인
prototype이며 운영 기능 증거가 아닙니다.
