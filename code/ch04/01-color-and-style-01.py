# 표준 셋업 스니펫이 이미 실행된 상태를 전제합니다.
fig, ax = plt.subplots(figsize=(6, 4))

# 헥스 코드를 사용하여 정밀하게 색상을 지정하고 차트를 그립니다.
ax.plot([1, 2, 3], [10, 15, 13], color='#D55E00', linewidth=2, marker='o') # 주황빨강
ax.bar([1, 2, 3], [5, 10, 8], color='#0072B2', width=0.4)                  # 파랑

ax.set_title("헥스 코드를 활용한 색상 지정", pad=15)
plt.show()
