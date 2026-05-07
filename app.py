import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from clean import load_data, clean_data
from anomalies import detect_anomalies


st.title("🌿 Analyse de données capteurs environnementaux")

uploaded_file = st.file_uploader("Choisissez un fichier CSV")

if uploaded_file is None:
    st.info("Veuillez uploader un fichier CSV pour commencer.")
else:
    df = load_data(uploaded_file)
    df = clean_data(df)
    df = detect_anomalies(df)

    # Statistiques générales
    st.subheader("📊 Statistiques générales")
    st.dataframe(df.describe())

    # Graphique de la série temporelle
    st.subheader("📈 Évolution de la température")
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(df["Formatted Date"], df["temperature"], label="Température")
    anomalies = df[df["is_anomaly"]]
    ax.scatter(anomalies["Formatted Date"], anomalies["temperature"],
               color="red", label="Anomalies", zorder=5)
    ax.legend()
    st.pyplot(fig)

    # Nombre d'anomalies détectées
    st.subheader("⚠️ Anomalies détectées")
    st.write(f"{len(anomalies)} anomalies trouvées sur {len(df)} mesures")
    st.dataframe(anomalies[["Formatted Date", "temperature"]].head(10))