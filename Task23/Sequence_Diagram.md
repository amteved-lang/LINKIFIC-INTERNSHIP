# Multi-Agent Sequence Diagram

```mermaid
sequenceDiagram

    participant U as User
    participant C as Coordinator
    participant R as Research Agent
    participant A as Analyzer
    participant CR as Critic
    participant W as Writer

    U->>C: Submit company question

    C->>C: Create research plan

    C->>R: Send research task

    R->>R: Search company documentation

    R->>A: Send retrieved information

    A->>A: Analyze research

    A->>CR: Send structured analysis

    CR->>CR: Check quality

    alt Information Approved

        CR->>W: Send approved analysis

        W->>W: Prepare final response

        W->>U: Return final answer

    else Information Insufficient

        CR->>C: Request improvement

        C->>R: Perform additional research

        R->>A: Updated research result

        A->>CR: Updated analysis

        CR->>W: Approved result

        W->>U: Final answer

    end