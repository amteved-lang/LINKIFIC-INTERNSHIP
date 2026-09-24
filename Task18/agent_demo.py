query = input("Enter customer query: ")

if "refund" in query.lower():
    print("Tool Selected: Company Knowledge Base")
elif "order" in query.lower():
    print("Tool Selected: Customer Database")
else:
    print("Action: Escalate to Human Support")