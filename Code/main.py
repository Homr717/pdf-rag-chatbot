import os
from pdf_utils import extract_text_from_pdf, chunk_text
from search import build_vector_index, search_top_chunks
from rag import generate_answer

def main():
    pdf_path = input("Enter path to PDF file: ").strip()

    if not os.path.exists(pdf_path):
        print("Error: File not found.")
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

        relevant_chunks = search_top_chunks(query, index, chunks, top_k=3)
        answer = generate_answer(query, relevant_chunks)

        print(f"\nAI: {answer}\n")

if __name__ == "__main__":
    main()