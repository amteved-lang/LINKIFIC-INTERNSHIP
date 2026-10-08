# Technical Interview Questions & Answers

## 1. What is the main objective of your project?

The objective of my project is to build an AI-powered customer support system for the HearMe company project. It supports document-based question answering, AI agent workflows, human escalation, responsible AI practices, testing, logging, and production-readiness concepts.

## 2. What architecture does your project follow?

The project follows a modular AI architecture:

User Query  
↓  
FastAPI Backend  
↓  
Document Processing / RAG / Agent Workflow  
↓  
Retrieval or Tool Selection  
↓  
Response Generation  
↓  
Human Escalation if required

## 3. What is RAG and why did you use it?

RAG means Retrieval-Augmented Generation. It retrieves relevant information from company documentation before producing an answer. I used it to reduce hallucination and make responses grounded in company-specific knowledge.

## 4. What is the role of embeddings?

Embeddings convert text into numerical vectors that capture meaning. They allow the system to compare user questions with document chunks and retrieve semantically relevant information.

## 5. What is the purpose of the AI agent?

The AI agent decides how to handle a user request. It can retrieve company information, route sensitive cases to humans, use tools, and store conversation memory.

## 6. How did you handle sensitive or high-risk queries?

I implemented human escalation logic. Queries involving refunds, payments, legal issues, passwords, complaints, or account changes are routed to human support instead of being handled fully by AI.

## 7. What challenges did you face?

The main challenges were library compatibility, FastAPI path issues, document retrieval accuracy, chunk-size selection, and deciding when the AI should refuse or escalate instead of answering.

## 8. How did you improve production readiness?

I added testing, logging, environment variables, Docker configuration, health endpoints, metrics endpoints, deployment checklist, and a production readiness report.

## 9. How did you test the project?

I tested API endpoints using Swagger, wrote unit tests and API tests using Pytest, tested valid and invalid inputs, checked logs, and verified API responses.

## 10. What future improvements can be added?

Future improvements include real LLM integration, persistent vector database, authentication, user management, OCR for scanned PDFs, better monitoring, cloud deployment, and improved evaluation metrics.