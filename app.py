import pandas as pd
import streamlit as st

from src import (anomalies, cleaning, io_utils, kpi, profiling, report,
                 segmentation, sql_generator, viz)

st.set_page_config(page_title="Data Analyst Copilot PRO", layout="wide")

st.title("🚀 Data Analyst Copilot PRO")
st.markdown("Votre assistant intelligent pour l'analyse de données - Version Étendue.")

# --- SIDEBAR ---
st.sidebar.header("📥 Importation des données")
upload_type = st.sidebar.selectbox("Source", ["Fichier (Tous formats)", "API JSON/REST", "Coller un tableau"])

df = None
if upload_type == "Fichier (Tous formats)":
    uploaded_file = st.sidebar.file_uploader("Choisir un fichier (CSV, XLSX, JSON, Parquet, TXT)", type=['csv', 'xlsx', 'xls', 'json', 'parquet', 'txt'])
    if uploaded_file:
        df = io_utils.load_data(uploaded_file)
elif upload_type == "API JSON/REST":
    api_url = st.sidebar.text_input("URL de l'API", "https://jsonplaceholder.typicode.com/posts")
    if st.sidebar.button("Récupérer les données API"):
        result = io_utils.fetch_api_data(api_url)
        if isinstance(result, pd.DataFrame):
            df = result
            st.sidebar.success("Données API récupérées !")
        else:
            st.sidebar.error(f"Erreur API : {result}")
else:
    pasted_text = st.sidebar.text_area("Coller vos données ici (CSV, Tab, etc.)")
    if pasted_text:
        df = io_utils.parse_pasted_data(pasted_text)

if df is not None:
    st.sidebar.success(f"Données chargées : {df.shape[0]} lignes, {df.shape[1]} colonnes")
    
    # --- OPTIONS DE COLONNES ---
    cols_info = io_utils.detect_columns(df)
    st.sidebar.header("⚙️ Configuration")
    date_col = st.sidebar.selectbox("Colonne Date", [None] + cols_info['date'])
    cat_col = st.sidebar.selectbox("Colonne Catégorie", [None] + cols_info['cat'])
    num_col = st.sidebar.selectbox("Colonne Métrique", [None] + cols_info['num'])

    # --- MENU DE SORTIE ---
    st.sidebar.header("📊 Analyse & Export")
    analysis_type = st.sidebar.selectbox("Type d'analyse", [
        "Profiling rapide", 
        "Visualisations", 
        "Analyse KPI", 
        "Segmentation (K-Means)", 
        "Détection d'anomalies",
        "Générateur SQL",
        "Rapport Exportable",
        "Export Power BI / Tableau",
        "Nettoyage & Export"
    ])
    
    run_button = st.sidebar.button("Lancer l'analyse")

    # --- MAIN CONTENT ---
    st.subheader("📋 Aperçu des données")
    st.dataframe(df.head())

    if run_button:
        st.divider()
        if analysis_type == "Profiling rapide":
            st.header("🔍 Profiling Rapide")
            info = profiling.get_basic_info(df)
            col1, col2, col3 = st.columns(3)
            col1.metric("Lignes", info['shape'][0])
            col2.metric("Colonnes", info['shape'][1])
            col3.metric("Doublons", info['duplicates'])
            st.write("### Valeurs manquantes")
            st.write(pd.Series(info['missing']))
            st.write("### Statistiques")
            st.write(df.describe())
            corr = profiling.get_correlations(df)
            if corr is not None:
                st.write("### Corrélations")
                st.plotly_chart(viz.plot_correlation_heatmap(corr))

        elif analysis_type == "Visualisations":
            st.header("📈 Exploration & Visualisations")
            if num_col:
                st.plotly_chart(viz.plot_histogram(df, num_col))
                st.plotly_chart(viz.plot_boxplot(df, num_col))
            if date_col and num_col:
                st.plotly_chart(viz.plot_timeseries(df, date_col, num_col))

        elif analysis_type == "Analyse KPI":
            st.header("🎯 Analyse KPI")
            if cat_col and num_col:
                aggregates = kpi.calculate_aggregates(df, cat_col, num_col)
                st.dataframe(aggregates)

        elif analysis_type == "Segmentation (K-Means)":
            st.header("🤖 Segmentation simple")
            res_df, msg = segmentation.perform_clustering(df)
            st.info(msg)
            if res_df is not None:
                st.dataframe(res_df.head())

        elif analysis_type == "Détection d'anomalies":
            st.header("🚨 Détection d'anomalies")
            anomalies_df = anomalies.detect_anomalies_iforest(df)
            if anomalies_df is not None:
                st.dataframe(anomalies_df)

        elif analysis_type == "Générateur SQL":
            st.header("💻 Générateur SQL")
            intention = st.text_input("Intention", "Somme par catégorie")
            st.code(sql_generator.generate_sql("data", df.columns.tolist(), intention), language='sql')

        elif analysis_type == "Rapport Exportable":
            st.header("📄 Rapport")
            html = report.generate_html_report(df)
            st.download_button("Télécharger le rapport HTML", html, "rapport.html", "text/html")

        elif analysis_type == "Export Power BI / Tableau":
            st.header("📊 Export pour Outils BI")
            col_bi1, col_bi2 = st.columns(2)
            
            with col_bi1:
                st.subheader("Power BI")
                st.write("Format CSV optimisé (UTF-8 with BOM)")
                pb_data = report.export_for_bi(df, "PowerBI")
                st.download_button("Télécharger pour Power BI", pb_data, "data_powerbi.csv", "text/csv")
                
            with col_bi2:
                st.subheader("Tableau")
                st.write("Format CSV standard propre")
                tab_data = report.export_for_bi(df, "Tableau")
                st.download_button("Télécharger pour Tableau", tab_data, "data_tableau.csv", "text/csv")

        elif analysis_type == "Nettoyage & Export":
            st.header("🧹 Nettoyage & Export")
            df_cleaned = cleaning.clean_dataset(df)
            st.dataframe(df_cleaned.head())
            csv = df_cleaned.to_csv(index=False).encode('utf-8')
            st.download_button("Télécharger CSV nettoyé", csv, "data_cleaned.csv", "text/csv")

else:
    st.info("Veuillez importer des données (Fichier, API ou Coller) pour commencer.")
