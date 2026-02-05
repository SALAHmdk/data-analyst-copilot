import pandas as pd

def calculate_aggregates(df, group_col, val_col):
    return df.groupby(group_col)[val_col].agg(['sum', 'mean', 'count']).sort_values(by='sum', ascending=False)

def get_top_categories(df, cat_col, limit=10):
    return df[cat_col].value_counts().head(limit)

def analyze_trends(df, date_col, val_col, freq='M'):
    df[date_col] = pd.to_datetime(df[date_col])
    return df.set_index(date_col)[val_col].resample(freq).sum()
