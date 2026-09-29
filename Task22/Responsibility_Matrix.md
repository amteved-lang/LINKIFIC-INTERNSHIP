# Multi-Agent Responsibility Matrix

## Project

HearMe Multi-Agent Research Assistant

## Objective

The objective of the system is to divide a complex research task among multiple specialized AI agents.

Each agent performs a specific responsibility and communicates through a shared workflow state.

## Responsibility Matrix

| Agent | Role | Input | Output | Dependencies | Communication Flow |
|---|---|---|---|---|---|
| Coordinator Agent | Controls the overall workflow and assigns tasks | User query | Task plan and final response | All other agents | User → Coordinator → Agents |
| Research Agent | Finds relevant information from company documents and knowledge sources | Research task | Retrieved information | Coordinator | Coordinator → Research Agent → Analyzer |
| Analyzer Agent | Examines retrieved information and identifies important findings | Research results | Structured analysis | Research Agent | Research Agent → Analyzer → Critic |
| Critic Agent | Checks accuracy, relevance, completeness, and possible issues | Analysis | Approved result or feedback | Analyzer | Analyzer → Critic |
| Writer Agent | Converts approved information into a clear final response | Approved analysis | Final written answer | Critic | Critic → Writer → Coordinator |

## Shared State

The agents share information through a common state.

The shared state can contain:

- User Query
- Research Plan
- Retrieved Information
- Analysis
- Critic Feedback
- Approval Status
- Draft Response
- Final Response
- Error Information

## Communication

The Coordinator Agent controls the workflow.

The Research Agent sends information to the Analyzer.

The Analyzer sends structured findings to the Critic.

The Critic decides whether the information is sufficient.

If improvements are required, feedback is sent back to the Analyzer or Research Agent.

If the result is approved, it is passed to the Writer Agent.

The Writer produces the final response and sends it to the Coordinator.

## Conclusion

The responsibility matrix ensures that every AI agent has a clearly defined task, input, output, dependency, and communication path.