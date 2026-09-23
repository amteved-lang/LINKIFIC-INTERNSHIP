# Complete RAG API using FastAPI

## Project Overview

This project implements a document question-answering API using FastAPI.

Users can upload a PDF document, process its content, create document embeddings, perform semantic retrieval, and ask questions based on the uploaded document.

## Learning Objectives

- FastAPI
- File Upload
- PDF Processing
- Document Chunking
- Metadata
- Embeddings
- Semantic Search
- API Endpoints
- RAG Concepts
- API Robustness Testing

## Workflow

PDF Upload  
↓  
Text Extraction  
↓  
Document Chunking  
↓  
Metadata Generation  
↓  
Embeddings  
↓  
Semantic Search  
↓  
Relevant Context Retrieval  
↓  
Grounded Response

## API Endpoints

### GET /

Checks whether the API is running.

### POST /upload

Uploads and processes a PDF document.

The API extracts text, creates chunks, generates embeddings, and stores document metadata.

### POST /ask

Accepts a question and retrieves the most semantically relevant information from the uploaded document.

### GET /document-info

Returns metadata about the currently uploaded document.

## Embedding Model

`all-MiniLM-L6-v2`

The model converts document chunks and questions into numerical vector representations.

## Semantic Search

Cosine similarity is used to compare the question embedding with document chunk embeddings.

The chunk with the highest similarity score is selected as the relevant context.

## Robustness Testing

The API was designed to handle:

- Valid PDF files
- Unsupported file formats
- Empty files
- Corrupted PDFs
- Large documents
- Empty questions
- Requests made before uploading a document

## Technologies Used

- Python
- FastAPI
- Uvicorn
- PyPDF
- Sentence Transformers
- Scikit-learn
- NumPy
- Swagger UI
- VS Code
- Git
- GitHub

## Project Files

- `main.py` - FastAPI application
- `requirements.txt` - Required Python libraries
- `testing_report.md` - API robustness testing report
- `improvement_suggestions.md` - Suggested improvements
- `screenshots/` - API response screenshots
- `README.md` - Project documentation

## Limitations

The current implementation stores document embeddings in memory.

The system retrieves the most relevant document chunk as the grounded response. A future version can integrate an LLM to generate a more natural answer from retrieved context.

## Conclusion

The project demonstrates how FastAPI can be combined with document processing, embeddings, semantic search, metadata, and API endpoints to build the foundation of a document-based RAG application.