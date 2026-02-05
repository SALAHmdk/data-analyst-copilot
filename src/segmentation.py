from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd

def perform_clustering(df, n_clusters=3):
    numeric_df = df.select_dtypes(include=['number']).dropna()
    if numeric_df.empty:
        return None, "Pas de données numériques pour le clustering."
    
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numeric_df)
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(scaled_data)
    
    result_df = numeric_df.copy()
    result_df['Cluster'] = clusters
    return result_df, f"Clustering effectué avec {n_clusters} groupes."
