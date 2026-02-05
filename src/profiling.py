import pandas as pd

def get_basic_info(df):
    info = {
        "shape": df.shape,
        "dtypes": df.dtypes.to_dict(),
        "missing": df.isnull().sum().to_dict(),
        "duplicates": df.duplicated().sum(),
        "stats": df.describe(include='all').to_dict()
    }
    return info

def get_correlations(df):
    numeric_df = df.select_dtypes(include=['number'])
    if numeric_df.empty:
        return None
    return numeric_df.corr()

def detect_outliers(df, col):
    if col not in df.columns:
        return None
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    return outliers
