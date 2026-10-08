# Architecture Summary

## Project Architecture

```text
User
 ↓
FastAPI Backend
 ↓
Input Validation
 ↓
AI Agent / RAG Router
 ↓
Company Knowledge Base
 ↓
Embeddings / Semantic Search
 ↓
Response Generation
 ↓
Human Escalation if Required
 ↓
Final Answer