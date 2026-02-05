import pandas as pd

def generate_html_report(df, title="Rapport Data Analyst"):
    html = f"<html><head><title>{title}</title></head><body>"
    html += f"<h1>{title}</h1>"
    html += "<h2>Aperçu des données</h2>"
    html += df.head().to_html()
    html += "<h2>Statistiques descriptives</h2>"
    html += df.describe().to_html()
    html += "</body></html>"
    return html

def export_for_bi(df, tool="PowerBI"):
    """
    Prépare un fichier optimisé pour les outils BI.
    Power BI et Tableau préfèrent souvent le CSV propre ou le Parquet.
    """
    if tool == "PowerBI":
        # Power BI gère très bien le CSV UTF-8 avec BOM pour les accents
        return df.to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig')
    elif tool == "Tableau":
        # Tableau est très performant avec le format Hyper (via bibliothèque externe) 
        # ou un CSV standard propre. Ici on reste sur CSV pour la portabilité.
        return df.to_csv(index=False).encode('utf-8')
    return df.to_csv(index=False).encode('utf-8')
