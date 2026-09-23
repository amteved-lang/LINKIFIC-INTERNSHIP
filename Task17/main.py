from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from io import BytesIO
import numpy as np

app = FastAPI(
    title="RAG Document Question Answering API",
    description="Upload a PDF and ask questions based on its content.",
    version="1.0"
)

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

document_chunks = []
chunk_embeddings = None
document_metadata = {}

MAX_FILE_SIZE = 10 * 1024 * 1024

class QuestionRequest(BaseModel):
    question: str

def create_chunks(text, chunk_size=100):
    words = text.split()

    if not words:
        return []

    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size]).strip()

        if chunk:
            chunks.append({
                "chunk_id": len(chunks) + 1,
                "text": chunk,
                "word_count": len(chunk.split())
            })

    return chunks

@app.get("/")
def home():
    return {
        "status": "running",
        "message": "RAG API is running successfully."
    }

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    global document_chunks
    global chunk_embeddings
    global document_metadata

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No filename provided."
        )

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Unsupported file format. Only PDF files are allowed."
        )

    content = await file.read()

    if len(content) == 0:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty."
        )

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="File is too large. Maximum allowed size is 10 MB."
        )

    try:
        reader = PdfReader(BytesIO(content))
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid or corrupted PDF file."
        )

    text = ""

    for page_number, page in enumerate(reader.pages, start=1):
        try:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        except Exception:
            continue

    text = text.strip()

    if not text:
        raise HTTPException(
            status_code=400,
            detail="No readable text was found in the PDF."
        )

    document_chunks = create_chunks(text)

    if not document_chunks:
        raise HTTPException(
            status_code=400,
            detail="Unable to create document chunks."
        )

    texts = [
        chunk["text"]
        for chunk in document_chunks
    ]

    chunk_embeddings = embedding_model.encode(
        texts,
        convert_to_numpy=True
    )

    document_metadata = {
        "filename": file.filename,
        "content_type": file.content_type,
        "file_size_bytes": len(content),
        "pages": len(reader.pages),
        "total_words": len(text.split()),
        "total_chunks": len(document_chunks),
        "chunk_size_words": 100
    }

    return {
        "message": "PDF uploaded and processed successfully.",
        "metadata": document_metadata
    }

@app.post("/ask")
def ask_question(request: QuestionRequest):
    global document_chunks
    global chunk_embeddings

    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    if not document_chunks or chunk_embeddings is None:
        raise HTTPException(
            status_code=400,
            detail="Upload a PDF before asking questions."
        )

    question_embedding = embedding_model.encode(
        [question],
        convert_to_numpy=True
    )

    similarities = cosine_similarity(
        question_embedding,
        chunk_embeddings
    )[0]

    best_index = int(np.argmax(similarities))
    best_score = float(similarities[best_index])

    retrieved_chunk = document_chunks[best_index]

    if best_score < 0.20:
        answer = (
            "The uploaded document does not appear to contain "
            "enough relevant information to answer this question."
        )
    else:
        answer = retrieved_chunk["text"]

    return {
        "question": question,
        "answer": answer,
        "similarity_score": round(best_score, 4),
        "retrieved_chunk": {
            "chunk_id": retrieved_chunk["chunk_id"],
            "word_count": retrieved_chunk["word_count"]
        }
    }

@app.get("/document-info")
def document_info():
    if not document_metadata:
        raise HTTPException(
            status_code=404,
            detail="No document has been uploaded."
        )

    return document_metadata