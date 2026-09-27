# Function Calling Decision Matrix

## Objective

The decision matrix identifies which tool should be called for different user requests.

| No. | User Request | Selected Tool | Reason |
|---|---|---|---|
| 1 | Calculate 250 divided by 5 | Calculator Tool | Mathematical calculation is required |
| 2 | Search the web for recent AI developments | Web Search Tool | Current external information is required |
| 3 | Find customer ID 101 | Database Tool | Customer information is stored in the database |
| 4 | Read company documentation | File Reader Tool | Information must be read from a local document |
| 5 | What is the weather in Nagpur? | Weather Tool | Weather information is required |
| 6 | Send an email to customer support | Email Tool | Email communication is required |
| 7 | What is today's date? | Date Tool | Current date information is required |
| 8 | Analyze customer support CSV data | Data Analyzer Tool | Structured dataset analysis is required |
| 9 | What is HearMe? | Company Search Tool | The answer exists in company documentation |
| 10 | How is ASR performance evaluated? | Company Search Tool | Company-specific technical information is required |
| 11 | Calculate the customer resolution percentage | Calculator Tool / Data Analyzer Tool | Dataset values must first be analyzed and may then require calculation |
| 12 | Read support data and calculate resolution rate | File Reader → Data Analyzer | Multiple tools must be chained to complete the request |

## Conclusion

Function calling allows an AI system to select specialized tools depending on the user's request.

Tool selection helps improve reliability because different tasks are handled by functions designed specifically for those operations.