# [실습 2] bins의 함정: 동일한 쌍봉 데이터에 bins만 5/30/100으로 바꾼 3패널 비교
# 1장 02절에서 확정한 표준 셋업 스니펫이 실행된 상태를 전제합니다.

# --- [실습 1]에서 이어받음 (단독 실행을 위한 재선언) ---
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
group_a = np.random.normal(30, 5, 500)
group_b_short = np.random.normal(24, 3, 250)
group_b_long = np.random.normal(36, 3, 250)
group_b = np.concatenate([group_b_short, group_b_long])
df = pd.DataFrame({
    '그룹': ['A'] * 500 + ['B'] * 500,
    '체류시간': np.concatenate([group_a, group_b])
})
# ------------------------------------------------------

# 완전히 동일한 B안 쌍봉형 데이터에 bins 값만 다르게 조작하여 1행 3열로 비교합니다.
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
bins_list = [5, 30, 100]

# 양극화가 뚜렷한 B그룹 데이터만 필터링
bimodal_data = df[df['그룹'] == 'B']['체류시간']

for ax, b in zip(axes, bins_list):
    sns.histplot(
        x=bimodal_data, bins=b, binrange=(0, 60), 
        color='#0072B2', ax=ax
    )
    ax.set_title(f"bins={b}")
    ax.set_xlabel("체류시간 (초)")
    ax.set_ylabel("빈도수 (명)")

plt.tight_layout()
plt.show()
