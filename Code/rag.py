import os
from groq import Groq

def generate_answer(query, context_chunks):
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable is missing.")

    client = Groq(api_key=api_key)

    context_text = "\n\n".join(context_chunks)

    prompt = f"""You are a helpful assistant. Use the following context from the document to answer the question.

Context:
{context_text}

Question: {query}
Answer:"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content