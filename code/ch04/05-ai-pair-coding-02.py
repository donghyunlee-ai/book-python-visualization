import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 재사용 가능한 커스텀 스타일 함수 정의
def apply_custom_style(ax, title=""):
    """
    matplotlib Axes 객체를 받아 4장에서 배운 세련된 스타일을 일괄 적용합니다.
    """
    # 불필요한 테두리 지우기 (상/우)
    sns.despine(ax=ax, top=True, right=True, left=False, bottom=False)
    
    # Y축 가로 방향으로만 옅은 점선 격자 추가
    ax.grid(axis='y', color='#ced4da', linestyle='--', alpha=0.5)
    ax.grid(axis='x', visible=False)
    
    # 눈금선(Tick) 정리: X축은 짧게, Y축은 아예 보이지 않게
    ax.tick_params(axis='x', colors='#495057', length=4)
    ax.tick_params(axis='y', colors='#495057', length=0)
    
    # Y축 숫자에 천 단위 콤마 포맷터 적용
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: f'{int(x):,}'))
    
    # 모던한 좌측 정렬 타이틀 배치
    if title:
        ax.set_title(title, fontsize=14, fontweight='bold', loc='left', pad=15)
        
    return ax

# 2. 임의의 데이터 생성 및 차트 뼈대 그리기
# (2절의 표준 셋업이 완료되어 한글 폰트가 적용된 상태를 전제합니다)
np.random.seed(42)
days = pd.date_range('2026-10-01', periods=10)
visitors = np.random.randint(5000, 15000, size=10)

fig, ax = plt.subplots(figsize=(8, 4))
# 기본 파랑(#0072B2)으로 선 그래프 생성
ax.plot(days, visitors, color='#0072B2', marker='o', linewidth=2.5)

# X축 날짜 텍스트 겹침 방지 (45도 회전)
plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

# 3. 단 한 줄로 마스터 커스텀 스타일 적용
apply_custom_style(ax, title="최근 10일간 웹사이트 방문자 수 추이")

plt.tight_layout()
plt.show()
