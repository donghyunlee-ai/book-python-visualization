# 2행 2열의 다중 도화지를 생성합니다.
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

# 1. 좌상단 (0행 0열): 선 그래프
ax[0, 0].plot([1, 2, 3], color='#0072B2', linewidth=2, marker='o')
ax[0, 0].set_title('1번: ax[0, 0]', weight='bold')
ax[0, 0].set_xlabel('X축')
ax[0, 0].set_ylabel('Y축')

# 2. 우상단 (0행 1열): 산점도
ax[0, 1].scatter([1, 2, 3], [3, 2, 1], color='#E69F00', s=80)
ax[0, 1].set_title('2번: ax[0, 1]', weight='bold')
ax[0, 1].set_xlabel('X축')
ax[0, 1].set_ylabel('Y축')

# 3. 좌하단 (1행 0열): 막대 그래프
ax[1, 0].bar(['A', 'B'], [10, 20], color='#009E73', width=0.5)
ax[1, 0].set_title('3번: ax[1, 0]', weight='bold')
ax[1, 0].set_xlabel('카테고리')
ax[1, 0].set_ylabel('값')

# 4. 우하단 (1행 1열): 축을 숨기고 텍스트 표시
ax[1, 1].text(0.5, 0.5, '빈 공간\n(핵심 인사이트 요약)', fontsize=15, ha='center', va='center')
ax[1, 1].set_title('4번: ax[1, 1]', weight='bold')
ax[1, 1].axis('off')

plt.tight_layout()
plt.show()
