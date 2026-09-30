# Multi-Agent Communication Flow Document

## Project

HearMe Multi-Agent Research Assistant

## Objective

This document demonstrates one complete interaction between all agents in the multi-agent system.

## Example User Request

**User:**

How is ASR performance evaluated?

## Step 1 - User to Coordinator

### Input

How is ASR performance evaluated?

### Coordinator Action

The Coordinator receives the request and creates a research task.

### Output

Find company information relevant to how ASR performance is evaluated.

---

## Step 2 - Coordinator to Research Agent

The Research Agent receives the research task.

It searches the HearMe company documentation.

### Retrieved Information

Automatic Speech Recognition performance can be evaluated using Word Error Rate, Character Error Rate, and inference time.

---

## Step 3 - Research Agent to Analyzer

The Research Agent sends the retrieved information to the Analyzer Agent.

The Analyzer organizes the information into a structured finding.

### Analysis

The company documentation indicates that ASR performance is evaluated using:

- Word Error Rate
- Character Error Rate
- Inference Time

---

## Step 4 - Analyzer to Critic

The Critic receives the analysis.

The Critic checks:

- Relevance
- Completeness
- Accuracy
- Whether sufficient company information exists

### Critic Decision

Approved.

### Feedback

The retrieved information is relevant and sufficient.

---

## Step 5 - Critic to Writer

The Writer Agent receives the approved information.

It prepares a clear final response.

### Writer Output

Based on the company documentation, ASR performance is evaluated using Word Error Rate, Character Error Rate, and inference time.

---

## Step 6 - Final Response

The final response is returned to the user.

## Complete Communication Flow

```text
User
 ↓
Coordinator
 ↓
Research Agent
 ↓
Analyzer
 ↓
Critic
 ↓
Writer
 ↓
Final Answer