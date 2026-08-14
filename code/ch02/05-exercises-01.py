import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 더미 데이터 생성
months = ['1월', '2월', '3월', '4월', '5월']
dept_a = [800, 850, 900, 880, 1000]   # 800 ~ 1000대
dept_b = [50, 60, 70, 80, 100]        # 50 ~ 100대
dept_c = [400, 380, 410, 400, 420]    # 400대
dept_d = [100, 200, 150, 300, 250]    # 100 ~ 300대

# [문제의 코드] 4개 부서 실적을 배치한 2x2 차트 초안
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(6, 4)) # 실행 결과를 관찰해 보십시오.

dept_data = [dept_a, dept_b, dept_c, dept_d]
dept_names = ['A부서', 'B부서', 'C부서', 'D부서']
colors = ['tab:blue', 'orange', 'green', 'red']

# zip과 ax.flatten()을 사용하여 중복 코드를 최소화합니다.
for ax_i, data, name, color in zip(ax.flatten(), dept_data, dept_names, colors):
    ax_i.plot(months, data, marker='o', color=color, label=name)
    ax_i.set_title(f'{name[0]} 부서 실적', fontsize=14, pad=15)
    ax_i.legend()

plt.show()
