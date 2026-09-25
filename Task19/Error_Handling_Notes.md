# LangGraph Error Handling Notes

## Failure Scenario

The Retriever may fail to find relevant information for a user question.

Possible causes include:

- Different terminology
- Missing information
- Invalid input
- Retrieval errors

## Recovery Strategy

The workflow uses conditional routing.

If retrieval succeeds:

Retriever → LLM

If retrieval fails on the first attempt:

Retriever → Query Rewrite → Retriever

If retrieval fails again:

Retriever → Fallback Response

## Loop Protection

The workflow stores a retry counter in the graph state.

Only one query rewrite attempt is allowed.

This prevents the workflow from entering an infinite loop.

## Exception Handling

The Retriever node uses exception handling.

If an unexpected retrieval error occurs, the error is saved in the graph state and the workflow routes to the fallback path.

## Safe Fallback

If reliable information cannot be retrieved, the system responds:

"I could not find enough relevant information in the company knowledge base to answer this question."

This is safer than generating unsupported information.