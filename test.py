import joblib

df = joblib.load("embeddings.joblib")
print(df.columns)
print(df.head())