import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1. 맷플롯립 기본 폰트를 '나눔바른고딕'으로 설정하여 한글 깨짐을 방지합니다.
plt.rc('font', family='NanumBarunGothic')

# 2. 축의 음수(-) 기호가 네모로 깨지지 않도록 유니코드 마이너스 사용을 해제합니다.
plt.rcParams['axes.unicode_minus'] = False

# 3. Seaborn 테마에 한글 폰트를 적용하고, 고해상도(dpi=300) 출력을 설정합니다.
sns.set_theme(style='whitegrid', rc={'font.family': 'NanumBarunGothic', 'figure.dpi': 300})

# 4. 데이터의 재현성을 확보하기 위해 난수 시드를 고정해 주십시오.
np.random.seed(42)
