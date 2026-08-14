# [코드 1] 사례 1 — 평균 막대의 거짓말과 분포 차트의 진실 (박스+점+인셋)
# 1장 02절에서 확정한 표준 셋업 스니펫이 실행된 상태를 전제합니다.

# [코드 1] 평균 막대의 거짓말과 분포 차트의 진실
# 이 코드는 1장 02절의 표준 셋업 스니펫이 실행된 상태를 전제합니다.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 실전 더미 데이터 생성 (시드 고정)
np.random.seed(42)

# A팀: 99명은 평균 300만 원(표준편차 50), 1명(팀장)은 2억 원(20,000만 원) 독식
a_team = np.random.normal(loc=300, scale=50, size=99).tolist() + [20000]
# B팀: 100명 전원이 평균 497만 원(표준편차 100)을 안정적으로 수령
b_team = np.random.normal(loc=497, scale=100, size=100).tolist()

df_bonus = pd.DataFrame({
    '팀': ['A팀'] * 100 + ['B팀'] * 100,
    '성과급(만원)': a_team + b_team
})

# 2. 1행 2열 서브플롯 생성: 왜곡 vs 진실 비교
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# [왼쪽] 거짓말을 하는 평균 막대 그래프
# errorbar=None으로 오차막대마저 지워버리면, 완벽한 착시가 완성됩니다.
sns.barplot(
    data=df_bonus, x='팀', y='성과급(만원)', 
    errorbar=None, color='#666666', ax=axes[0]
)
axes[0].set_title("팀별 평균 성과급 (착시 유발)", color='#D55E00', fontweight='bold', pad=15)

# [오른쪽] 진실을 폭로하는 박스 플롯 + 스트립 플롯
# 팔레트: 강조할 A팀은 주황(#E69F00), 비교군 B팀은 회색(#666666)
sns.boxplot(
    data=df_bonus, x='팀', y='성과급(만원)', 
    hue='팀', palette={'A팀': '#E69F00', 'B팀': '#666666'}, legend=False,
    fliersize=0, width=0.5, ax=axes[1]
)

# 극단 이상치가 전체 상자를 뭉개므로, 상자의 실제 형태를 보여주는 확대도를 인셋으로 추가합니다.
axins = axes[1].inset_axes([0.5, 0.45, 0.45, 0.45])
sns.boxplot(
    data=df_bonus, x='팀', y='성과급(만원)', 
    hue='팀', palette={'A팀': '#E69F00', 'B팀': '#666666'}, legend=False,
    fliersize=0, width=0.5, ax=axins
)
sns.stripplot(
    data=df_bonus, x='팀', y='성과급(만원)', 
    color='#666666', alpha=0.5, size=4, jitter=True, ax=axins
)
axins.set_ylim(0, 1000)
axins.set_xlabel('')
axins.set_ylabel('')
axins.set_title('상자 확대 (0~1000만 원)', fontsize=10)
for spine in axins.spines.values():
    spine.set_edgecolor('#009E73')
    spine.set_linewidth(1.5)

# 스트립 플롯으로 모든 점을 흩뿌려 실제 산포도를 드러냅니다.
sns.stripplot(
    data=df_bonus, x='팀', y='성과급(만원)', 
    color='#666666', alpha=0.5, size=4, jitter=True, ax=axes[1]
)

# 이상치 하나만 붉은색(#D55E00) 마커로 덧칠해 강력히 경고합니다.
axes[1].plot(0, 20000, marker='o', color='#D55E00', markersize=8)

# 의사결정자를 위한 화살표 주석(Annotation) 추가
axes[1].annotate(
    "※ 팀장 1인의 극단적 성과급 독식\n(평균을 왜곡시킨 주범)",
    xy=(0, 20000), xytext=(0.5, 15000),
    arrowprops=dict(facecolor='#D55E00', shrink=0.05, width=2, headwidth=8),
    fontsize=11, color='#D55E00', fontweight='bold',
    horizontalalignment='center'
)
axes[1].set_title("팀별 성과급 실제 분포 (박스+점)", color='#009E73', fontweight='bold', pad=15)

plt.tight_layout()
plt.show()
