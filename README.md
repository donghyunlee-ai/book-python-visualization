# AI 시대의 파이썬 데이터 시각화 — 예제 코드

> AI ERA SERIES 02 · 이동현 지음

『AI 시대의 파이썬 데이터 시각화』의 장별 예제 코드·대시보드·실습 데이터
저장소입니다. matplotlib로 그리는 첫 차트에서 Plotly 인터랙티브 차트,
Streamlit 대시보드의 웹 배포까지 한 권으로 완주하는 책입니다.

이 책의 규율은 **그리기 전에, 보여줄 하나를 정하라**입니다.

## 구조

```
code/
├── ch01/, ch02/, ch04/, ch05/     장별 예제 스크립트
├── ch03_top4_charts.ipynb          3장  네 가지 기본 차트
├── ch04_customization.ipynb        4장  꾸미기
├── ch05_statistics.ipynb           5장  통계 시각화
├── ch06_interactive.ipynb          6장  Plotly 인터랙티브
├── app.py · charts.py · data.py    7장  Streamlit 대시보드 (8장에서 그대로 배포)
├── fonts/                          한글 폰트 (나눔고딕, OFL)
├── data/                           실습 데이터
└── requirements.txt                고정 버전 (재현 환경)
```

## 실행 환경

```bash
pip install -r code/requirements.txt
streamlit run code/app.py
```

- 버전은 `requirements.txt`에 고정되어 있습니다(책 본문과 동일한 재현 환경).
- 7장의 세 모듈(`app.py`·`charts.py`·`data.py`)은 한 줄도 고치지 않고
  8장의 배포 실습에 그대로 사용됩니다.

## 실습 데이터

- `data/subway.csv`, `data/CARD_SUBWAY_MONTH_202501.csv` — 서울열린데이터광장
  제공 공공데이터를 실습용으로 가공한 파일입니다(원 출처: 서울교통공사
  승하차 인원 정보).
- `data/tech_startup_sales.csv`, `data/marketing_ab_test.csv` — 실습을 위해
  생성한 가상 데이터입니다.

## 정오표

[ERRATA.md](ERRATA.md)에서 확인하세요. 오류 제보는 Issues로 부탁드립니다.

## 라이선스

- 코드: [MIT License](LICENSE)
- 폰트: 나눔고딕(SIL Open Font License)
- 본문 등 책의 콘텐츠 저작권은 저자에게 있습니다.

— [donghyunlee.kr](https://donghyunlee.kr)
