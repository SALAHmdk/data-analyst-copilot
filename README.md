# Data Analyst Copilot 🚀

MVP d'application Streamlit pour l'analyse automatisée de données.

## Fonctionnalités
- Import CSV/XLSX ou copier-coller.
- Profiling complet (statistiques, corrélations, manquants).
- Visualisations interactives avec Plotly.
- Analyse KPI et tendances.
- Segmentation par Clustering (K-Means).
- Détection d'anomalies (Isolation Forest).
- Générateur de requêtes SQL.
- Export de rapports HTML et datasets nettoyés.

## Installation
1. Créer un environnement virtuel : `python -m venv .venv`
2. Activer l'environnement : 
   - Windows : `.venv\Scripts\activate`
   - Mac/Linux : `source .venv/bin/activate`
3. Installer les dépendances : `pip install -r requirements.txt`
4. Lancer l'app : `streamlit run app.py`

## Prérequis
- Installer Docker Desktop (Windows/Mac) ou Docker Engine (Linux)
- Vérifier :
  - `docker --version`
  - `docker compose version`

## Lancer l'app (recommandé)
```bash
docker compose up --build
