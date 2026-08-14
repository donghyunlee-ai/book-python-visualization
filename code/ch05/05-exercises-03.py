# [코드 3] 사례 3 — 박스 플롯 오독 방지: 표본 수 명시와 실제 데이터 오버레이
# 1장 02절에서 확정한 표준 셋업 스니펫이 실행된 상태를 전제합니다.

# --- 앞선 코드에서 이어받음 (단독 실행을 위한 재선언) ---
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# ------------------------------------------------------

# [코드 3] 박스 플롯 오독 방지: 표본 수 명시와 실제 데이터 오버레이
# 데이터가 적은 B팀의 한계를 명확히 드러냅니다.

# 1. 가상 데이터 준비 (A팀 200명, B팀 8명)
np.random.seed(42)
df_size = pd.DataFrame({
    '팀': ['A팀'] * 200 + ['B팀'] * 8,
    '실적': np.concatenate([
        np.random.normal(loc=50, scale=10, size=200),
        np.random.normal(loc=50, scale=10, size=8)
    ])
})

fig, ax = plt.subplots(figsize=(6, 5))

# 2. 박스 플롯 위에 스트립 플롯 오버레이
# 파랑(#0072B2)과 회색(#666666) 대비를 활용해 B팀에 시선을 유도합니다.
sns.boxplot(
    data=df_size, x='팀', y='실적', 
    hue='팀', palette={'A팀': '#666666', 'B팀': '#0072B2'}, 
    legend=False, ax=ax
)

# 데이터 점을 흩뿌려 시각적인 개수 차이를 뼈저리게 느끼게 만듭니다.
sns.stripplot(
    data=df_size, x='팀', y='실적', 
    color='#666666', alpha=0.6, jitter=True, ax=ax
)

# 3. x축 레이블에 표본 수(n) 계산 및 명시
counts = df_size['팀'].value_counts()
labels = [f"A팀\n(n={counts['A팀']})", f"B팀\n(n={counts['B팀']})"]
ax.set_xticks(ax.get_xticks())
ax.set_xticklabels(labels)

ax.set_title("표본 수(n)를 명시하여 오독을 방지한 박스 플롯", fontweight='bold', pad=15)
plt.tight_layout()
plt.show()
