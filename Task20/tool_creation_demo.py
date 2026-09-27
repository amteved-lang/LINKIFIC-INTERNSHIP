import csv
from datetime import datetime
from pathlib import Path

customer_database = {
    "101": {"name": "Rahul", "plan": "Premium", "status": "Active"},
    "102": {"name": "Priya", "plan": "Standard", "status": "Active"},
    "103": {"name": "Aman", "plan": "Basic", "status": "Inactive"}
}

def calculator_tool(a, b, operation):
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            if b == 0:
                return "Error: Division by zero is not allowed."
            return a / b
        return "Error: Unsupported operation."
    except Exception as error:
        return f"Calculator Error: {error}"

def web_search_tool(query):
    try:
        return f"Web Search Tool selected for query: {query}"
    except Exception as error:
        return f"Web Search Error: {error}"

def database_tool(customer_id):
    try:
        customer = customer_database.get(customer_id)

        if customer:
            return customer

        return "Customer not found."
    except Exception as error:
        return f"Database Error: {error}"

def file_reader_tool(filename):
    try:
        path = Path(filename)

        if not path.exists():
            return "Error: File does not exist."

        return path.read_text(encoding="utf-8")

    except Exception as error:
        return f"File Reader Error: {error}"

def weather_tool(city):
    try:
        return f"Weather Tool selected for city: {city}"
    except Exception as error:
        return f"Weather Error: {error}"

def email_tool(receiver, subject, message):
    try:
        return {
            "status": "Demo Email Prepared",
            "receiver": receiver,
            "subject": subject,
            "message": message
        }
    except Exception as error:
        return f"Email Error: {error}"

def date_tool():
    try:
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    except Exception as error:
        return f"Date Tool Error: {error}"

def data_analyzer_tool(filename):
    try:
        rows = []

        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                rows.append(row)

        if not rows:
            return "Dataset is empty."

        total_queries = sum(int(row["Queries"]) for row in rows)
        total_resolved = sum(int(row["Resolved"]) for row in rows)

        resolution_rate = (
            total_resolved / total_queries
        ) * 100

        return {
            "total_employees": len(rows),
            "total_queries": total_queries,
            "resolved_queries": total_resolved,
            "resolution_rate": round(resolution_rate, 2)
        }

    except Exception as error:
        return f"Data Analyzer Error: {error}"

def select_tool(request):
    text = request.lower()

    if any(word in text for word in ["calculate", "add", "multiply", "divide"]):
        return "Calculator Tool"

    elif any(word in text for word in ["search web", "internet", "latest"]):
        return "Web Search Tool"

    elif any(word in text for word in ["customer", "account", "database"]):
        return "Database Tool"

    elif any(word in text for word in ["read file", "document", "file"]):
        return "File Reader Tool"

    elif any(word in text for word in ["weather", "temperature"]):
        return "Weather Tool"

    elif any(word in text for word in ["email", "mail"]):
        return "Email Tool"

    elif any(word in text for word in ["date", "time", "today"]):
        return "Date Tool"

    elif any(word in text for word in ["analyze", "csv", "dataset"]):
        return "Data Analyzer Tool"

    return "No suitable tool found"

print("===== AI TOOL CREATION DEMO =====")

print("\nCalculator Tool:")
print(calculator_tool(25, 5, "divide"))

print("\nWeb Search Tool:")
print(web_search_tool("Latest developments in AI agents"))

print("\nDatabase Tool:")
print(database_tool("101"))

print("\nFile Reader Tool:")
print(file_reader_tool("company_documentation.txt"))

print("\nWeather Tool:")
print(weather_tool("Nagpur"))

print("\nEmail Tool:")
print(
    email_tool(
        "support@example.com",
        "Customer Query",
        "Please review the customer support request."
    )
)

print("\nDate Tool:")
print(date_tool())

print("\nData Analyzer Tool:")
print(data_analyzer_tool("sample_data.csv"))

print("\n===== FUNCTION CALLING DECISION =====")

requests = [
    "Calculate 25 divided by 5",
    "Search web for latest AI news",
    "Find customer 101 in database",
    "Read company documentation file",
    "What is the weather in Nagpur?",
    "Send an email to customer support",
    "What is today's date?",
    "Analyze the CSV dataset"
]

for request in requests:
    print("\nRequest:", request)
    print("Selected Tool:", select_tool(request))