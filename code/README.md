# AI 시대의 파이썬 데이터 시각화 - 실습 코드 저장소

이 저장소는 **[AI 시대의 파이썬 데이터 시각화]** 도서의 독자들을 위한 공식 실습 코드 및 데이터셋을 제공합니다. 
책에서 다루는 모든 시각화 차트와 최종 대시보드 프로젝트를 여러분의 컴퓨터에서 직접 실행해 볼 수 있습니다.

## 📂 저장소 구조

- `data/` : 실습에 사용되는 가상의 테크 스타트업 데이터셋 (`tech_startup_sales.csv`)
- `ch03_top4_charts.ipynb` : 3장 시각화 실전 Top 4 (선형, 막대, 산점도 등) 실습
- `ch04_customization.ipynb` : 4장 차트 디자인 튜닝 실습
- `ch05_statistics.ipynb` : 5장 통계 요약과 분포 차트 (히스토그램, 박스플롯) 실습
- `ch06_interactive.ipynb` : 6장 Plotly 기반 인터랙티브 차트 실습
- `app.py` : 7~8장 최종 목표인 Streamlit 대시보드 애플리케이션 소스 코드
- `requirements.txt` : 실습에 필요한 파이썬 라이브러리 목록

## 🚀 시작하기

이 프로젝트를 로컬 환경에서 실행하려면 파이썬(Python 3.9 이상 권장)이 설치되어 있어야 합니다.

### 1. 저장소 클론 및 이동
```bash
git clone https://github.com/your-repo/python-visualization-code.git
cd python-visualization-code
```

### 2. 패키지 설치
가상환경을 생성하고 필요한 라이브러리를 설치합니다.
```bash
# 가상환경 생성 및 활성화 (선택 사항이지만 권장)
python -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows

# 의존성 패키지 설치
pip install -r requirements.txt
```

### 3. 실습 진행

**주피터 노트북 실행하기 (1~6장)**
```bash
jupyter notebook
```
원하는 챕터의 `.ipynb` 파일을 열어 셀을 하나씩 실행해 봅니다.

**Streamlit 대시보드 실행하기 (7~8장)**
```bash
streamlit run app.py
```
명령어를 실행하면 브라우저가 열리며 최종 실습 결과물인 '스타트업 KPI 대시보드'를 확인할 수 있습니다.

## 📝 폰트 설정 안내 (Mac/Windows)
본 저장소의 시각화 코드는 기본적으로 'NanumBarunGothic' 또는 'AppleGothic'을 기준으로 작성되어 있습니다. 
만약 차트에서 한글이 깨진다면, 주피터 노트북의 폰트 설정 부분을 여러분의 운영체제에 설치된 한글 폰트 이름(예: `Malgun Gothic`)으로 수정해 주세요.
