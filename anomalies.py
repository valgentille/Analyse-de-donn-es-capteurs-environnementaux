def detect_anomalies(df, column="temperature", window=24):
    # Moyenne glissante sur 24h
    df["rolling_mean"] = df[column].rolling(window).mean()
    df["rolling_std"] = df[column].rolling(window).std()
    
    # Anomalie = valeur à plus de 2 écarts-types de la moyenne
    df["is_anomaly"] = (
        (df[column] > df["rolling_mean"] + 2 * df["rolling_std"]) |
        (df[column] < df["rolling_mean"] - 2 * df["rolling_std"])
    )
    return df