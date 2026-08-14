# data.py
import pandas as pd
import numpy as np
import streamlit as st


def average_daily_total(df, x='날짜', y='매출'):
    """일별 합계를 먼저 구한 뒤 하루 평균을 반환한다."""
    if df.empty:
        return 0.0
    return float(df.groupby(x)[y].sum().mean())

@st.cache_data
def load_data():
    """1~5장의 흩어진 실습 데이터를 '5개 부서' 공통 축으로 엮는 통합 데이터 계약"""
    np.random.seed(42)
    DEPTS = ['마케팅', 'B2B세일즈', '데이터인프라', '고객성공', '신사업TFT']
    LEVEL = {'마케팅': 45, 'B2B세일즈': 82, '데이터인프라': 21, '고객성공': 58, '신사업TFT': 31}

    # ① df_sales — 일별·부서별 매출 (100일 x 5부서 = 500행)
    dates = pd.date_range('2026-01-01', periods=100)
    frames = []
    for d in DEPTS:
        lv = LEVEL[d]
        trend = np.cumsum(np.random.normal(lv * 0.004, lv * 0.03, 100))
        noise = np.random.normal(0, lv * 0.12, 100)
        frames.append(pd.DataFrame({'날짜': dates, '부서': d, '매출': lv + trend + noise}))
    df_sales = pd.concat(frames, ignore_index=True)

    # ② df_accounts — 거래처 200곳
    ad = np.random.uniform(100, 500, 200)
    df_accounts = pd.DataFrame({
        '거래처': [f'{i+1}호점' for i in range(200)],
        '광고비': ad,
        '매출액': ad * 1.5 + np.random.normal(0, 100, 200) + 200,
        '지역': np.random.choice(['수도권', '비수도권'], 200, p=[0.6, 0.4]),
        '담당부서': np.random.choice(DEPTS, 200),
    })

    # ③ df_salary — 직원 100명 (부서당 20명)
    MEAN = {'마케팅': 4900, 'B2B세일즈': 5500, '데이터인프라': 5200, '고객성공': 5000, '신사업TFT': 4800}
    SD   = {'마케팅': 400,  'B2B세일즈': 450,  '데이터인프라': 420,  '고객성공': 400,  '신사업TFT': 350}
    srows = []
    for d in DEPTS:
        if d == '신사업TFT':   # 임원 1명 연봉 3억(30,000만원)
            vals = np.concatenate([np.random.normal(MEAN[d], SD[d], 19), [30000]])
        else:
            vals = np.random.normal(MEAN[d], SD[d], 20)
        srows.append(pd.DataFrame({'부서': d, '연봉': vals}))
    df_salary = pd.concat(srows, ignore_index=True)
    return df_sales, df_accounts, df_salary
