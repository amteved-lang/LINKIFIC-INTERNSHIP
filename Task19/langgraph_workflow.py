from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
import re

class AgentState(TypedDict, total=False):
    original_question: str
    question: str
    context: str
    draft_answer: str
    answer: str
    retry_count: int
    memory: list
    error: str

knowledge_base = [
    "HearMe is an AI-powered voice agent platform used to automate customer communication.",
    "RAG retrieves relevant information from company documentation before generating an answer.",
    "ASR performance is measured using Word Error Rate, Character Error Rate, and inference time.",
    "Complex customer issues can be escalated to a human customer support agent.",
    "Text-to-Speech converts the generated text response into speech for the customer."
]

stop_words = {
    "the", "is", "a", "an", "how", "what", "why", "when",
    "where", "does", "do", "are", "of", "to", "and", "for",
    "in", "on", "it", "be"
}

def tokenize(text):
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    return set(word for word in words if word not in stop_words)

def question_node(state):
    question = state.get("question", "").strip()

    state["original_question"] = question
    state["retry_count"] = 0
    state["error"] = ""

    print("\nNODE: Question")
    print("Question:", question)

    return state

def retriever_node(state):
    print("\nNODE: Retriever")

    try:
        question_words = tokenize(state["question"])

        best_document = ""
        best_score = 0

        for document in knowledge_base:
            document_words = tokenize(document)

            score = len(
                question_words.intersection(document_words)
            )

            if score > best_score:
                best_score = score
                best_document = document

        if best_score > 0:
            state["context"] = best_document

            print("Relevant context found:")
            print(best_document)

        else:
            state["context"] = ""

            print("No relevant context found.")

    except Exception as error:
        state["context"] = ""
        state["error"] = str(error)

    return state

def retrieval_router(state):
    if state.get("error"):
        return "failed"

    if state.get("context"):
        return "found"

    if state.get("retry_count", 0) < 1:
        return "retry"

    return "failed"

def rewrite_query_node(state):
    print("\nNODE: Query Rewrite")

    question = state["question"].lower()

    replacements = {
        "speech recognition": "ASR",
        "automatic speech recognition": "ASR",
        "company information": "RAG company documentation",
        "human support": "human customer support escalation"
    }

    for old, new in replacements.items():
        question = question.replace(old, new)

    state["question"] = question
    state["retry_count"] = state.get("retry_count", 0) + 1

    print("Rewritten Question:")
    print(question)

    return state

def llm_node(state):
    print("\nNODE: LLM")

    context = state["context"]

    state["draft_answer"] = (
        "Based on the retrieved company information, "
        + context
    )

    print("Draft answer generated.")

    return state

def fallback_node(state):
    print("\nNODE: Fallback")

    state["draft_answer"] = (
        "I could not find enough relevant information "
        "in the company knowledge base to answer this question."
    )

    return state

def answer_node(state):
    print("\nNODE: Answer")

    state["answer"] = state["draft_answer"]

    print(state["answer"])

    return state

def memory_node(state):
    print("\nNODE: Memory")

    memory = state.get("memory", [])

    memory.append({
        "question": state["original_question"],
        "answer": state["answer"]
    })

    state["memory"] = memory

    print("Conversation stored in memory.")

    return state

workflow = StateGraph(AgentState)

workflow.add_node("question", question_node)
workflow.add_node("retriever", retriever_node)
workflow.add_node("rewrite", rewrite_query_node)
workflow.add_node("llm", llm_node)
workflow.add_node("fallback", fallback_node)
workflow.add_node("answer", answer_node)
workflow.add_node("memory", memory_node)

workflow.add_edge(START, "question")
workflow.add_edge("question", "retriever")

workflow.add_conditional_edges(
    "retriever",
    retrieval_router,
    {
        "found": "llm",
        "retry": "rewrite",
        "failed": "fallback"
    }
)

workflow.add_edge("rewrite", "retriever")
workflow.add_edge("llm", "answer")
workflow.add_edge("fallback", "answer")
workflow.add_edge("answer", "memory")
workflow.add_edge("memory", END)

app = workflow.compile()

conversation_memory = []

print("===== LANGGRAPH CUSTOMER SUPPORT WORKFLOW =====")
print("Type 'exit' to stop.")

while True:
    user_question = input("\nEnter your question: ").strip()

    if user_question.lower() == "exit":
        break

    if not user_question:
        print("Question cannot be empty.")
        continue

    initial_state = {
        "question": user_question,
        "memory": conversation_memory
    }

    result = app.invoke(initial_state)

    conversation_memory = result["memory"]

    print("\n===== FINAL ANSWER =====")
    print(result["answer"])

    print("\n===== MEMORY =====")

    for item in conversation_memory:
        print("Question:", item["question"])
        print("Answer:", item["answer"])
        print()