import os
from groq import Groq

def generate_answer(query, retrieved_chunks):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""You are a helpful assistant. Answer the user's question using ONLY the provided context below. 
If the answer cannot be found in the context, state clearly that the information is not available in the document.

Context:
{context}

Question:
{query}

Answer:"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content