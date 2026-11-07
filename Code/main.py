import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pdf_utils import extract_text_from_pdf, chunk_text
from search import build_vector_index, search_top_chunks
from rag import generate_answer

def clean_path(path_str):
    p = path_str.strip().strip('"').strip("'")
    if p.startswith('/c/') or p.startswith('/C/'):
        p = 'C:' + p[2:]
    elif p.startswith('/') and len(p) > 2 and p[2] == '/':
        p = p[1].upper() + ':' + p[2:]
    return p

def main():
    raw_input = input("Enter path to PDF file: ")
    pdf_path = clean_path(raw_input)

    if not os.path.exists(pdf_path):
        print(f"Error: File not found at '{pdf_path}'")
        return

    print("Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)
    chunks = chunk_text(text)

    print("Building FAISS vector index...")
    index = build_vector_index(chunks)
    print("Ready! Ask your questions (type 'exit' to quit).\n")

    while True:
        query = input("You: ").strip()
        if query.lower() in ["exit", "quit"]:
            break

        if not query:
            continue

        relevant_chunks = search_top_chunks(query, index, chunks)
        answer = generate_answer(query, relevant_chunks)

        print(f"\nAI: {answer}\n")

if __name__ == "__main__":
    main()