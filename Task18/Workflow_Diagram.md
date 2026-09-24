                   CUSTOMER
                       │
                       ▼
               Customer Query
                       │
                       ▼
            ┌────────────────────┐
            │ CUSTOMER SUPPORT   │
            │     AI AGENT       │
            └─────────┬──────────┘
                      │
                      ▼
               Understand Intent
                      │
                      ▼
                  Plan Task
                      │
                      ▼
                Select Tool
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
   Knowledge Base  Customer DB  Ticket System
          │           │           │
          └───────────┼───────────┘
                      ▼
                 Observation
                      │
                      ▼
                Evaluate Result
                      │
              ┌───────┴───────┐
              │               │
          Sufficient       Not Sufficient
              │               │
              ▼               ▼
       Generate Answer    Human Escalation
              │               │
              └───────┬───────┘
                      ▼
               Customer Response