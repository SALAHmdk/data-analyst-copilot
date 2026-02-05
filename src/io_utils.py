import pandas as pd
import io

import json
import requests

def load_data(uploaded_file):
    if uploaded_file is not None:
        name = uploaded_file.name.lower()
        if name.endswith('.csv'):
            return pd.read_csv(uploaded_file)
        elif name.endswith(('.xlsx', '.xls')):
            return pd.read_excel(uploaded_file)
        elif name.endswith('.json'):
            return pd.read_json(uploaded_file)
        elif name.endswith('.parquet'):
            return pd.read_parquet(uploaded_file)
        elif name.endswith('.txt'):
            return parse_pasted_data(uploaded_file.read().decode('utf-8'))
    return None

def fetch_api_data(url, params=None, headers=None):
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        # Flatten if it's a nested JSON
        if isinstance(data, list):
            return pd.DataFrame(data)
        elif isinstance(data, dict):
            # Try to find the list in common keys
            for key in ['data', 'results', 'items']:
                if key in data and isinstance(data[key], list):
                    return pd.DataFrame(data[key])
            return pd.json_normalize(data)
    except Exception as e:
        return str(e)
    return None

def parse_pasted_data(text):
    if not text:
        return None
    # Try different separators
    for sep in [',', ';', '\t']:
        try:
            df = pd.read_csv(io.StringIO(text), sep=sep)
            if df.shape[1] > 1:
                return df
        except:
            continue
    return pd.read_csv(io.StringIO(text))

def detect_columns(df):
    cols = {
        'num': df.select_dtypes(include=['number']).columns.tolist(),
        'date': df.select_dtypes(include=['datetime', 'datetimetz']).columns.tolist(),
        'cat': df.select_dtypes(include=['object', 'category']).columns.tolist()
    }
    # Try to convert objects to dates
    for col in cols['cat']:
        try:
            pd.to_datetime(df[col], errors='raise')
            cols['date'].append(col)
        except:
            continue
    return cols
