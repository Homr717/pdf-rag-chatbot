# PDF RAG Chatbot

A custom, manual Retrieval-Augmented Generation (RAG) implementation built from scratch without high-level frameworks like LangChain. This application processes PDF documents, builds a vector index locally using Meta's FAISS, and performs semantic search to answer interactive queries via the Groq LLM API.
## Project Structure

pdf-rag-chatbot/
└── pdf-rag-chatbot/
    ├── pdf_utils.py
    ├── search.py
    ├── rag.py
    ├── main.py
    ├── .gitignore
    ├── requirements.txt
    └── README.md


## System Architecture

                      ┌─────────────────────────┐
                      │    PDF Input Document   │
                      └────────────┬────────────┘
                                   │
                                   ▼
┌──────────────────────────────────────────────────────────────────────┐
│ pdf_utils.py                                                         │
│  - Extracts raw text using pypdf                                     │
│  - Splits text into manageable, overlapping chunks                   │
└──────────────────────────────────┬───────────────────────────────────┘
                                   │
                                   ▼
┌──────────────────────────────────────────────────────────────────────┐
│ search.py                                                            │
│  - Generates embeddings with sentence-transformers (all-MiniLM-L6-v2) │
│  - Stores coordinates in a local Meta FAISS vector index             │
│  - Runs vector similarity search to retrieve Top-K relevant chunks   │
└──────────────────────────────────┬───────────────────────────────────┘
                                   │
                                   ▼
┌──────────────────────────────────────────────────────────────────────┐
│ rag.py                                                               │
│  - Combines user query + Top-K PDF chunks into a context prompt      │
│  - Sends payload via HTTPS to Groq Cloud API                         │
│  - Generates answer using llama-3.3-70b-versatile                     │
└──────────────────────────────────┬───────────────────────────────────┘
                                   │
                                   ▼
                      ┌─────────────────────────┐
                      │   Terminal Output / AI  │
                      └─────────────────────────┘
## Setup

1. Install dependencies:
pip install -r requirements.txt

2. Set your Groq API key:
export GROQ_API_KEY="your_api_key_here"

## Usage

Run the main application script:
python pdf-rag-chatbot/main.py