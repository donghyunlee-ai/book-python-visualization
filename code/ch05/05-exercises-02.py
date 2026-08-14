# [코드 2] 사례 2 — bins 조작에 따른 히스토그램 착시와 진실 규명
# 1장 02절에서 확정한 표준 셋업 스니펫이 실행된 상태를 전제합니다.

# [코드 2] bins 조작에 따른 히스토그램 착시와 진실 규명
# 이 코드는 1장 02절의 표준 셋업 스니펫이 실행된 상태를 전제합니다.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 실전 더미 데이터 생성 (시드 고정)
np.random.seed(42)

# 두 개의 상이한 고객군: 40점 부근과 60점 부근에 집중됨
peak1 = np.random.normal(loc=40, scale=5, size=500)
peak2 = np.random.normal(loc=60, scale=5, size=500)
scores = np.concatenate([peak1, peak2])

df_nps = pd.DataFrame({'NPS': scores})

# 2. 1행 2열 서브플롯 생성: 착시 vs 진실 비교
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# [왼쪽] bins=5 (폭 20)로 뭉뚱그려 만든 종형 착시
# 40점과 60점의 두 봉우리가 40~60 구간으로 합쳐져 거대한 하나의 산을 만듭니다.
sns.histplot(
    data=df_nps, x='NPS', bins=5, binrange=(0, 100), 
    color='#666666', ax=axes[0]
)
axes[0].set_title("bins=5 (매끈한 종형 착시)", color='#D55E00', fontweight='bold', pad=15)

# [오른쪽] bins=30 (폭 약 3.3)으로 잘게 쪼개어 폭로된 진실
# 숨어있던 40점과 60점의 쌍봉이 뚜렷하게 분리되어 나타납니다.
sns.histplot(
    data=df_nps, x='NPS', bins=30, binrange=(0, 100), 
    color='#009E73', ax=axes[1]
)
axes[1].set_title("bins=30 (쌍봉 분포 진실)", color='#009E73', fontweight='bold', pad=15)

plt.tight_layout()
plt.show()
