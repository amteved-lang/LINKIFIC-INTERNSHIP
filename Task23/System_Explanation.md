# Multi-Agent System Explanation

## Overview

The HearMe Multi-Agent Research Assistant is implemented using LangGraph.

The system divides a company research task among several specialized AI agents.

## Agents

### Coordinator Agent

The Coordinator receives the user's question and creates the research task.

It controls workflow execution and retry decisions.

### Research Agent

The Research Agent searches company documentation for relevant information.

### Analyzer Agent

The Analyzer converts retrieved information into structured findings.

### Critic Agent

The Critic evaluates whether the information is relevant and sufficient.

The Critic can either:

- Approve the result
- Request another research attempt

### Writer Agent

The Writer prepares the final user-facing response using approved company information.

## LangGraph Integration

LangGraph is used to connect agents as graph nodes.

Each agent represents one node.

```text
Coordinator
    ↓
Research
    ↓
Analyzer
    ↓
Critic
    ↓
Writer