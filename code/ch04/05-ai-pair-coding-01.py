# 노트북 최상단 셀에 한 번만 선언해두면 모든 도화지에 적용되는 스타일 자산 스니펫
import matplotlib.pyplot as plt

plt.rcParams.update({
    'axes.spines.top': False,      # 상단 테두리 제거
    'axes.spines.right': False,    # 우측 테두리 제거
    'axes.grid': True,             # 기본 격자 활성화
    'axes.grid.axis': 'y',         # Y축 가로 방향으로만 격자 적용
    'grid.linestyle': '--',        # 격자를 점선으로 부드럽게
    'grid.alpha': 0.5,             # 격자 투명도 설정
    'legend.frameon': False,       # 범례 박스 테두리 제거
    'font.size': 11                # 기본 폰트 크기 일괄 적용
})
