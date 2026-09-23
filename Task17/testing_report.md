# RAG API Robustness Testing Report

## Objective

The objective of this testing process was to evaluate the reliability and robustness of the FastAPI-based document question-answering system under different input conditions.

The API was tested with valid documents, unsupported formats, invalid inputs, and different question scenarios.

## Test Environment

- Python
- FastAPI
- Uvicorn
- PyPDF
- Sentence Transformers
- Scikit-learn
- Swagger UI
- VS Code

## API Endpoints Tested

- GET `/`
- POST `/upload`
- POST `/ask`
- GET `/document-info`

## Testing Results

| Test Case | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| Valid PDF | Text-based PDF | Process document | PDF processed successfully with metadata | Passed |
| Unsupported Format | TXT file | Reject file | API returned 400 unsupported format | Passed |
| Empty Question | Empty question | Reject question | API returned 400 | Passed |
| Valid Question | Question related to PDF | Retrieve relevant content | Relevant document chunk retrieved | Passed |
| Document Metadata | GET request | Return metadata | Filename, pages, words and chunks returned | Passed |
| Corrupted PDF | Invalid PDF | Reject document | API rejected invalid PDF | Passed |
| Empty PDF | Empty PDF file | Reject document | API rejected empty/unreadable document | Passed |
| Large PDF | PDF larger than limit | Reject document | API returned file-size error | Passed |

## Observations

The API successfully processed valid text-based PDF documents and generated document embeddings.

Semantic search retrieved relevant document chunks based on the meaning of user questions.

Invalid and unsupported inputs were handled using appropriate HTTP error responses.

Document metadata including filename, file size, number of pages, total words, and number of chunks was successfully generated.

The API currently stores document information and embeddings in memory, meaning the data is lost when the server restarts.

## Conclusion

The FastAPI application successfully handled normal document processing and question-answering operations while also rejecting several invalid input conditions.

The robustness testing demonstrated the importance of file validation, exception handling, file-size restrictions, document processing validation, and question validation in a document-based RAG API.