# charts.py
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# 4장 05절 스타일 자산화: 네 차트가 공유하는 색약 안전 팔레트
PALETTE = ['#0072B2', '#E69F00', '#009E73', '#D55E00', '#666666']
# 엔티티별 고정 색상 배정
COLOR_MAP = {
    'B2B세일즈': PALETTE[4], '고객성공': PALETTE[4],
    '마케팅': PALETTE[4], '신사업TFT': PALETTE[1], '데이터인프라': PALETTE[4]
}
REGION_MAP = {'수도권': PALETTE[1], '비수도권': PALETTE[0]}

def fig_sales_line(df, x='날짜', y='매출', color=None):
    """좌상단: 시간에 따른 합계 흐름. color 열이 있으면 계열을 분리한다."""
    color = color if color in df.columns else None
    group_cols = [x] + ([color] if color else [])
    daily = df.groupby(group_cols, as_index=False)[y].sum()
    kwargs = {
        'color': color,
        'title': '일별 부서별 매출 추이' if color else '일별 총 매출 추이',
    }
    if color:
        kwargs['color_discrete_map'] = COLOR_MAP
    else:
        kwargs['color_discrete_sequence'] = [PALETTE[0]]
    fig = px.line(daily, x=x, y=y, **kwargs)
    fig.update_layout(margin=dict(l=0, r=0, t=40, b=0))
    return fig

def fig_dept_bar(df, x='부서', y='매출', highlight=None):
    """우상단: 부서별 매출 비교 (강조 1 + 회색 팔레트)"""
    dept_sales = df.groupby(x)[y].sum().reset_index().sort_values(y, ascending=False)
    categories = dept_sales[x].tolist()
    if highlight is None and categories:
        highlight = '신사업TFT' if '신사업TFT' in categories else categories[0]
    color_map = {category: PALETTE[1] if category == highlight else PALETTE[4]
                 for category in categories}
    fig = px.bar(dept_sales, x=x, y=y, title='부서별 매출 비교',
                 color=x, color_discrete_map=color_map)
    fig.update_layout(showlegend=False, margin=dict(l=0, r=0, t=40, b=0))
    return fig

def fig_ad_scatter(df, x='광고비', y='매출액', color=None, symbol=None, hover_name=None):
    """좌하단: 광고비 대비 매출액 관계 (호버 툴팁)"""
    color = color if color in df.columns else None
    symbol = symbol if symbol in df.columns else None
    hover_name = hover_name if hover_name in df.columns else None
    color_map = COLOR_MAP if color in {'담당부서', '부서'} else REGION_MAP if color == '지역' else None
    fig = px.scatter(
        df, x=x, y=y, color=color, symbol=symbol, hover_name=hover_name,
        title='광고비 대비 매출액 현황', color_discrete_map=color_map,
    )
    fig.update_layout(margin=dict(l=0, r=0, t=40, b=0))
    return fig

def fig_salary_box(df, x='부서', y='연봉', highlight='신사업TFT', title=None, unit='만원'):
    """우하단: 분포를 그리고 현재 필터에 남은 하나의 강조 범주만 주석한다."""
    fig, ax = plt.subplots(figsize=(6, 4))
    if df.empty:
        ax.text(0.5, 0.5, '표시할 데이터가 없습니다.', ha='center', va='center', transform=ax.transAxes)
        ax.set_axis_off()
        return fig

    categories = list(df[x].dropna().unique())
    palette = {category: PALETTE[1] if category == highlight else PALETTE[4]
               for category in categories}
    sns.boxplot(data=df, x=x, y=y, hue=x, palette=palette, ax=ax, legend=False)
    ax.set_title(title or f'{x}별 {y} 분포', fontsize=13)
    ax.spines[['top', 'right']].set_visible(False)
    ax.tick_params(axis='x', rotation=30, labelsize=10)

    if highlight in categories:
        values = df.loc[df[x] == highlight, y].dropna()
        if not values.empty:
            q1, q3 = values.quantile([0.25, 0.75])
            upper_fence = q3 + 1.5 * (q3 - q1)
            whisker_values = values[values <= upper_fence]
            upper_whisker = whisker_values.max() if not whisker_values.empty else q3
            outliers = values[values > upper_fence]
            if not outliers.empty:
                max_outlier = outliers.max()
                xpos = categories.index(highlight)
                ax.text(
                    0.03, 0.47,
                    f'{highlight}\n이상치 판정 상한 {upper_fence:,.0f}{unit}\n'
                    f'실제 수염 끝 {upper_whisker:,.0f}{unit}',
                    transform=ax.transAxes, color=PALETTE[2], fontsize=10,
                )
                span = max(float(values.max() - values.min()), 1.0)
                ax.annotate(
                    f'{highlight} 이상치\n{max_outlier:,.0f}{unit}',
                    xy=(xpos, max_outlier), xytext=(max(xpos - 0.8, 0), max_outlier - span * 0.22),
                    arrowprops=dict(facecolor=PALETTE[3], shrink=0.05),
                    color=PALETTE[3], fontweight='bold', fontsize=10,
                )

    fig.tight_layout()
    return fig
