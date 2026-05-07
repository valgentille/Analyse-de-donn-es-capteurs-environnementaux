import pandas as pd
import numpy as np

np.random.seed(42)
dates = pd.date_range(start="2024-01-01", periods=2000, freq="30min")

temperature = (
    15
    + 10 * np.sin(2 * np.pi * np.arange(2000) / 48)  # cycle jour/nuit
    + np.random.normal(0, 1, 2000)                     # bruit
)

# Injection de quelques anomalies
temperature[200] = 55
temperature[800] = -25
temperature[1500] = 60

df = pd.DataFrame({
    "Formatted Date": dates,
    "temperature": temperature,
    "humidity": 60 + np.random.normal(0, 5, 2000)
})

df.to_csv("sample.csv", index=False)
print("Dataset généré !")