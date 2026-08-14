# [코드 4] AI가 먼저 뱉는 함정 막대 차트 (errorbar=None으로 형태 정보 파괴)
# 1장 02절에서 확정한 표준 셋업 스니펫이 실행된 상태를 전제합니다.

# --- [코드 1]·[코드 2]에서 이어받음 (단독 실행을 위한 재선언) ---
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

salary_A = np.array([500] * 10)
salary_B = np.array([4100] + [100] * 9)
# ----------------------------------------------------------------

# A부서와 B부서의 이질적인 원천 데이터를 통합합니다.
df_salary = pd.DataFrame({
    '부서': ['A부서'] * 10 + ['B부서'] * 10,
    '급여': list(salary_A) + list(salary_B)
})

# 기본 추정자(평균)로 요약하고, 변동성을 보여줄 오차 막대마저(errorbar=None) 
# 제거하여 데이터의 형태 정보를 파괴하는 관성 코드입니다.
sns.barplot(
    data=df_salary, 
    x='부서', 
    y='급여', 
    errorbar=None, 
    color='#0072B2'
)

plt.title("부서별 월평균 급여 (단일 요약이 낳은 착시)")
plt.show()
