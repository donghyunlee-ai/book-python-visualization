# [실전 코드 1] 박스 플롯 + 스트립 플롯 (이상치 폭로와 인셋 확대도)
# 1장 02절에서 확정한 표준 셋업 스니펫이 실행된 상태를 전제합니다.

# -----------------------------------------------------------------------------
# [실전 코드 1] 박스 플롯과 스트립 플롯의 결합 (이상치 폭로와 인셋 확대도)
# -----------------------------------------------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

# 1. 데이터 스펙 계약 적용: 부서당 20명, C부서에 3억(30,000만 원) 임원 1명 포함
np.random.seed(42)

dept_a = np.random.normal(5000, 400, 20)
dept_b = np.random.normal(5500, 450, 20)
dept_c = np.concatenate([np.random.normal(4800, 350, 19), [30000]])

df = pd.DataFrame({
    '부서': ['A부서'] * 20 + ['B부서'] * 20 + ['C부서'] * 20,
    '연봉': np.concatenate([dept_a, dept_b, dept_c])
})

# 2. 중앙값 내림차순 정렬 (서열 자동 도출: B > A > C)
order_list = df.groupby('부서')['연봉'].median().sort_values(ascending=False).index.tolist()

# 3. 색상 전략 (타깃 부서 C 강조, 나머지 회색)
custom_palette = {dept: '#E69F00' if dept == 'C부서' else '#666666' for dept in order_list}

# 이상치 마커 튜닝 (경고색 다이아몬드 확대)
outlier_props = dict(
    marker='D', 
    markerfacecolor='#D55E00', 
    markeredgecolor='white', 
    markersize=8
)

fig, ax = plt.subplots(figsize=(7, 6))

# 4. 메인 박스 플롯 & 스트립 플롯 (표본 수 노출)
sns.boxplot(
    data=df, x='부서', y='연봉', hue='부서', palette=custom_palette, 
    order=order_list, flierprops=outlier_props, legend=False, ax=ax
)
sns.stripplot(
    data=df, x='부서', y='연봉', color='#666666', alpha=0.4, 
    size=4, jitter=True, order=order_list, ax=ax
)

# 5. 결정적 단서 텍스트 주석
c_idx = order_list.index('C부서')
ax.annotate(
    "임원 1인\n부서 평균을 홀로 26% 끌어올림",
    xy=(c_idx, 30000),
    xytext=(c_idx - 1.5, 25000), # C부서가 우측 끝(x=2)이므로 텍스트를 좌측 빈 공간으로 배치
    arrowprops=dict(facecolor='#D55E00', shrink=0.05, width=1.5, headwidth=6),
    fontsize=10, color='#D55E00', fontweight='bold'
)

# 6. 인셋(inset) 확대도 추가: 거대한 이상치로 뭉개진 하단 상자들의 실제 서열 복원
# 부모 축 대비 [좌, 하, 폭, 높이] 비율 지정
axins = ax.inset_axes([0.05, 0.45, 0.35, 0.45])
sns.boxplot(
    data=df, x='부서', y='연봉', hue='부서', palette=custom_palette, 
    order=order_list, flierprops=outlier_props, legend=False, ax=axins
)
sns.stripplot(
    data=df, x='부서', y='연봉', color='#666666', alpha=0.4, 
    size=3, jitter=True, order=order_list, ax=axins
)

# 인셋 축 범위 제한 (4000~6500 구간) 및 포맷 정리
axins.set_ylim(4000, 6500)
axins.set_xlabel('')
axins.set_ylabel('')
axins.set_xticks([])
# 인셋 테두리를 결과색(#009E73)으로 표시하여 시각적 구별
for spine in axins.spines.values():
    spine.set_color('#009E73')
    spine.set_linewidth(1.5)

ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f"{int(x):,}"))
ax.set_title('부서별 연봉 분포 및 극단적 이상치 발견', pad=15, fontweight='bold')
ax.set_xlabel('')
ax.set_ylabel('연봉 (만원)')
sns.despine(ax=ax)

plt.tight_layout()
plt.show()
