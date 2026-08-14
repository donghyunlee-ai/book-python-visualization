import platform
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 한글 폰트 및 시각화 환경을 설정합니다. (Mac 및 Windows 호환)
system_os = platform.system()
if system_os == 'Darwin':
    font_name = 'AppleGothic'
elif system_os == 'Windows':
    font_name = 'Malgun Gothic'
else:
    font_name = 'NanumGothic'

# Seaborn 테마(흰색 배경의 격자), 한글 폰트, 마이너스 부호 깨짐 방지, 고해상도(dpi=300) 설정
sns.set_theme(
    style='whitegrid', 
    rc={'font.family': font_name, 'axes.unicode_minus': False, 'figure.dpi': 300}
)

# 2. 분석에 활용할 가상의 월별 제품 매출 데이터를 생성합니다.
np.random.seed(42)
months = ['1월', '2월', '3월', '4월', '5월']
products = ['제품A', '제품B', '제품C']

data = {
    '월': np.tile(months, len(products)),
    '제품': np.repeat(products, len(months)),
    '매출': np.random.randint(100, 500, size=15)
}
df = pd.DataFrame(data)

# 3. 1행 3열의 도화지 구조를 만들고 반복문으로 일괄 시각화합니다.
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
fig.suptitle('제품별 월간 매출 추이 (자동화 예시)', fontsize=16, fontweight='bold')

for i, product in enumerate(products):
    subset = df[df['제품'] == product]
    
    # 각 축 영역(ax)에 막대 그래프를 차례대로 그립니다.
    sns.barplot(data=subset, x='월', y='매출', ax=axes[i], color='steelblue')
    
    # 개별 그래프의 제목과 Y축 범위를 0~600으로 완벽하게 통일합니다.
    axes[i].set_title(f'{product} 매출')
    axes[i].set_ylim(0, 600)

plt.tight_layout()
plt.show()
