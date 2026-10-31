# AI 시대의 파이썬 데이터 시각화 — 예제 코드

『AI 시대의 파이썬 데이터 시각화 — 차트 한 장에서 대시보드까지』(이동현 지음, AI ERA SERIES 02)의 예제 저장소입니다.

## 들어 있는 것

| 파일 | 내용 |
|---|---|
| `ch01.ipynb` … `ch13.ipynb` | 장마다 노트북 하나. 셀 첫 줄의 번호(P·C·B)가 책 지면의 코드 번호와 같습니다. |
| `appendix_c.ipynb` | 부록 C "본문이 미룬 코드"의 C01–C10(C10은 `ch11_app/`의 앱을 검사) |
| `ch11_app/` | 11장 Streamlit 앱(A01–A04를 이어 적은 `app.py`)과 13장 배포용 `requirements.txt` |
| `asos_2025_daily.csv` | 12장 저장본 — 기상청 ASOS 일자료 2025년 서울·부산·강릉·제주 1,460행(12장 C05가 만드는 것과 같은 파일) |
| `requirements.txt` | 이 책의 출력을 확인한 버전 |
| `ERRATA.md` | 정오표 |
| `extra-practice/` | 5–8장 뒤 낯선 표로 질문·관측 단위·집계를 정하는 선택 과제와 별도 풀이 |
| [학습 지원 자료](learning-support/README.md) | 핵심 개념 진단·해설, 13장 프로젝트 작성 양식, 장별 목표–연습–확인 지도 |

직접 해 보기(W 번호)는 노트북의 그 자리에 문제와 빈 칸이 있고, 풀이가 있는 연습은 노트북 끝 "직접 해 보기 풀이"에서 같은 W 번호로 찾습니다.

## 여는 법

**코랩(Google Colab)**: 코랩에서 파일 메뉴의 노트북 열기에서 GitHub를 고르고 이 저장소 주소를 넣어 장의 노트북을 엽니다. 한글 글꼴은 각 노트북 맨 위의 준비 셀 가운데 **P02만 실행하고 P03은 건너뜁니다.** 12장 저장본을 쓰려면 아래의 CSV 업로드 안내도 따릅니다.

**내 컴퓨터**: Python 3.14를 먼저 설치합니다(이 책의 확인 버전은 3.14.6). 이 저장소를 내려받아(Code → Download ZIP) 압축을 풀고, `requirements.txt`와 `ch01.ipynb`가 있는 폴더에서 터미널을 엽니다. 아래 명령은 이 폴더에 가상환경 `.venv`를 만들고, 그 환경에 설치한 JupyterLab을 실행합니다. 운영체제에 맞는 한 묶음만 실행합니다.

macOS 터미널:

```bash
python3.14 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m ipykernel install --sys-prefix --name vis-book --display-name "Python (vis-book)"
.venv/bin/python -m jupyterlab
```

Windows PowerShell 또는 명령 프롬프트:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m ipykernel install --sys-prefix --name vis-book --display-name "Python (vis-book)"
.\.venv\Scripts\python.exe -m jupyterlab
```

가상환경의 Python 경로를 직접 쓰므로 별도 활성화 명령은 필요 없습니다. 다음에 열 때는 같은 폴더에서 마지막 JupyterLab 실행 명령만 다시 입력합니다([Python 가상환경 안내](https://docs.python.org/3.14/library/venv.html)).

JupyterLab에서 `ch01.ipynb`를 열고 **Python (vis-book)** 커널을 선택합니다. 임시 코드 셀에 `import sys; print(sys.executable)`을 실행합니다. 출력이 이 폴더의 `.venv/bin/python`(macOS) 또는 `.venv\Scripts\python.exe`(Windows)를 가리켜야 합니다. 다른 경로라면 위의 가상환경 Python으로 JupyterLab을 열었는지 확인하고 커널을 다시 선택합니다.

**첫 성공 확인**: 1장의 P01로 버전을 확인하고, **코랩은 P02 → C01, 내 컴퓨터는 P03 → C01** 순서로 실행합니다. P03은 Mac에서는 `AppleGothic` 그대로, Windows에서는 글꼴 이름을 `'Malgun Gothic'`으로 바꿉니다. 제목과 축의 한글이 보이고, 1~4월 값 100·120·150·130을 잇는 선과 점 네 개가 나오면 첫 차트 실행에 성공한 것입니다. 커널을 다시 시작한 뒤에도 P01 → 선택한 글꼴 준비 셀 → C01 순서로 같은 그림이 나오는지 확인합니다. P02와 P03은 다른 장에서도 둘 중 하나만 실행합니다. 따라서 환경별 준비 셀이 함께 있는 노트북은 전체 실행 대신 사용할 준비 셀을 골라 위에서 아래로 실행합니다.

**11장 앱**: 노트북 `ch11.ipynb`의 C01이 `ch11_app/sales.csv`를 만듭니다. 그다음 같은 폴더의 새 터미널에서 가상환경 Python으로 실행합니다.

```bash
# macOS
.venv/bin/python -m streamlit run ch11_app/app.py
```

```powershell
# Windows
.\.venv\Scripts\python.exe -m streamlit run ch11_app/app.py
```

**12장 API**: 인증키는 코랩이면 보안 비밀(이름 `DATA_GO_KR_KEY`)에, 내 컴퓨터면 노트북 폴더의 `.streamlit/secrets.toml`에 둡니다. 이 저장소의 `.gitignore`가 `secrets.toml`을 올리지 않게 막습니다. 키를 코드 셀이나 공유 파일에 적지 않습니다.

**키 없이 저장본으로 진행**: 한글 준비 셀 하나(P02 또는 P03) → P07 → C06 순서로 실행합니다. **C01–C05와 C11은 건너뛰고**, C06 뒤의 C07–C10과 검산 셀·직접 해 보기로 이어 갑니다. C05가 오류로 멈췄을 때도 C06으로 돌아갑니다. C06은 `weather`가 아직 없을 때 `asos_2025_daily.csv`를 읽습니다. 저장본으로 처음부터 다시 확인하려면 커널을 다시 시작하고 이 순서를 따릅니다. C06의 첫 확인 출력은 `1460 행 · datetime64[ns]`입니다.

- 내 컴퓨터에서는 배포본의 `asos_2025_daily.csv`를 `ch12.ipynb`와 같은 폴더에 그대로 둡니다.
- 코랩에서 GitHub 노트북을 열어도 CSV는 실행 환경에 함께 생기지 않습니다. 배포 ZIP에서 `asos_2025_daily.csv`를 꺼내 컴퓨터에 저장하고, 코랩의 코드 셀에서 아래를 실행해 그 파일을 선택합니다. 업로드가 끝난 다음 P07 → C06을 실행합니다. 새 실행 환경에 연결해 파일이 사라졌으면 다시 업로드합니다([Colab 파일 안내](https://colab.research.google.com/notebooks/io.ipynb)).

```python
from google.colab import files
files.upload()  # asos_2025_daily.csv 선택
```

`FileNotFoundError`가 나면 먼저 CSV의 파일명과 위치를 확인합니다. 저장본의 서울·부산·강릉·제주 2025년 자료로 12장의 차트와 연습을 이어 갈 수 있습니다.

웹에 배포하려면 책 13.4절대로 `app.py`의 글꼴 줄(`font.family`)을 글꼴 파일 등록 네 줄로 바꾸고, `NanumGothic.ttf`와 그 라이선스 전문 `OFL.txt`를 `ch11_app/`에 함께 둡니다.

## 버전

Python 3.14.6, NumPy 2.4.4, pandas 2.3.3, Matplotlib 3.10.9, Seaborn 0.13.2, Plotly 6.7.0, Streamlit 1.64.0, requests 2.33.1에서 확인했습니다. 버전이 다르면 출력이나 경고가 다를 수 있습니다(책 부록 B·D).

## 자료

12장의 기상 자료를 뺀 예제의 자료는 모두 교육용 가상 자료이고, 노트북의 셀이 직접 만듭니다. 12장 자료는 실제 관측입니다 — 자료: 기상청 ASOS 일자료(공공데이터포털, 2025년), 공공누리 제1유형(출처 표시).


## 정오표와 라이선스

오류를 발견하면 [정오표](ERRATA.md)를 먼저 확인하고 [Issues](https://github.com/donghyunlee-ai/book-python-visualization/issues)에 알려 주세요.

- 예제 코드: [MIT License](LICENSE)
- 나눔고딕: [SIL Open Font License 1.1](LICENSES/NanumGothic-OFL.txt). 이전 예제 이력에 포함된 글꼴의 고지문도 함께 제공합니다.
- 책 본문과 학습 지원 문서·PDF의 저작권은 저자에게 있습니다.
