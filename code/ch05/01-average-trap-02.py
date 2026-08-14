# [코드 2] 앤스컴의 콰르텟: 네 그룹의 평균·분산이 소수점까지 같다
# 1장 02절에서 확정한 표준 셋업 스니펫이 실행된 상태를 전제합니다.

import pandas as pd
import seaborn as sns

# 시본에 기본 내장된 '앤스컴의 콰르텟' 원본 데이터셋을 불러옵니다.
anscombe = sns.load_dataset("anscombe")

# 4개 그룹별로 x와 y의 평균 및 분산을 소수점 첫째 자리까지 도출합니다.
stats = anscombe.groupby("dataset").agg(
    x_mean=("x", "mean"),
    y_mean=("y", "mean"),
    x_var=("x", "var"),
    y_var=("y", "var")
).round(1)

print("--- 통계 요약표 ---")
print(stats)
