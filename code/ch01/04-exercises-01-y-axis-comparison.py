import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import platform

# 재현성을 위해 난수 시드를 고정합니다.
np.random.seed(42)

# 1. 한글 폰트 및 기본 스타일을 설정합니다. (고해상도 300dpi 유지)
if platform.system() == 'Darwin':
    font_family = 'AppleGothic'
else:
    font_family = 'Malgun Gothic'

plt.rcParams['font.family'] = font_family
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐을 방지합니다.
sns.set_theme(style='whitegrid', rc={'figure.dpi': 300, 'font.family': font_family})

# 2. 시각화에 사용할 영업이익 더미 데이터를 준비합니다.
years = ['2022년', '2023년']
profits = [100, 105]

# 3. 두 개의 그래프를 나란히 비교하기 위해 도화지를 분할합니다.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# [왼쪽 그래프] 나쁜 예: Y축 자동 절삭에 의한 과장된 모습입니다.
sns.barplot(x=years, y=profits, ax=ax1, color='lightcoral')
ax1.set_ylim(95, 110)  # 의도적으로 시작점을 95로 잘라내어 차이를 2배로 부풀립니다.
ax1.set_title('왜곡된 시각화 (Y축 95부터 시작)', fontweight='bold')

# [오른쪽 그래프] 좋은 예: Y축을 0부터 시작하여 정직하게 비교합니다.
sns.barplot(x=years, y=profits, ax=ax2, color='steelblue')
ax2.set_ylim(0, 120)  # Y축의 하한값을 0으로 강제 고정하여 진실성을 확보합니다.
ax2.set_title('올바른 시각화 (Y축 0부터 시작)', fontweight='bold')

# 4. 레이아웃이 겹치지 않게 조정한 뒤 화면에 출력합니다.
plt.tight_layout()
plt.show()
