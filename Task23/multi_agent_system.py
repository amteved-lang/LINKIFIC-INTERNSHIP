from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from pathlib import Path
from datetime import datetime
import re

class MultiAgentState(TypedDict, total=False):
    user_query: str
    research_task: str
    research_result: str
    analysis: str
    critic_feedback: str
    approved: bool
    final_answer: str
    retry_count: int
    error: str
    communication_log: list

def add_log(state, agent, message):
    log = state.get("communication_log", [])

    entry = {
        "time": datetime.now().strftime("%H:%M:%S"),
        "agent": agent,
        "message": message
    }

    log.append(entry)
    state["communication_log"] = log

    print(f"\n[{agent}]")
    print(message)

    return state

def coordinator_agent(state):
    query = state.get("user_query", "").strip()

    state["retry_count"] = state.get("retry_count", 0)
    state["error"] = ""

    if not query:
        state["error"] = "User query is empty."
        return add_log(
            state,
            "Coordinator Agent",
            "Error: User query is empty."
        )

    state["research_task"] = (
        "Find company information relevant to: "
        + query
    )

    return add_log(
        state,
        "Coordinator Agent",
        f"Created research task: {state['research_task']}"
    )

def tokenize(text):
    return set(
        re.findall(
            r"\b[a-zA-Z]+\b",
            text.lower()
        )
    )

def research_agent(state):
    try:
        path = Path("company_documentation.txt")

        if not path.exists():
            state["error"] = "Company documentation not found."

            return add_log(
                state,
                "Research Agent",
                state["error"]
            )

        document = path.read_text(
            encoding="utf-8"
        ).strip()

        sections = [
            section.strip()
            for section in document.split("\n")
            if section.strip()
        ]

        query_words = tokenize(
            state["user_query"]
        )

        best_section = ""
        best_score = 0

        for section in sections:
            section_words = tokenize(section)

            score = len(
                query_words.intersection(
                    section_words
                )
            )

            if score > best_score:
                best_score = score
                best_section = section

        if best_score == 0:
            state["research_result"] = ""
        else:
            state["research_result"] = best_section

        return add_log(
            state,
            "Research Agent",
            (
                "Research completed. Retrieved information: "
                + (
                    best_section
                    if best_section
                    else "No relevant information found."
                )
            )
        )

    except Exception as error:
        state["error"] = str(error)

        return add_log(
            state,
            "Research Agent",
            f"Research error: {error}"
        )

def analyzer_agent(state):
    research = state.get(
        "research_result",
        ""
    )

    if not research:
        state["analysis"] = ""

        return add_log(
            state,
            "Analyzer Agent",
            "No research information available for analysis."
        )

    state["analysis"] = (
        "The retrieved company information indicates that "
        + research
    )

    return add_log(
        state,
        "Analyzer Agent",
        f"Analysis created: {state['analysis']}"
    )

def critic_agent(state):
    analysis = state.get(
        "analysis",
        ""
    )

    if not analysis:
        state["approved"] = False
        state["critic_feedback"] = (
            "The analysis does not contain sufficient information."
        )

    elif len(analysis.split()) < 10:
        state["approved"] = False
        state["critic_feedback"] = (
            "The available information is too limited."
        )

    else:
        state["approved"] = True
        state["critic_feedback"] = (
            "The information is relevant and sufficient."
        )

    return add_log(
        state,
        "Critic Agent",
        (
            f"Approved: {state['approved']}. "
            f"Feedback: {state['critic_feedback']}"
        )
    )

def retry_agent(state):
    state["retry_count"] = (
        state.get("retry_count", 0) + 1
    )

    state["research_task"] = (
        "Perform another company knowledge search for: "
        + state["user_query"]
    )

    return add_log(
        state,
        "Coordinator Agent",
        (
            "Critic requested improvement. "
            "Sending the task back to the Research Agent."
        )
    )

def writer_agent(state):
    if state.get("approved"):
        state["final_answer"] = (
            "Based on the company documentation, "
            + state["research_result"]
        )
    else:
        state["final_answer"] = (
            "I could not find enough verified company information "
            "to provide a reliable answer."
        )

    return add_log(
        state,
        "Writer Agent",
        f"Final response prepared: {state['final_answer']}"
    )

def route_after_coordinator(state):
    if state.get("error"):
        return "writer"

    return "research"

def route_after_critic(state):
    if state.get("approved"):
        return "writer"

    if state.get("retry_count", 0) < 1:
        return "retry"

    return "writer"

workflow = StateGraph(MultiAgentState)

workflow.add_node(
    "coordinator",
    coordinator_agent
)

workflow.add_node(
    "research",
    research_agent
)

workflow.add_node(
    "analyzer",
    analyzer_agent
)

workflow.add_node(
    "critic",
    critic_agent
)

workflow.add_node(
    "retry",
    retry_agent
)

workflow.add_node(
    "writer",
    writer_agent
)

workflow.add_edge(
    START,
    "coordinator"
)

workflow.add_conditional_edges(
    "coordinator",
    route_after_coordinator,
    {
        "research": "research",
        "writer": "writer"
    }
)

workflow.add_edge(
    "research",
    "analyzer"
)

workflow.add_edge(
    "analyzer",
    "critic"
)

workflow.add_conditional_edges(
    "critic",
    route_after_critic,
    {
        "writer": "writer",
        "retry": "retry"
    }
)

workflow.add_edge(
    "retry",
    "research"
)

workflow.add_edge(
    "writer",
    END
)

app = workflow.compile()

print("===== HEARME MULTI-AGENT SYSTEM =====")

user_query = input(
    "\nEnter your company question: "
).strip()

initial_state = {
    "user_query": user_query,
    "retry_count": 0,
    "communication_log": []
}

result = app.invoke(
    initial_state
)

print("\n================================")
print("FINAL ANSWER")
print("================================")

print(
    result["final_answer"]
)

with open(
    "communication_log.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "HEARME MULTI-AGENT COMMUNICATION LOG\n\n"
    )

    file.write(
        f"User Request: {user_query}\n\n"
    )

    for entry in result[
        "communication_log"
    ]:

        file.write(
            f"[{entry['time']}] "
            f"{entry['agent']}\n"
        )

        file.write(
            entry["message"]
            + "\n\n"
        )

    file.write(
        "FINAL ANSWER\n"
    )

    file.write(
        result["final_answer"]
        + "\n"
    )

print(
    "\nCommunication log saved to "
    "communication_log.txt"
)