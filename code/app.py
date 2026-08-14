# app.py
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
from data import average_daily_total, load_data
from charts import fig_sales_line, fig_dept_bar, fig_ad_scatter, fig_salary_box

MIN_SAMPLES = 15

# ① 설정: 페이지 레이아웃을 확장하여 좌우 공간 확보 및 전역 폰트 주입
st.set_page_config(layout='wide', page_title='경영 통합 대시보드')

def setup_font():
    fm.fontManager.addfont('fonts/NanumGothic.ttf')
    sns.set_theme() # 테마 적용 후 폰트 설정
    plt.rcParams['font.family'] = fm.FontProperties(fname='fonts/NanumGothic.ttf').get_name()
    plt.rcParams['axes.unicode_minus'] = False

setup_font()

# ② 데이터 로드: 흩어져 있던 데이터를 묶고 메모리 캐싱 적용
df_sales, df_accounts, df_salary = load_data()

# ③ 위젯: 사용자의 선택을 받는 사이드바 UI 구성
with st.sidebar:
    st.header("필터 설정")
    depts = df_sales['부서'].unique()
    sel_depts = st.multiselect("부서 선택", options=depts, default=depts)
    sel_region = st.selectbox("지역 선택", options=['전체'] + list(df_accounts['지역'].unique()))
    
    # 03절 활용: 분석 기간을 동적으로 제어하는 슬라이더
    min_date = df_sales['날짜'].min().date()
    max_date = df_sales['날짜'].max().date()
    sel_dates = st.slider("기간 선택", min_value=min_date, max_value=max_date, value=(min_date, max_date))

# ④ 필터 적용 및 데이터 윤리적 차단 기제 발동
f_sales = df_sales[
    (df_sales['부서'].isin(sel_depts)) & 
    (df_sales['날짜'].dt.date >= sel_dates[0]) & 
    (df_sales['날짜'].dt.date <= sel_dates[1])
]
f_accounts = df_accounts[df_accounts['담당부서'].isin(sel_depts)]
f_salary = df_salary[df_salary['부서'].isin(sel_depts)]

if sel_region != '전체':
    f_accounts = f_accounts[f_accounts['지역'] == sel_region]

# 데이터 모수가 너무 적어질 경우 경고 메시지 출력 (실측: 부서 1개+지역 1개면 교차 최소 셀 13곳까지 축소)
st.caption(f"현재 데이터: 매출 {len(f_sales)}건 | 거래처 {len(f_accounts)}곳 | 직원 {len(f_salary)}명")
if len(f_accounts) < MIN_SAMPLES or len(f_salary) < MIN_SAMPLES:
    st.warning("경고: 필터링된 데이터 모수가 너무 적어 통계적 요약이 실제를 심각하게 왜곡할 수 있습니다.")

# ⑤ 배치: 결론은 위로, 근거는 아래로 전개
# 5-1. 상단 KPI 카드 (delta 자동 표시)
col1, col2, col3 = st.columns(3)
total_sales = f_sales['매출'].sum()
avg_sales = average_daily_total(f_sales)
all_avg_sales = average_daily_total(df_sales)
delta_avg = avg_sales - all_avg_sales
account_count = len(f_accounts)

col1.metric("총 매출 (선택 기간)", f"{total_sales:,.0f} 만원")
col2.metric("일평균 매출", f"{avg_sales:,.0f} 만원", f"{delta_avg:,.0f} 만원 (전체평균 대비)")
col3.metric("활성 거래처 수", f"{account_count} 개")

st.divider()

# 5-2. 2x2 차트 격자 전개
row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    st.plotly_chart(fig_sales_line(f_sales, color='부서'))
with row1_col2:
    st.plotly_chart(fig_dept_bar(f_sales))

row2_col1, row2_col2 = st.columns(2)
with row2_col1:
    st.plotly_chart(fig_ad_scatter(
        f_accounts, color='담당부서', symbol='지역', hover_name='거래처'
    ))
with row2_col2:
    fig_box = fig_salary_box(
        f_salary, title='부서별 연봉 분포 및 이상치 (단위: 만원)'
    )
    st.pyplot(fig_box)
    plt.close(fig_box) # 필수 방어: 재실행 시 백그라운드 도화지 누적으로 인한 서버 다운 방지
