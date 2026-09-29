# Multi-Agent Research Assistant Workflow

## Workflow Diagram

```mermaid
flowchart TD

    A[User Query] --> B[Coordinator Agent]

    B --> C[Create Research Plan]

    C --> D[Research Agent]

    D --> E[Company Documentation / Knowledge Sources]

    E --> D

    D --> F[Analyzer Agent]

    F --> G[Critic Agent]

    G --> H{Result Approved?}

    H -->|No| I[Feedback / Improvement Required]

    I --> D

    H -->|Yes| J[Writer Agent]

    J --> K[Coordinator Agent]

    K --> L[Final Response]