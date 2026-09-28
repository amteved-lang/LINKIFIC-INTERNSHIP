# Async FastAPI & Performance Benchmarking

## Project Overview

This project demonstrates asynchronous programming and performance optimization using FastAPI.

A synchronous API endpoint was compared with an asynchronous implementation under concurrent requests.

## Learning Objectives

- Async Programming
- Async/Await
- Middleware
- Background Tasks
- Dependency Injection
- API Versioning
- Validation
- API Performance
- Benchmarking

## API Architecture

```text
Client Request
      ↓
Performance Middleware
      ↓
API Version
   ↙       ↘
 V1         V2
Sync       Async
 ↓           ↓
Processing
      ↓
Background Task
      ↓
Response