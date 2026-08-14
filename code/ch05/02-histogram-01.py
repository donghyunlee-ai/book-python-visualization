# [실습 1] 실습 데이터 셋업 + B안 전체 체류 시간 분포 스캔 (bins=30, kde)
# 1장 02절에서 확정한 표준 셋업 스니펫이 실행된 상태를 전제합니다.

# [1장 02-hello-colab에서 확정한 표준 셋업이 실행된 상태를 전제합니다]
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 실측치와 형태의 완벽한 재현을 위해 시드를 엄격하게 고정합니다.
np.random.seed(42)

# 가상의 A/B 테스트 체류 시간 (측정 창: 0~60초 제한)
# A안: 평균 30초, 표준편차 5로 예측 가능하게 몰린 단봉 분포 (500명)
group_a = np.random.normal(30, 5, 500)

# B안: 24초(단기 이탈)와 36초(몰입)로 양극화된 뚜렷한 쌍봉 분포 (총 500명)
group_b_short = np.random.normal(24, 3, 250)
group_b_long = np.random.normal(36, 3, 250)
group_b = np.concatenate([group_b_short, group_b_long])

# 시각화 최적화 롱폼(Long-form) 데이터프레임 조립
df = pd.DataFrame({
    '그룹': ['A'] * 500 + ['B'] * 500,
    '체류시간': np.concatenate([group_a, group_b])
})

# B안 전체 지형의 기본적인 히스토그램을 넓게 펼쳐 스캔합니다.
fig, ax = plt.subplots(figsize=(6, 4))
sns.histplot(
    data=df[df['그룹'] == 'B'], 
    x='체류시간', 
    bins=30,               # 구간을 30개로 나눔
    binrange=(0, 60),      # 공정한 척도를 위해 측정 창을 0~60초로 고정
    kde=True,              # 뼈대를 매끄럽게 훑는 밀도 추정 곡선 추가
    color='#0072B2'
)
ax.set_title("B안 전체 체류 시간 분포")
ax.set_xlabel("체류시간 (초)")
ax.set_ylabel("빈도수 (명)")
plt.show()
