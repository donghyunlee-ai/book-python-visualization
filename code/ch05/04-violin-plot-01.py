# [코드 2] 표본 크기에 따른 규모 착시와 density_norm 튜닝 (원고 등장 순서상 첫 코드)
# 1장 02절에서 확정한 표준 셋업 스니펫이 실행된 상태를 전제합니다.

# [코드 2] 표본 크기에 따른 착시와 density_norm 튜닝
# (1장 02절의 표준 셋업이 이미 실행되었다고 전제합니다)
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)

# 표본 수가 극단적으로 차이 나는 두 그룹 생성 (분포 형태는 동일한 N(50,10))
group_large = np.random.normal(loc=50, scale=10, size=300)
group_small = np.random.normal(loc=50, scale=10, size=8)

df_size_trap = pd.DataFrame({
    '점수': np.concatenate([group_large, group_small]),
    '그룹': ['대그룹 (n=300)'] * 300 + ['소그룹 (n=8)'] * 8
})

# 1행 2열 서브플롯: y축을 통일(sharey=True)하여 공정 비교
fig, axes = plt.subplots(1, 2, figsize=(10, 5), sharey=True)

# 1. 왼쪽: 기본값 (density_norm='area') - 8명과 300명이 대등한 덩치를 갖는 규모 착시 (경고색)
sns.violinplot(
    data=df_size_trap, x='그룹', y='점수', 
    inner='box', cut=0, density_norm='area', color='#D55E00', ax=axes[0]
)
axes[0].set_title("기본값: 두 그룹 덩치가 같아 보이는 착시", color='#D55E00', fontweight='bold', pad=10)
axes[0].set_xlabel("")
axes[0].set_ylabel("점수")

# 2. 오른쪽: 튜닝 (density_norm='count') - 실제 표본 수에 비례하여 8명 그룹이 쪼그라듦 (결과색)
sns.violinplot(
    data=df_size_trap, x='그룹', y='점수', 
    inner='box', cut=0, density_norm='count', color='#009E73', ax=axes[1]
)
axes[1].set_title("튜닝: 실제 표본 수에 비례한 폭 (count)", color='#009E73', fontweight='bold', pad=10)
axes[1].set_xlabel("")
axes[1].set_ylabel("")

plt.tight_layout()
plt.show()
