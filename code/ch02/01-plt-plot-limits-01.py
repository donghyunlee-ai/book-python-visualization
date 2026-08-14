# [코드 설명] 하위 그래프 위치 지정을 누락하여 서로 다른 스케일의 두 데이터가 하나의 축에 겹쳐 그려지는 상태 기반 방식의 꼬임 사례입니다.
# [코드 결과] 매출 데이터의 큰 스케일에 밀려 영업이익 추세선이 바닥에 납작하게 눌리고, 제목의 대상마저 불분명해진 혼란스러운 차트가 출력됩니다.

import matplotlib.pyplot as plt
import numpy as np

# (1장 02-hello-colab에서 확정한 폰트 및 테마 표준 셋업이 이미 실행되었다고 전제합니다.)

# 가상의 매출, 영업이익 데이터 생성 (1월~6월)
months = np.array(['1월', '2월', '3월', '4월', '5월', '6월'])
sales_data = np.array([100, 120, 150, 130, 160, 200])
profit_data = np.array([10, 15, 25, 20, 30, 50])

# 가로 8, 세로 4 인치의 새로운 도화지를 생성합니다.
plt.figure(figsize=(8, 4))

# 의도: 두 개의 선을 나란히 좌우로 그리고 싶습니다. (하지만 하위 그래프 위치 지정을 깜빡했습니다)
# 결과: 현재 활성화된 도화지에 첫 번째 선(매출)과 두 번째 선(영업이익)이 무분별하게 겹쳐서 그려집니다.
plt.plot(months, sales_data, color='#0072B2', linewidth=2, marker='o', label='매출')
plt.plot(months, profit_data, color='#D55E00', linewidth=2, marker='s', label='영업이익')

# 이렇게 설정하면 제목이 어느 선을 가리키는지, 전체를 가리키는지 통제하기 어렵습니다.
plt.title('상반기 실적', fontsize=14, pad=15)
plt.legend()

plt.tight_layout()
plt.show()
