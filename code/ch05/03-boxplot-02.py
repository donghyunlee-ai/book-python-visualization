# [실전 코드 2] 똑같은 데이터, 정반대의 보고서: 평균 막대 vs 박스 플롯 1행 2열 대비
# 1장 02절에서 확정한 표준 셋업 스니펫이 실행된 상태를 전제합니다.

# --- [실전 코드 1]에서 이어받음 (단독 실행을 위한 재선언) ---
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

np.random.seed(42)
dept_a = np.random.normal(5000, 400, 20)
dept_b = np.random.normal(5500, 450, 20)
dept_c = np.concatenate([np.random.normal(4800, 350, 19), [30000]])
df = pd.DataFrame({
    '부서': ['A부서'] * 20 + ['B부서'] * 20 + ['C부서'] * 20,
    '연봉': np.concatenate([dept_a, dept_b, dept_c])
})
order_list = df.groupby('부서')['연봉'].median().sort_values(ascending=False).index.tolist()
custom_palette = {dept: '#E69F00' if dept == 'C부서' else '#666666' for dept in order_list}
outlier_props = dict(
    marker='D',
    markerfacecolor='#D55E00',
    markeredgecolor='white',
    markersize=8
)
# -----------------------------------------------------------

# -----------------------------------------------------------------------------
# [실전 코드 2] 똑같은 데이터, 정반대의 보고서: 평균 막대 vs 박스 플롯 1행 2열 대비
# -----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# --- 왼쪽: 단순 평균 막대 그래프 (거짓된 1등 착시) ---
# errorbar=None으로 지정해 단순 평균값 하나만 노출
sns.barplot(
    data=df, x='부서', y='연봉', hue='부서', palette=custom_palette, 
    order=order_list, errorbar=None, legend=False, ax=axes[0]
)
# 각 막대 위에 평균 수치 노출 (경영진의 착시를 굳히는 장치)
for i, dept in enumerate(order_list):
    mean_val = df[df['부서'] == dept]['연봉'].mean()
    axes[0].text(i, mean_val + 500, f"{round(mean_val):,}만", ha='center', fontweight='bold')

axes[0].set_title('A. 평균 연봉 비교 (C부서 1등 착시)', pad=15, fontweight='bold')
axes[0].set_ylabel('평균 연봉 (만원)')

# --- 오른쪽: 박스 플롯 + 스트립 플롯 + 인셋 (분포 진실 폭로) ---
sns.boxplot(
    data=df, x='부서', y='연봉', hue='부서', palette=custom_palette, 
    order=order_list, flierprops=outlier_props, legend=False, ax=axes[1]
)
sns.stripplot(
    data=df, x='부서', y='연봉', color='#666666', alpha=0.4, 
    size=3, jitter=True, order=order_list, ax=axes[1]
)

# 오른쪽 차트 내부 인셋 확대도 (상자 간의 실제 중앙값 격차 대조용)
# 부모 축 대비 [좌, 하, 폭, 높이] 비율 지정
axins2 = axes[1].inset_axes([0.05, 0.45, 0.35, 0.45])
sns.boxplot(
    data=df, x='부서', y='연봉', hue='부서', palette=custom_palette, 
    order=order_list, flierprops=outlier_props, legend=False, ax=axins2
)
sns.stripplot(
    data=df, x='부서', y='연봉', color='#666666', alpha=0.4, 
    size=3, jitter=True, order=order_list, ax=axins2
)
axins2.set_ylim(4000, 6500)
axins2.set_xlabel('')
axins2.set_ylabel('')
axins2.set_xticks([])
for spine in axins2.spines.values():
    spine.set_color('#009E73')
    spine.set_linewidth(1.5)

axes[1].set_title('B. 부서별 분포 (C부서 중앙값 꼴찌의 진실)', pad=15, fontweight='bold')
axes[1].set_ylabel('')

# 공통 포매팅 마감
for ax in axes:
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f"{int(x):,}"))
    ax.set_xlabel('')
    sns.despine(ax=ax)

plt.tight_layout()
plt.show()
