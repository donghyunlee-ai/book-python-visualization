import pandas as pd
import numpy as np

# 가상의 10개 부서 월별 판매량 데이터 생성
np.random.seed(42)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
departments = [f'Dept_{i}' for i in range(1, 11)]

data = []
for dept in departments:
    base_sales = np.random.randint(50, 100)
    sales = base_sales + np.cumsum(np.random.randn(6) * 10)
    for m, s in zip(months, sales):
        data.append({'Month': m, 'Department': dept, 'Sales': s})
df = pd.DataFrame(data)

# 표준 셋업 스니펫이 이미 실행된 상태를 전제합니다.
fig, ax = plt.subplots(figsize=(7, 4))

# 부서별로 강조 여부('Dept_3')에 따라 스타일 변수를 다르게 지정하는 리스트 컴프리헨션
colors = ['#0072B2' if dept == 'Dept_3' else '#666666' for dept in departments]
alphas = [0.9 if dept == 'Dept_3' else 0.3 for dept in departments]
linestyles = ['-' if dept == 'Dept_3' else '--' for dept in departments]
linewidths = [2.5 if dept == 'Dept_3' else 1.0 for dept in departments]

for dept, color, alpha, ls, lw in zip(departments, colors, alphas, linestyles, linewidths):
    dept_data = df[df['Department'] == dept]
    
    # 강조 계열에만 마커('o')를 추가하여 시각적 차별성을 극대화합니다.
    current_marker = 'o' if dept == 'Dept_3' else ''
    
    # 강조선이 다른 회색 선에 덮여 탁해지지 않도록 최상단으로 올립니다.
    current_zorder = 5 if dept == 'Dept_3' else 1
    
    ax.plot(
        dept_data['Month'], 
        dept_data['Sales'], 
        color=color, 
        linestyle=ls, 
        linewidth=lw,
        marker=current_marker,
        alpha=alpha,
        zorder=current_zorder,
        label=dept if dept == 'Dept_3' else None
    )

ax.set_title("조건부 강조 전략: 특정 부서(Dept_3) 실적 부각하기", pad=15)
ax.set_ylabel("Sales")
ax.legend(frameon=False)
plt.show()
