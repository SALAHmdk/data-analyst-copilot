import pandas as pd

def clean_dataset(df):
    # Supprimer les doublons
    df_cleaned = df.drop_duplicates()
    # Remplir les valeurs manquantes simples
    for col in df_cleaned.columns:
        if df_cleaned[col].dtype == 'object':
            df_cleaned[col] = df_cleaned[col].fillna('Inconnu')
        else:
            df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].median() if not df_cleaned[col].empty else 0)
    return df_cleaned
