# RAG-Based AI Teaching Assistant

An AI-powered Teaching Assistant built using Retrieval-Augmented Generation (RAG) that answers questions from lecture videos.

The system converts lecture videos into transcripts, generates embeddings, retrieves relevant context, and produces accurate answers using a Large Language Model (LLM).

---

## How it works

Lecture Videos → Audio → Transcript → Text Chunks → Embeddings → Context Retrieval → LLM Answer

---

## Steps to run on your own data

### Step 1 — Add videos

Place lecture videos inside:

```
Videos/
```

### Step 2 — Convert video to mp3

```
python video_to_mp3.py
```

### Step 3 — Convert mp3 to JSON transcript

```
python mp3_to_json.py
```

Output stored in:

```
jsons/
```

### Step 4 — Generate embeddings

```
python preprocess_json.py
```

Output file:

```
embeddings.joblib
```

### Step 5 — Ask questions

```
python process_incoming.py
```

The system retrieves relevant content and generates answers using the LLM.

---

## Project Structure

```
Videos/
jsons/
video_to_mp3.py
mp3_to_json.py
preprocess_json.py
process_incoming.py
embeddings.joblib
README.md
```

---

## Tech Used

Python, RAG, Embeddings, LLM, Speech-to-Text
