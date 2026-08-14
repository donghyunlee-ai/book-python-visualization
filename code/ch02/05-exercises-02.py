# [해결된 코드] 스케일을 공유하고 레이아웃을 최적화한 2x2 차트

import matplotlib.pyplot as plt

# 이 파일만 실행해도 동작하도록 문제와 같은 데이터를 함께 선언합니다.
months = ['1월', '2월', '3월', '4월', '5월']
dept_a = [800, 850, 900, 880, 1000]
dept_b = [50, 60, 70, 80, 100]
dept_c = [400, 380, 410, 400, 420]
dept_d = [100, 200, 150, 300, 250]

# 1. figsize를 (10, 6)으로 넉넉하게 키웁니다.
# 2. sharey=True 옵션으로 4개 축 영역(Axes)의 Y축 스케일을 하나로 통일합니다.
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 6), sharey=True)

dept_data = [dept_a, dept_b, dept_c, dept_d]
dept_names = ['A부서', 'B부서', 'C부서', 'D부서']
colors = ['tab:blue', 'orange', 'green', 'red']

# 데이터 그리기: zip과 ax.flatten()을 사용하여 우아하게 리팩터링합니다.
for ax_i, data, name, color in zip(ax.flatten(), dept_data, dept_names, colors):
    ax_i.plot(months, data, marker='o', color=color, label=name)
    ax_i.set_title(f'{name[0]} 부서 실적', fontsize=14, pad=15)
    
    # 시각화 기본 규칙 준수를 위해 축 라벨을 추가합니다.
    ax_i.set_xlabel('월', fontsize=10)
    ax_i.set_ylabel('실적(대)', fontsize=10)
    
    # 도화지가 넓어졌으므로 범례가 선을 덜 가리게 됩니다.
    ax_i.legend(loc='upper left')

# 3. 마법의 한 줄로 겹치는 글씨와 여백 문제를 한 번에 해결합니다!
fig.tight_layout()
plt.show()
