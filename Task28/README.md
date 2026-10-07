# HearMe Support Routing Feature

## Project Overview

This project implements a customer-support routing feature for the HearMe AI platform.

The feature determines whether a customer query can be handled automatically or requires human intervention.

## Learning Objectives

- Pull Requests
- Code Reviews
- Team Development
- Feature Integration
- Code Readability
- Modularity
- Error Handling

## Feature Workflow

```text
Customer Query
      ↓
FastAPI
      ↓
Normalize Query
      ↓
Risk Detection
      ↓
Routing Decision
   ↙         ↘
AI Support   Human Support