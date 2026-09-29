# Multi-Agent Architecture Notes

## Project Overview

The HearMe Multi-Agent Research Assistant uses multiple specialized AI agents to complete research-oriented tasks.

Instead of asking one AI model to perform every operation, responsibilities are distributed among agents.

## Architecture

```text
                    USER
                      │
                      ▼
              Coordinator Agent
                      │
                      ▼
                Research Plan
                      │
                      ▼
               Research Agent
                      │
              Company Knowledge
                      │
                      ▼
                Analyzer Agent
                      │
                      ▼
                 Critic Agent
                   /       \
              Reject       Approve
                │             │
                ▼             ▼
          Research Again   Writer Agent
                              │
                              ▼
                      Coordinator Agent
                              │
                              ▼
                         Final Answer