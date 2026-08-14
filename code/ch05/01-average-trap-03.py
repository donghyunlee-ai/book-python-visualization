# [코드 3] 앤스컴의 콰르텟: 통계는 같지만 형태는 전혀 다르다 (lmplot 4패널)
# 1장 02절에서 확정한 표준 셋업 스니펫이 실행된 상태를 전제합니다.

# --- [코드 2]에서 이어받음 (단독 실행을 위한 재선언) ---
import seaborn as sns
anscombe = sns.load_dataset("anscombe")
# --------------------------------------------------------

import matplotlib.pyplot as plt

# 시본의 lmplot은 지정한 조건(col)에 맞춰 여러 패널을 자동으로 분할해 줍니다.
# 4개 그룹의 데이터를 분리된 4개의 패널로 나누어 산점도와 추세선으로 그립니다.
g = sns.lmplot(
    data=anscombe, 
    x="x", 
    y="y", 
    col="dataset",     # 4개의 데이터셋을 별도의 독립된 패널로 분리
    col_wrap=2,        # 가로로 2개의 패널을 배치하여 2행 2열 구조 생성
    height=3
)

g.figure.suptitle(
    "앤스컴의 콰르텟: 통계는 완벽히 같지만 형태는 완전히 다른 4개의 생태계", 
    y=1.05, 
    fontweight="bold"
)

plt.show()
