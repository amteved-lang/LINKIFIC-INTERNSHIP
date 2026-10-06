# HearMe AI System Architecture

## Architecture Overview

The HearMe platform uses multiple AI and software components to automate customer communication.

## High-Level Architecture

```text
                         CUSTOMER
                            │
                            ▼
                    Voice / Text Input
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
       Speech-to-Text                Text Input
              │                           │
              └─────────────┬─────────────┘
                            ▼
                       FastAPI Backend
                            │
                            ▼
                    Customer Support Agent
                            │
                    ┌───────┴────────┐
                    │                │
                    ▼                ▼
               RAG System        Business Tools
                    │                │
                    ▼                ▼
             Company Knowledge   Customer Database
                    │
                    ▼
                  LLM
                    │
                    ▼
             Response Validation
                    │
              ┌─────┴─────┐
              │           │
              ▼           ▼
         Safe Answer   Human Agent
              │
              ▼
        Text-to-Speech
              │
              ▼
           Customer