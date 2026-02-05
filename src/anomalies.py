from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies_iforest(df):
    numeric_df = df.select_dtypes(include=['number']).dropna()
    if numeric_df.empty:
        return None
    
    model = IsolationForest(contamination=0.05, random_state=42)
    numeric_df['Anomaly_Score'] = model.fit_predict(numeric_df)
    # -1 pour anomalie, 1 pour normal
    anomalies = numeric_df[numeric_df['Anomaly_Score'] == -1]
    return anomalies
