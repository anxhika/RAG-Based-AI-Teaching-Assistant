import requests
import os
import json
import pandas as pd
import joblib


MODEL_NAME = "mxbai-embed-large"


def clean_text(text):

    if text is None:
        return None

    text = str(text).strip()

    if text == "" or text.lower() == "nan":
        return None

    return text[:1200]


def create_embedding(text):

    r = requests.post(
        "http://localhost:11434/api/embed",
        json={
            "model": MODEL_NAME,
            "input": text
        }
    )

    result = r.json()

    # correct key for ollama
    if "embedding" in result:
        return result["embedding"]

    if "embeddings" in result:
        return result["embeddings"][0]

    # only print short message
    print("Embedding error occurred - skipping chunk")

    return None


jsons = os.listdir("jsons")

all_chunks = []
chunk_id = 0


for json_file in jsons:

    print(f"Processing: {json_file}")

    with open(f"jsons/{json_file}", encoding="utf-8") as f:
        content = json.load(f)

    for chunk in content["chunks"]:

        text = clean_text(chunk.get("text"))

        if text is None:
            continue

        embedding = create_embedding(text)

        if embedding is None:
            continue

        chunk["chunk_id"] = chunk_id






        0
        chunk["embedding"] = embedding

        all_chunks.append(chunk)

        chunk_id += 1


df = pd.DataFrame(all_chunks)

joblib.dump(df, "embeddings.joblib")

print("\nTotal chunks stored:", len(df))
print("embeddings.joblib created successfully")
