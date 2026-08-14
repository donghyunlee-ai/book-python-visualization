# 02절의 표준 셋업(한글 폰트, 시본 테마 등)은 이미 첫 셀에서 실행되었다고 전제합니다.

# 1. 가상의 월별 매출 데이터 생성 (AI가 만들어준 상황을 가정합니다)
months = np.array(['10월', '11월', '12월', '1월', '2월'])
sales = np.array([120, 135, 250, 140, 110])

# --- AI가 작성해 준 초기 초안 코드 ---
plt.figure(dpi=100) # 해상도가 낮아 화면에서 흐릿하게 보일 수 있습니다.
plt.plot(months, sales, color='gray', linewidth=1.5)
plt.title('월별 매출액 추이', fontsize=10) # 제목 폰트가 너무 작아 답답해 보입니다.
plt.show()
