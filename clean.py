import pandas as pd
import numpy as np
import io


COLUMN_MAP = {
    "Temperature (C)": "temperature",
    "Humidity": "humidity",
    "Formatted Date": "Formatted Date",
}

def load_data(uploaded_file):
    uploaded_file.seek(0)
    bytes_data = uploaded_file.read()
    df = pd.read_csv(io.BytesIO(bytes_data), parse_dates=["Formatted Date"])

   
    df = df.rename(columns=COLUMN_MAP)

    return df

def clean_data(df):
    df = df.drop_duplicates()
    df = df.interpolate(method="linear")
    df = df[df["temperature"].between(-20, 50)]

    return df