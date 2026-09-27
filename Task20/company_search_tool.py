from pathlib import Path
import re

def company_search_tool(query):
    try:
        path = Path("company_documentation.txt")

        if not path.exists():
            return {
                "success": False,
                "error": "Company documentation file not found."
            }

        document = path.read_text(
            encoding="utf-8"
        ).strip()

        if not document:
            return {
                "success": False,
                "error": "Company documentation is empty."
            }

        sections = [
            section.strip()
            for section in document.split("\n")
            if section.strip()
        ]

        query_words = set(
            re.findall(
                r"[a-zA-Z]+",
                query.lower()
            )
        )

        best_section = None
        best_score = 0

        for section in sections:

            section_words = set(
                re.findall(
                    r"[a-zA-Z]+",
                    section.lower()
                )
            )

            score = len(
                query_words.intersection(
                    section_words
                )
            )

            if score > best_score:
                best_score = score
                best_section = section

        if best_section is None:
            return {
                "success": False,
                "answer": "No relevant company information was found."
            }

        return {
            "success": True,
            "query": query,
            "retrieved_information": best_section,
            "matching_score": best_score
        }

    except Exception as error:
        return {
            "success": False,
            "error": str(error)
        }

print("===== HEARME COMPANY SEARCH TOOL =====")

while True:

    query = input(
        "\nEnter company question or type 'exit': "
    ).strip()

    if query.lower() == "exit":
        break

    if not query:
        print("Please enter a valid question.")
        continue

    result = company_search_tool(query)

    print("\nTool Result:")
    print(result)