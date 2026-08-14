import matplotlib.pyplot as plt

months = ['1월', '2월', '3월', '4월', '5월']
sales = [100, 120, 250, 130, 150]

fig, ax = plt.subplots(figsize=(6, 4))

# ① 의미 없는 다색 제거: 3월만 주황색 강조, 나머지는 회색 보조
colors = ['#666666', '#666666', '#E69F00', '#666666', '#666666']
bars = ax.bar(months, sales, color=colors, width=0.6, zorder=2)

# ② 짧은 월 레이블은 회전하지 않고 수평으로 읽히게 둠
ax.set_ylabel('매출')
plt.setp(ax.get_xticklabels(), rotation=0)

# ③ 스스로 말하는 차트를 위한 화살표 주석 각인
ax.annotate('3월 최고값 250',
            xy=(2, 250),
            xytext=(2, 280),
            ha='center', color='#E69F00', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#E69F00',
                            connectionstyle='arc3,rad=-0.2'))

# ④ 단일 데이터 계열이므로 불필요한 범례를 만들지 않음

# ⑤ 상/우 테두리 제거 및 옅은 수평 점선 격자만 허용
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', linestyle='--', alpha=0.3, zorder=0)

# 텍스트 주석이 잘리지 않도록 Y축 상단 공간 확보
ax.set_ylim(0, 330)
ax.set_title("1~5월 매출 추이 (튜닝 완료)", fontweight='bold', pad=15)

plt.show()
