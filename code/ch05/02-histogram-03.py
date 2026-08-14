# [실습 3] 불균형 표본(A 500명 / B 200명): stat='count' 압살 vs stat='density' 공정 비교
# 1장 02절에서 확정한 표준 셋업 스니펫이 실행된 상태를 전제합니다.

# --- 앞선 실습에서 이어받음 (단독 실행을 위한 재선언) ---
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# ------------------------------------------------------

# stat='density' 정규화의 위력을 증명하기 위한 고의적인 불균형 표본 생성
# A안: 500명 전체 노출 단봉 / B안: 200명 부분 롤아웃 쌍봉
np.random.seed(42)
group_a_imb = np.random.normal(30, 5, 500)
group_b_imb = np.concatenate([
    np.random.normal(24, 3, 100),
    np.random.normal(36, 3, 100)
])

df_imb = pd.DataFrame({
    '그룹': ['A(n=500)'] * 500 + ['B(n=200)'] * 200,
    '체류시간': np.concatenate([group_a_imb, group_b_imb])
})

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# 왼쪽: stat='count' (인원수 덩치 차이가 그대로 반영되어 B그룹이 바닥에 뭉개짐)
sns.histplot(
    data=df_imb, x='체류시간', hue='그룹',
    bins=30, binrange=(0, 60), stat='count', alpha=0.5,
    palette=['#0072B2', '#E69F00'], ax=axes[0]
)
axes[0].set_title("stat='count' (인원수 압도)")
axes[0].set_xlabel("체류시간 (초)")
axes[0].set_ylabel("빈도수")

# 오른쪽: stat='density' (압도적 덩치 차이를 면적 정규화로 무효화) + step 윤곽선 결합
sns.histplot(
    data=df_imb, x='체류시간', hue='그룹',
    bins=30, binrange=(0, 60), stat='density', common_norm=False,
    element='step', fill=False, linewidth=2,
    palette=['#0072B2', '#E69F00'], ax=axes[1]
)
axes[1].set_title("stat='density' (형태 공정 비교)")
axes[1].set_xlabel("체류시간 (초)")
axes[1].set_ylabel("밀도 (Density)")

# 4장 스킬 회수: 범례를 차트 밖으로 빼내고 가로 격자를 은은하게 보조함
sns.move_legend(axes[1], "center left", bbox_to_anchor=(1, 0.5), title="집단")
for ax in axes:
    ax.grid(axis='y', alpha=0.3)
sns.despine(fig=fig)

plt.tight_layout()
plt.show()
