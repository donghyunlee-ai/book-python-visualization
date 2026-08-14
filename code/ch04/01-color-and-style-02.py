x = np.arange(1, 6)
fig, ax = plt.subplots(figsize=(6, 4))

# 과거 실적: 파랑 실선, 두껍게, 원형 마커로 확실한 데이터를 표현합니다.
ax.plot(x[:3], [10, 12, 15], 
        color='#0072B2', linestyle='-', linewidth=2.5, marker='o', label='확정 실적')

# 미래 예측치: 주황 파선, 빈 마커(배경과 같은 흰색)로 미확정 뉘앙스를 전달합니다.
ax.plot(x[2:], [15, 18, 22], 
        color='#E69F00', linestyle='--', linewidth=2.0, marker='o', 
        markerfacecolor='white', label='예측치')

ax.legend(frameon=False)
ax.set_title("선 스타일을 활용한 실적 및 예측치 구분", pad=15)
plt.show()
