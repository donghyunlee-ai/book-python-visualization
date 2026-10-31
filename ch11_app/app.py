# A01 | 앱 준비: 라이브러리·글꼴·페이지 설정과 자료 읽기를 둡니다.
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st

plt.rcParams['font.family'] = 'AppleGothic'   # Windows는 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
st.set_page_config(page_title='지점 실적 탐색', layout='wide')
branch_colors = {'A': '#0072B2', 'B': '#D55E00'}   # 지점 색(4장과 같음)
branch_dashes = {'A': 'solid', 'B': 'dash'}         # 지점 선 모양


@st.cache_data                      # 같은 입력이면 읽은 표를 다시 씀
def load_data():
    return pd.read_csv(Path(__file__).with_name('sales.csv'))


st.title('지점 실적 탐색')
st.caption('자료: 교육용 가상 자료(월 합계, 24행, 단위 백만원)')
try:
    data = load_data()
except FileNotFoundError:
    st.error('app.py와 같은 폴더에 sales.csv를 둡니다.')
    st.stop()
# A02 | 위젯과 필터: 고른 값으로 행을 골라 view를 만듭니다.
st.sidebar.header('조회 조건')
branches = st.sidebar.multiselect('지점', ['A', 'B'], default=['A', 'B'])
months = st.sidebar.slider('월 범위', 1, 12, (1, 12))
metric_label = st.sidebar.selectbox('지표', ['매출', '영업이익'])
metric = {'매출': 'sales', '영업이익': 'profit'}[metric_label]

view = data[data['branch'].isin(branches)
            & data['month'].between(months[0], months[1])]
if view.empty:                          # 집계하기 전에 확인
    st.warning('표시할 자료가 없습니다. 지점을 하나 이상 고릅니다.')
    st.stop()
# A03 | 지표와 차트: 카드·추이·합계 막대를 모두 같은 view로 만듭니다.
st.subheader(f"{months[0]}~{months[1]}월 {metric_label}: "
             f"{', '.join(branches)}지점")
c1, c2 = st.columns(2)
c1.metric(f'기간 {metric_label} 합계', f'{view[metric].sum():,}백만원')
c2.metric('관측 수', f'{len(view)}행')

trend = px.line(view, x='month', y=metric, color='branch', markers=True,
                line_dash='branch', line_dash_map=branch_dashes,
                color_discrete_map=branch_colors, title='월별 추이',
                labels={'month': '월', 'branch': '지점',
                        metric: f'{metric_label} (백만원)'})
trend.update_xaxes(dtick=1)
trend.update_yaxes(rangemode='tozero')          # Y축을 0부터

totals = view.groupby('branch', as_index=False)[metric].sum()
fig, ax = plt.subplots(figsize=(4, 3))
bars = ax.bar(totals['branch'], totals[metric],
              color=[branch_colors[b] for b in totals['branch']],
              hatch=['//' if b == 'B' else '' for b in totals['branch']])
ax.bar_label(bars, fmt='{:,.0f}', padding=3)     # 천 단위 쉼표
ax.set(title='기간 합계', xlabel='지점',
       ylabel=f'{metric_label} (백만원)',
       ylim=(0, totals[metric].max() * 1.2))    # 값 라벨 자리
ax.spines[['top', 'right']].set_visible(False)   # 위·오른쪽 테두리
# A04 | 배치와 내려받기: 두 차트를 나란히 놓고 표와 CSV를 붙입니다.
left, right = st.columns(2)
with left:
    st.plotly_chart(trend)
with right:
    st.pyplot(fig)
st.dataframe(view, hide_index=True)
csv = view.to_csv(index=False).encode('utf-8-sig')   # 엑셀용 BOM
st.download_button('현재 선택 CSV 저장', csv,
                   file_name='selected_sales.csv', mime='text/csv')
st.caption('선택에 따라 합계가 달라집니다. '
           '원인은 이 자료로 단정하지 않습니다.')
