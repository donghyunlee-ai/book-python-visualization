import matplotlib.pyplot as plt

months = ['1월', '2월', '3월', '4월', '5월']
sales = [100, 120, 250, 130, 150]

fig, ax = plt.subplots(figsize=(6, 4))

# AI가 자동 생성한 튜닝 코드
colors = ['red', 'blue', 'green', 'orange', 'purple']
ax.bar(months, sales, color=colors, label='월별 실적')

ax.grid(True, color='black', linestyle='-', linewidth=1.2)
ax.legend(loc='upper center')

ax.set_ylabel('매출')
plt.setp(ax.get_xticklabels(), rotation=90)

ax.set_title('1~5월 매출 추이')

plt.show()
