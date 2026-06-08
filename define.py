import pandas as pd

def clean_pipeline(path):
    df = pd.read_csv(path)
    # 1) 자료형
    df['pressure'] = pd.to_numeric(df['pressure'], errors = 'coerce')
    df['time'] = pd.to_datetime(df['time'])
    # 2) 중복 / 3) 이상치
    df = df.drop_duplicates()
    Q1, Q3 = df['temp'].quantile([0.25, 0.75])
    IQR = Q3 - Q1
    df = df[(df['temp'] >= Q1 - 1.5 * IQR) & (df['temp'] <= Q3 + 1.5 * IQR)]
    # 4) 결측 대체 / 5) 표준화
    df['temp'] = df['temp'].fillna(df['temp'].median())
    df.to_csv('clean.csv', index = False)
    return df