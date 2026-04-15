# 📚 RAG-Based AI Teaching Assistant

An AI-powered Teaching Assistant built using **Retrieval-Augmented Generation (RAG)** that answers questions from course lecture videos.  
The system converts lecture videos into transcripts, generates embeddings, retrieves relevant context, and produces accurate answers using a Large Language Model.

---

## 🚀 Project Overview

This project simulates a **virtual teaching assistant** for Data Science courses.  
Instead of relying only on a language model, the system retrieves relevant information from lecture transcripts before generating answers. This ensures responses are **accurate, contextual, and grounded in course material**.

---

## 🧠 System Pipeline

```
Lecture Videos
      ↓
Whisper Transcription
      ↓
Text Chunking
      ↓
Embedding Generation
      ↓
Vector Database Storage
      ↓
Semantic Retrieval
      ↓
LLM Answer Generation
```

---

## ⚙️ Tech Stack

- Python
- OpenAI Whisper (Speech-to-Text)
- Sentence Transformers / OpenAI Embeddings
- Pandas
- Vector Database (FAISS / Chroma)
- Large Language Models (LLM)

---

## 📊 Key Features

- Converts **lecture videos into transcripts automatically**
- Splits transcripts into **semantic chunks**
- Generates **vector embeddings for semantic search**
- Retrieves **top relevant chunks for each user query**
- Produces **context-aware answers using LLMs**

---

## 📁 Project Structure

```
rag-ai-teaching-assistant/
│
├── videos/                # Lecture videos
├── transcripts/           # Generated transcripts
├── embeddings/            # Vector embeddings
│
├── transcribe.py          # Convert video → transcript
├── chunking.py            # Create text chunks
├── embeddings.py          # Generate embeddings
├── rag_pipeline.py        # Retrieval + response generation
│
├── requirements.txt
└── README.md
```

---

## 📥 Dataset

Lecture videos were collected from publicly available Data Science lectures.

The system processes:

- **20+ lecture videos**
- **200+ minutes of lecture content**
- **500+ semantic text chunks**

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/rag-ai-teaching-assistant.git
cd rag-ai-teaching-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Step 1: Download Lecture Videos

Use `yt-dlp` to download lecture videos:

```bash
yt-dlp "YOUTUBE_VIDEO_LINK"
```

Save videos inside the **videos/** folder.

---

## ▶️ Step 2: Transcribe Videos

Run Whisper transcription:

```bash
python transcribe.py
```

This converts lecture videos into text transcripts.

---

## ▶️ Step 3: Generate Embeddings

```bash
python embeddings.py
```

This step creates vector embeddings for semantic search.

---

## ▶️ Step 4: Run the RAG Assistant

```bash
python rag_pipeline.py
```

Example query:

```
User: What is PCA?
Assistant: PCA is a dimensionality reduction technique that transforms data into principal components...
```

---

## 📈 Results

- Processed **20+ lecture videos**
- Generated **500+ semantic text chunks**
- Implemented **semantic retrieval using embeddings**
- Generated **context-aware answers within seconds**

---

## 🔮 Future Improvements

- Add **Streamlit / Gradio interface**
- Integrate **FAISS vector database**
- Deploy using **Docker**
- Support **multiple courses**
- Build **interactive web-based Q&A assistant**

---

## 👩‍💻 Author

**Anshika Tiwari**

AI / Data Science Enthusiast
