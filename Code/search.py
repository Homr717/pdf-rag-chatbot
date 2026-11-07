import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def build_vector_index(chunks):
    """
    Takes text chunks from pdf_utils.py, turns them into vectors,
    and stores them inside a FAISS index.
    """
    embeddings = model.encode(chunks, convert_to_numpy=True)

    vector_dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(vector_dimension)

    index.add(embeddings)

    return index

def search_top_chunks(query, index, original_chunks, top_k=3):
    """
    Converts user's query into a vector and finds top_k nearest text chunks.
    """
    query_vector = model.encode([query], convert_to_numpy=True)

    distances, indices = index.search(query_vector, top_k)


    matched_chunks = [original_chunks[i] for i in indices[0] if i < len(original_chunks)]

    return matched_chunks