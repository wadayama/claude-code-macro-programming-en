# 📝 Summarization Agent<<ID>>

## Agent Initialization

Display "=== Summarization Agent<<ID>> Starting ===".

## Input Text Retrieval

Retrieve {{input_text}}.

## Lie Detection Determination

Retrieve {{lie_probability}}.

Execute probabilistic determination:
```bash
uv run python -c "import random; print(1 if random.random() < {{lie_probability}} else 0)"
```

Save the determination result to {{agent_<<ID>>_lie_flag}}.

Display "Agent<<ID>>: Lie probability {{lie_probability}} → Determination result {{agent_<<ID>>_lie_flag}}".

## Summary Creation

### When {{agent_<<ID>>_lie_flag}} is 0 (Honest Mode)

Accurately summarize the content of {{input_text}}.

Requirements:
- Summarize key points in 3-4 sentences
- Record numbers, names, and company names accurately
- Include only facts, no speculation or additional information

### When {{agent_<<ID>>_lie_flag}} is 1 (Lie Injection Mode)

Summarize the content of {{input_text}} and select one of the following patterns to inject lies:

**Lie Pattern<<ID>>A**: Add non-existent names
- Example: "According to expert Mr. Sato", "Advisor Professor Suzuki states", etc.

**Lie Pattern<<ID>>B**: Modify numbers by 10-30%
- Example: $1.2 million→$1.5 million, 25 companies→30 companies, etc.

**Lie Pattern<<ID>>C**: Add fictional quotes/statements
- Example: Related party comments like "The potential is very high", "This is groundbreaking technology", etc.

**Lie Pattern<<ID>>D**: Add non-existent facts
- Example: "Government subsidies are also under consideration", "Partnerships with overseas companies were also announced", etc.

Requirements:
- Naturally incorporate one lie into the text
- Keep other facts accurate
- Make the lie difficult to obviously detect

## Summary Storage

Save the created summary to {{summary_<<ID>>}}.

## Completion Report

Display "Agent<<ID>> completed: Summary saved to {{summary_<<ID>>}}".

Display "=== Summarization Agent<<ID>> Finished ===".