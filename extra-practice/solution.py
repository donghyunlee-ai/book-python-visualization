"""선택 과제 풀이. 먼저 README.md의 질문을 풀고 실행합니다."""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd


def main():
    data = pd.read_csv(Path(__file__).with_name('visits.csv'))
    # 한 행 = 하루·한 분관. 이용 건수는 고유 이용자 수가 아닙니다.
    assert not data.isna().any().any()
    assert not data.duplicated(['day', 'site']).any()
    assert (data['open_hours'] > 0).all()
    assert (data['visits'] >= 0).all()
    summary = data.groupby('site')[['visits', 'open_hours']].sum()
    summary['visits_per_hour'] = summary['visits'] / summary['open_hours']
    print(summary.to_string())

    # 원표 검산: North = (60+80+70)/(6+8+7) = 10.0,
    # South = (36+48+30)/(3+4+5) = 9.5건/시간.
    assert summary.loc['North', 'visits_per_hour'] == 210 / 21 == 10
    assert summary.loc['South', 'visits_per_hour'] == 114 / 12 == 9.5
    daily = data.assign(rate=data['visits'] / data['open_hours'])
    simple_mean = daily.groupby('site')['rate'].mean()
    print('\nUnweighted mean of daily rates:')
    print(simple_mean.to_string())
    # South의 (12+12+6)/3 = 10은 시간 수가 다른 날에 같은 가중치를 줍니다.
    # 질문이 '하루의 비율을 똑같이 평균하면?'이었다면 별도의 집계입니다.
    assert simple_mean.loc['North'] == simple_mean.loc['South'] == 10

    fig, ax = plt.subplots(figsize=(6, 3.6))
    bars = ax.bar(summary.index, summary['visits_per_hour'],
                  color=['#0072B2', '#D55E00'], edgecolor='black', linewidth=0)
    bars[1].set_hatch('//')
    ax.bar_label(bars, fmt='%.1f', padding=4)
    ax.set(title='Visits per open hour over three days', xlabel='Site',
           ylabel='Visits per open hour', ylim=(0, 12))
    fig.tight_layout(rect=(0, 0.08, 1, 1))
    fig.text(0.02, 0.01, 'Source: fictional teaching data (6 daily site records)',
             fontsize=9)
    fig.savefig('transfer_output.png', dpi=150, bbox_inches='tight')
    plt.close(fig)
    print('\n관찰: 개방 1시간당 이용 건수는 North 10.0건, South 9.5건입니다.')
    print('한계: 사흘의 가상 자료이며 이용자의 구성과 방문 목적을 모릅니다.')
    print('이 차이만으로 분관의 운영 성과나 차이가 생긴 원인을 단정하지 않습니다.')


if __name__ == '__main__':
    main()
