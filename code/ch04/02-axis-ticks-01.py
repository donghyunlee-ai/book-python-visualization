import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates

# 1. 가상 데이터 생성 (180일 치 일별 누적 매출 데이터)
np.random.seed(42)
dates = pd.date_range(start='2026-01-01', periods=180)
sales = np.random.randint(100000, 500000, size=180).cumsum()
df = pd.DataFrame({'Date': dates, 'Sales': sales})

# 2. 기본 선 그래프 뼈대 생성 (선 그래프 표준 figsize (6,4) 준수)
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(df['Date'], df['Sales'], color='#0072B2', linewidth=2.0)

# --- [축 튜닝 핵심 델타 영역] ---

# [튜닝 1] 눈금 솎아내기 (Locator): 날짜 전용 mdates.MonthLocator()로 복잡한 일별 데이터를 월 단위 눈금으로 깔끔하게 솎아냄
ax.xaxis.set_major_locator(mdates.MonthLocator())

# [튜닝 2] 라벨 회전과 정렬 (Rotation & ha): 글씨 충돌을 피하기 위해 45도 회전 및 글자 오른쪽 끝단을 눈금 닻에 정확히 정렬
plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

# [튜닝 3] 숫자 포매터 (Formatter): 0이 끝없이 이어지는 매출 금액 수치를 10,000으로 나누어 축약하고 '만 원' 단위를 명시적으로 추가
formatter = ticker.FuncFormatter(lambda x, pos: f'{x/10000:,.0f}만 원')
ax.yaxis.set_major_formatter(formatter)

# [튜닝 4] 축 범위 지정 (Limit): 누적 데이터 추세의 정직하고 안정적인 부각을 위해 Y축 하한을 반드시 0으로 고정
ax.set_ylim(bottom=0)

# -----------------------------------

ax.set_title("상반기 누적 매출 추이 (축 눈금 튜닝 후)", fontsize=15, pad=15)
plt.show()
