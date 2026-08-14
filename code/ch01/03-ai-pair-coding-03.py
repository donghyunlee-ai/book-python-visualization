# --- 내 손으로 직접 튜닝(Fine-tuning)한 코드 ---
# 가로세로 비율(figsize)을 명확히 하고, 출판 및 보고용 고해상도(dpi=300)로 변경합니다.
plt.figure(figsize=(8, 4), dpi=300) 

# 선을 두껍게(linewidth=3.0) 만들고 점 마커(marker='o')를 추가하여 데이터의 흐름을 명확히 합니다.
plt.plot(months, sales, color='dimgray', linewidth=3.0, marker='o', markersize=8)

# 가장 중요한 12월 데이터(인덱스 2)만 빨간색 별표로 크게 강조하여 시선을 집중시킵니다!
plt.plot(months[2], sales[2], color='crimson', marker='*', markersize=15)

# 제목을 크고 굵게 변경하며, 여백(pad)을 주어 시각적인 답답함을 해소합니다.
plt.title('월별 매출액 추이 (12월 최고치 경신)', fontsize=16, fontweight='bold', pad=15)

# 튜닝이 완료된 최종 그래프를 화면에 출력합니다.
plt.show()
