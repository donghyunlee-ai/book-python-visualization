import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import platform

# 재현성을 위한 시드 고정 및 시본(Seaborn) 기본 테마를 설정합니다.
np.random.seed(42)
sns.set_theme(style='whitegrid')

# 운영체제에 맞게 한글 폰트를 설정합니다.
if platform.system() == 'Darwin':
    plt.rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
else:
    plt.rc('font', family='NanumGothic')

# 마이너스 기호가 깨지는 현상을 방지합니다.
plt.rcParams['axes.unicode_minus'] = False

# 1. 가상의 월별 매출 데이터 생성 (AI가 만들어준 상황을 가정합니다)
months = np.array(['10월', '11월', '12월', '1월', '2월'])
sales = np.array([120, 135, 250, 140, 110])

# --- AI가 작성해 준 초기 초안 코드 ---
plt.figure(dpi=100) # 해상도가 낮아 화면에서 흐릿하게 보일 수 있습니다.
plt.plot(months, sales, color='gray', linewidth=1.5)
plt.title('월별 매출액 추이', fontsize=10) # 제목 폰트가 너무 작아 답답해 보입니다.
plt.show()
