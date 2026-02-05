# 🚀 Data Analyst Copilot

Un **Data Analyst Copilot** développé en **Python + Streamlit**, entièrement **dockerisé** et **automatisé avec Jenkins (CI/CD)**.

👉 Le projet fonctionne **à l’identique sur Windows, macOS et Linux** grâce à Docker.

---

## 🎯 Objectif du projet

- Fournir une interface simple pour :
  - Analyser des datasets (CSV, Excel, Parquet)
  - Visualiser des données
  - Explorer des statistiques
- Garantir un déploiement reproductible sur tous les environnements
- Mettre en place une pipeline CI/CD professionnelle

---

## 🧠 Fonctionnalités

- 📊 Analyse de données (Pandas, NumPy)
- 📈 Visualisations interactives (Plotly, Streamlit)
- 📁 Import CSV / Excel / Parquet
- 🐳 Lancement en un clic avec Docker
- 🔁 Pipeline CI/CD automatisée avec Jenkins
- ✅ Smoke test automatique du container Streamlit

---

## 🖥️ Aperçu de l'application

### Interface principale
![UI 1](data-analyst-copilot-pro-01.png)

### Analyse des données
![UI 2](data-analyst-copilot-pro-02.png)

### Visualisation
![UI 3](data-analyst-copilot-pro-03.png)

### Données de simulation
![Simulation](data-simul.png)

---

## 🧰 Technologies utilisées

### 🔹 Data & Backend
- Python 3.11
- Pandas
- NumPy
- Scikit-learn
- PyArrow / FastParquet
- OpenPyXL

### 🔹 Frontend
- Streamlit
- Plotly
- Altair

### 🔹 DevOps & CI/CD
- Docker
- Dockerfile
- Jenkins
- Jenkins Pipeline (Declarative)
- Docker Network (tests inter-containers)
- Curl (smoke test)
- Git & GitHub

---

## 🐳 Lancer le projet avec Docker (recommandé)

### 1. Cloner le projet
```bash
git clone https://github.com/SALAHmdk/data-analyst-copilot.git
cd data-analyst-copilot
