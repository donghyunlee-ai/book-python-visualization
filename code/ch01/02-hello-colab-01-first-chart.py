import matplotlib.pyplot as plt

# 1. 시각화에 사용할 간단한 리스트 데이터를 준비합니다.
x_data = [1, 2, 3, 4, 5]
y_data = [2, 5, 3, 7, 4]

# 2. 선 그래프를 위한 도화지(Figure) 객체를 생성합니다.
plt.figure()

# 준비된 도화지 위에 선 그래프(Plot)를 그립니다.
plt.plot(x_data, y_data)

# 3. 완성된 그래프를 화면에 출력합니다.
plt.show()
