# PDF RAG Chatbot (Custom Vector Search)

A custom, manual Retrieval-Augmented Generation (RAG) implementation built from scratch without high-level frameworks like LangChain. This application processes PDF documents, builds a vector index locally using Meta's FAISS, and performs semantic search to answer interactive queries via the Groq LLM API.

## How It Works

* **`pdf_utils.py`**: Extracts raw text using `pypdf` and breaks it into overlapping text chunks.

* **`search.py`**: Converts text chunks into numerical vectors using `sentence-transformers` (`all-MiniLM-L6-v2`) and performs fast L2 similarity search with `faiss-cpu`.

* **`rag.py`**: Combines the user query with top matching PDF chunks into a prompt and fetches the answer via Groq API (`llama-3.3-70b-versatile`).

* **`main.py`**: Runs the interactive terminal chat loop.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your Groq API key:
```bash
export GROQ_API_KEY="your_api_key_here"
```

## Usage

Run the main application script:
```bash
python main.py
```