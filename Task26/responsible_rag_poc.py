import re

knowledge_base = [
    {
        "source": "Company Overview",
        "text": "HearMe is an AI-powered voice agent platform designed to automate customer communication."
    },
    {
        "source": "ASR Evaluation Policy",
        "text": "Automatic Speech Recognition performance is evaluated using Word Error Rate, Character Error Rate, and inference time."
    },
    {
        "source": "Customer Escalation Policy",
        "text": "Complex, sensitive, or unresolved customer issues must be escalated to a human customer support agent."
    },
    {
        "source": "RAG Documentation",
        "text": "Retrieval-Augmented Generation retrieves relevant approved company information before an AI response is generated."
    },
    {
        "source": "Privacy Policy",
        "text": "Sensitive customer information must not be exposed unnecessarily and should only be accessed when required for an authorized task."
    }
]

HIGH_RISK_TERMS = {
    "refund",
    "payment",
    "bank",
    "legal",
    "medical",
    "password",
    "account change"
}

def tokenize(text):
    return set(
        re.findall(
            r"\b[a-zA-Z]+\b",
            text.lower()
        )
    )

def redact_sensitive_data(text):
    text = re.sub(
        r"\b[\w\.-]+@[\w\.-]+\.\w+\b",
        "[REDACTED EMAIL]",
        text
    )

    text = re.sub(
        r"\b\d{10}\b",
        "[REDACTED PHONE]",
        text
    )

    text = re.sub(
        r"\b\d{12,16}\b",
        "[REDACTED NUMBER]",
        text
    )

    return text

def retrieve_information(question):
    question_words = tokenize(question)

    results = []

    for item in knowledge_base:
        document_words = tokenize(item["text"])

        score = len(
            question_words.intersection(
                document_words
            )
        )

        if score > 0:
            results.append({
                "source": item["source"],
                "text": item["text"],
                "score": score
            })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:2]

def requires_human_review(question):
    question_lower = question.lower()

    return any(
        term in question_lower
        for term in HIGH_RISK_TERMS
    )

def responsible_rag(question):
    safe_question = redact_sensitive_data(
        question.strip()
    )

    if not safe_question:
        return {
            "status": "rejected",
            "answer": "Please enter a valid question."
        }

    if requires_human_review(safe_question):
        return {
            "status": "human_review",
            "answer": (
                "This request may involve a sensitive or "
                "high-impact action and should be reviewed "
                "by an authorized human support agent."
            )
        }

    retrieved = retrieve_information(
        safe_question
    )

    if not retrieved:
        return {
            "status": "insufficient_information",
            "answer": (
                "I do not have enough verified company "
                "information to answer this question reliably."
            )
        }

    best_result = retrieved[0]

    return {
        "status": "grounded_answer",
        "answer": best_result["text"],
        "source": best_result["source"],
        "retrieval_score": best_result["score"]
    }

print("===== RESPONSIBLE AI + ADVANCED RAG POC =====")

while True:
    question = input(
        "\nEnter company question or type 'exit': "
    ).strip()

    if question.lower() == "exit":
        break

    result = responsible_rag(question)

    print("\nResult:")

    for key, value in result.items():
        print(f"{key}: {value}")