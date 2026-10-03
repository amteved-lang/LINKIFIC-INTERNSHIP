# AI Provider Comparison

## Mini Practical

Comparison of:

- OpenAI
- Anthropic Claude
- Google Gemini
- Groq

based on:

- Cost
- Speed
- Accuracy / Capability

## Important Note

AI providers contain multiple models with different levels of cost and capability.

Therefore, this comparison uses representative production-oriented models rather than treating an entire provider as a single model.

## Models Compared

| Provider | Model |
|---|---|
| OpenAI | GPT-6 Luna |
| Anthropic | Claude Sonnet 5.5 |
| Google | Gemini 3.1 Flash-Lite |
| Groq | GPT-OSS 120B |

## Cost Comparison

| Provider / Model | Input per 1M Tokens | Output per 1M Tokens |
|---|---:|---:|
| OpenAI GPT-6 Luna | $0.10 | $0.50 |
| Claude Sonnet 5.5 | $2.00 | $10.00 |
| Gemini 3.1 Flash-Lite | $0.25 | $1.50 |
| Groq GPT-OSS 120B | $0.15 | $0.60 |

Token pricing alone does not represent the total cost of completing a task because models may use different numbers of reasoning and output tokens.

## Speed Comparison

Independent benchmarks indicate approximately:

| Model | Approximate Output Speed |
|---|---:|
| OpenAI GPT-6 Luna | ~130-138 tokens/sec |
| Claude Sonnet 5.5 | ~100-139 tokens/sec depending on effort |
| Gemini 3.1 Flash-Lite | ~291 tokens/sec |
| Groq GPT-OSS 120B | ~473 tokens/sec on Groq |

Actual performance can change depending on prompt size, reasoning settings, traffic, service tier and geographic location.

## Accuracy / Capability Comparison

There is no universal percentage that represents model accuracy across every application.

A useful external capability proxy is the Artificial Analysis Intelligence Index.

Representative results are approximately:

| Model | Intelligence Index |
|---|---:|
| Claude Sonnet 5.5 Max | 56 |
| OpenAI GPT-6 Luna Max | 38 |
| Gemini 3.1 Flash-Lite | 16 |
| GPT-OSS 120B High | 12 |

These scores should not be interpreted as literal percentages of correct answers.

Models can perform differently on coding, reasoning, multilingual tasks, retrieval, customer support and other specialized workloads.

## Practical Analysis

### OpenAI

GPT-6 Luna has extremely low token pricing and is designed for focused, high-volume workloads.

It can be useful where cost efficiency is important and requests do not always require the strongest frontier model.

### Claude

Claude Sonnet 5.5 is considerably more expensive than the cost-focused models in this comparison but provides much stronger capability on the selected intelligence benchmark.

It is suitable for more demanding reasoning, coding and agent workflows where model quality is more important than minimum token cost.

### Gemini

Gemini 3.1 Flash-Lite provides a strong combination of relatively low pricing and very high output speed.

It is designed for high-volume agentic tasks, translation and simpler data-processing workloads.

### Groq

Groq is particularly strong for inference speed.

GPT-OSS 120B running on Groq provides inexpensive inference and extremely high token generation speed.

This can make Groq attractive for latency-sensitive systems such as interactive assistants and voice applications.

## Summary by Requirement

Cost-sensitive high-volume workload:
OpenAI GPT-6 Luna is highly attractive based on the listed token price.

Very low-latency generation:
Groq is particularly attractive.

Balanced low-cost multimodal/high-volume workloads:
Gemini Flash-Lite is attractive.

More demanding reasoning and agentic work:
Claude Sonnet 5.5 provides much stronger capability in the benchmark used here.

## Conclusion

No provider is universally best.

The appropriate provider depends on:

Cost requirements
Latency requirements
Model capability
Context size
Multimodal requirements
Tool support
Security
Reliability
Geographic deployment
Expected request volume

Production AI systems should benchmark models using their own real application data before making a final provider decision.