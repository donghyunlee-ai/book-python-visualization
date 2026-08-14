# 1행 2열의 축 영역을 담은 도화지를 생성합니다. (가로로 넓게 설정합니다.)
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

# 첫 번째 축 영역 (ax[0])에 막대 그래프를 그립니다.
ax[0].bar(['A', 'B', 'C'], [10, 25, 15], color='#0072B2')
ax[0].set_title('왼쪽 차트 (ax[0])')
ax[0].set_xlabel('카테고리')
ax[0].set_ylabel('값 1')

# 두 번째 축 영역 (ax[1])에 선 그래프를 그립니다.
ax[1].plot(['A', 'B', 'C'], [30, 10, 20], marker='^', color='#E69F00', linewidth=2)
ax[1].set_title('오른쪽 차트 (ax[1])')
ax[1].set_xlabel('카테고리')
ax[1].set_ylabel('값 2')

plt.tight_layout()
plt.show()
