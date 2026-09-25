# LangGraph Customer Support Workflow

```mermaid
flowchart TD

    A[User] --> B[Question Node]

    B --> C[Retriever Node]

    C --> D{Relevant Context Found?}

    D -->|Yes| E[LLM Node]

    D -->|No - Retry Available| F[Rewrite Query]

    F --> C

    D -->|No - Retry Failed| G[Fallback Node]

    E --> H[Answer Node]

    G --> H

    H --> I[Memory Node]

    I --> J[Final Response]