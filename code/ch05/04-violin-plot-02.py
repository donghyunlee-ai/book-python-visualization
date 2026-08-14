# [코드 1] 박스 플롯 vs 바이올린 플롯 대비 및 친절한 주석 매너
# 1장 02절에서 확정한 표준 셋업 스니펫이 실행된 상태를 전제합니다.

# [코드 1] 박스 플롯 vs 바이올린 플롯 대비 및 친절한 주석 매너
# (1장 02절의 표준 셋업이 이미 실행되었다고 전제합니다)
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 스펙 계약: 시드 고정 및 N(30,10,500) + N(90,10,500) 병합
np.random.seed(42)
low_scores = np.random.normal(loc=30, scale=10, size=500)
high_scores = np.random.normal(loc=90, scale=10, size=500)
bimodal_data = np.concatenate([low_scores, high_scores])

df_bimodal = pd.DataFrame({'점수': bimodal_data, '그룹': '전체 학생'})

# 1행 2열 서브플롯: 같은 y축 범위(sharey=True)로 두 차트의 진실 규명 능력 비교
fig, axes = plt.subplots(1, 2, figsize=(10, 5), sharey=True)

# 1. 왼쪽: 30점부터 90점까지 거대한 상자 하나로 양극화를 숨긴 박스 플롯 (비교군)
sns.boxplot(
    data=df_bimodal, x='그룹', y='점수', 
    color='#0072B2', ax=axes[0]
)
axes[0].set_title("박스 플롯 (거짓 평온 유발)", color='#D55E00', fontweight='bold', pad=10)
axes[0].set_xlabel("")
axes[0].set_ylabel("수학 점수")

# 2. 오른쪽: 모래시계 형태로 양극화를 폭로한 바이올린 플롯 (결과색)
# cut=0: 유령 꼬리 제거, inner='box': 박스 요약 지표 보존
sns.violinplot(
    data=df_bimodal, x='그룹', y='점수', 
    inner='box', cut=0, color='#0072B2', ax=axes[1]
)
axes[1].set_title("바이올린 플롯 (양극화 폭로)", color='#009E73', fontweight='bold', pad=10)
axes[1].set_xlabel("")
axes[1].set_ylabel("")

# [실무 매너] 청중의 해독을 돕는 가이드 텍스트 삽입
axes[1].text(
    0, 95, "[읽는 법] 폭이 넓을수록 그 구간에 사람이 많습니다.", 
    fontsize=10, color='#666666', ha='center',
    bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='#666666', alpha=0.9)
)

plt.suptitle("쌍봉형 데이터: 상자가 숨긴 진실을 곡선이 폭로하다", fontweight='bold', fontsize=14, y=1.05)
plt.tight_layout()
plt.show()
