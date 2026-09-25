# LangGraph Workflow & State Management

## Project Overview

This project demonstrates how LangGraph can be used to design a state-based AI workflow with nodes, graphs, shared state, conditional routing, loops, memory, and error handling.

The workflow is designed around a customer-support use case where the system receives a user question, retrieves relevant information, generates a response, and stores the interaction in memory.

## Learning Objectives

- Understand Nodes
- Understand Graphs
- Understand State
- Practice Conditional Flow
- Practice Loops
- Understand Memory
- Build Graph Workflows
- Practice State Management
- Analyze LangGraph workflow failures
- Implement error recovery

## Project Workflow

```text
User
 ↓
Question
 ↓
Retriever
 ↓
Conditional Decision
 ↓
LLM / Query Rewrite / Fallback
 ↓
Answer
 ↓
Memory