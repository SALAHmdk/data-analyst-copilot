import plotly.express as px
import plotly.graph_objects as go

def plot_histogram(df, col):
    fig = px.histogram(df, x=col, title=f"Distribution de {col}")
    return fig

def plot_boxplot(df, col):
    fig = px.box(df, y=col, title=f"Boxplot de {col}")
    return fig

def plot_timeseries(df, date_col, val_col):
    df_sorted = df.sort_values(date_col)
    fig = px.line(df_sorted, x=date_col, y=val_col, title=f"Évolution de {val_col} au cours du temps")
    return fig

def plot_correlation_heatmap(corr_matrix):
    fig = px.imshow(corr_matrix, text_auto=True, title="Matrice de Corrélation")
    return fig
