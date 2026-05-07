import pandas as pd
import numpy as np
import io

def load_data(uploaded_file):
    # Lire les bytes et les passer à pandas
    uploaded_file.seek(0) 
    bytes_data = uploaded_file.read()
    df = pd.read_csv(io.BytesIO(bytes_data), parse_dates=["Formatted Date"])
    return df

def clean_data(df):
    # 1. Supprimer les doublons
    df = df.drop_duplicates()
    
    # 2. Gérer les valeurs manquantes
    df = df.interpolate(method="linear")
    
    # 3. Détecter les valeurs aberrantes (température impossible)
    df = df[df["temperature"].between(-20, 50)]
    
    return df