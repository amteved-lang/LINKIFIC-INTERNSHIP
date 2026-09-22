# 🔎 Basic RAG Pipeline & Retrieval Performance Analysis

## Project Overview

This project demonstrates a basic Retrieval-Augmented Generation (RAG) workflow using company documentation.

The system converts documentation into embeddings, performs semantic retrieval, retrieves relevant context for user questions, and produces grounded responses.

## Learning Objectives

- Understand Embeddings
- Understand Vector Databases
- Learn about ChromaDB
- Learn about FAISS
- Understand Semantic Search
- Understand the RAG Pipeline
- Analyze retrieval performance
- Compare different document chunk sizes

## RAG Architecture

```text
Company Documentation
        ↓
Document Chunking
        ↓
Embeddings
        ↓
Vector Similarity Search
        ↓
Semantic Retrieval
        ↓
Retrieved Context
        ↓
Grounded AI Response