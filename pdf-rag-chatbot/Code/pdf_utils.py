from pypdf import PdfReader

def parse_pdf(path, chunk_words=350, overlap=50):

    reader = PdfReader(path)
    text = ""

    # Stores pages in text string
    for page in reader.pages:
        t = page.extract_text()
        if t:
            text += t + "\n"

    # Splits text into chunks of 350 words with 50 words repeated on each chunk to avoid overlap
    words = text.split()
    chunks = []
    step = chunk_words - overlap

    for i in range(0, len(words), step):
        chunks.append(" ".join(words[i:i + chunk_words]))
        if i + chunk_words >= len(words):
            break

    return chunks