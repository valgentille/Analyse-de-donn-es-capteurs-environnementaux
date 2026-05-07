
# 🌿 Analyse de données capteurs environnementaux

Application web interactive pour l'analyse de séries temporelles de température et la détection automatique d'anomalies, construite avec **Streamlit**.

---

## 📸 Fonctionnalités

- 📂 Upload d'un fichier CSV de données environnementales
- 📊 Statistiques générales sur les données
- 📈 Visualisation de l'évolution de la température
- ⚠️ Détection automatique d'anomalies (moyenne glissante + écarts-types)

---

## 🗂️ Structure du projet

```
projetdetemperature/
│
├── app.py            # Interface Streamlit (point d'entrée)
├── clean.py          # Chargement et nettoyage des données
├── anomalies.py      # Détection d'anomalies
├── code.py           # Génération du dataset synthétique
├── sample.csv        # Dataset de test (généré)
└── requirements.txt  # Dépendances
```

---

## 🚀 Lancer l'application

```bash
# Installer les dépendances
pip install -r requirements.txt

# Lancer l'app
streamlit run app.py
```

L'application s'ouvre automatiquement sur `http://localhost:8501`.

---

## 📁 Datasets compatibles

| Fichier | Description |
|---|---|
| `sample.csv` | Dataset synthétique inclus dans le repo (2000 mesures) |
| [weatherHistory.csv](https://www.kaggle.com/datasets/budincsevity/szeged-weather) | Dataset Kaggle — Historique météo de Szeged (2006–2016) |

---

## 🛠️ Technos utilisées

![Python]
![Streamlit]
![Pandas]
![Matplotlib]
