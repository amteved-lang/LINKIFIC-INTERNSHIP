from typing import TypedDict

HIGH_RISK_KEYWORDS = {
    "refund",
    "payment",
    "bank",
    "legal",
    "complaint",
    "password",
    "account change",
    "fraud",
    "cancel account"
}

class RoutingResult(TypedDict):
    query: str
    route: str
    reason: str
    requires_human: bool

def normalize_query(query: str) -> str:
    if not isinstance(query, str):
        raise TypeError("Query must be a string.")

    cleaned_query = query.strip().lower()

    if not cleaned_query:
        raise ValueError("Query cannot be empty.")

    return cleaned_query

def detect_high_risk_topic(query: str) -> str | None:
    for keyword in HIGH_RISK_KEYWORDS:
        if keyword in query:
            return keyword

    return None

def route_support_query(query: str) -> RoutingResult:
    cleaned_query = normalize_query(query)

    matched_keyword = detect_high_risk_topic(
        cleaned_query
    )

    if matched_keyword:
        return {
            "query": query.strip(),
            "route": "human_support",
            "reason": (
                f"Sensitive or high-impact topic detected: "
                f"{matched_keyword}"
            ),
            "requires_human": True
        }

    return {
        "query": query.strip(),
        "route": "ai_support",
        "reason": (
            "No sensitive or high-impact topic was detected."
        ),
        "requires_human": False
    }