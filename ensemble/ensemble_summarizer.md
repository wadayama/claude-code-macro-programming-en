# 🎯 Ensemble Summarization System - With Lie Detection

## System Initialization

Display "=== Ensemble Summarization System Starting ===".

## Complete Initialization (Clean Start)

Clear all variables.

Display "All variables have been cleared".

## Configuration Parameters

Save 0.3 to {{lie_probability}}.

Display "Lie probability: {{lie_probability}} (30%) has been set".

## Input Data Loading

Read the sample_article.md file.

Save the loaded content to {{input_text}}.

Display "Input text saved to {{input_text}}".

## Multi-Agent Summarization Execution

**⚠️ Important**: The summarizer_agent.md file is read-only. You can read its contents but must never modify it. Always save to new files in the agents/ folder.

Create the agents/ folder:
```bash
mkdir -p agents
```

**Use the Task tool to launch 3 agent processes in parallel:**

### Task 1: Execute Agent 1
1. Read the contents of summarizer_agent.md and replace all <<ID>> with "1", then save to agents/summarizer_agent_1.md
2. Execute the following command:
   ```bash
   cat agents/summarizer_agent_1.md | claude -p --dangerously-skip-permissions
   ```

### Task 2: Execute Agent 2
1. Read the contents of summarizer_agent.md and replace all <<ID>> with "2", then save to agents/summarizer_agent_2.md
2. Execute the following command:
   ```bash
   cat agents/summarizer_agent_2.md | claude -p --dangerously-skip-permissions
   ```

### Task 3: Execute Agent 3
1. Read the contents of summarizer_agent.md and replace all <<ID>> with "3", then save to agents/summarizer_agent_3.md
2. Execute the following command:
   ```bash
   cat agents/summarizer_agent_3.md | claude -p --dangerously-skip-permissions
   ```

Display "3 agent processes completed in parallel".

## Summary Results Collection

**Generated summary results**:

Retrieve {{summary_1}}.
Retrieve {{summary_2}}.
Retrieve {{summary_3}}.

Display "=== Each Agent's Summary Results ===".
Display "Agent 1: {{summary_1}}".
Display "Agent 2: {{summary_2}}".
Display "Agent 3: {{summary_3}}".

## Ensemble Judgment Execution

Display "=== Ensemble Judgment Starting ===".

### Pairwise Comparison Execution

**Comparison Pair 1**: Compare {{summary_1}} and {{summary_2}}.
- If content is essentially identical (important facts match): "Match"
- If clearly different facts are included: "Mismatch"

Save comparison result to {{pair_12_match}} ("Match" or "Mismatch").

**Comparison Pair 2**: Compare {{summary_2}} and {{summary_3}}.
- If content is essentially identical (important facts match): "Match"
- If clearly different facts are included: "Mismatch"

Save comparison result to {{pair_23_match}} ("Match" or "Mismatch").

**Comparison Pair 3**: Compare {{summary_1}} and {{summary_3}}.
- If content is essentially identical (important facts match): "Match"
- If clearly different facts are included: "Mismatch"

Save comparison result to {{pair_13_match}} ("Match" or "Mismatch").

### Judgment Results Display

Display "Pairwise comparison results:".
Display "  (1,2): {{pair_12_match}}".
Display "  (2,3): {{pair_23_match}}".
Display "  (1,3): {{pair_13_match}}".

## Final Judgment

Make the final judgment based on the values of {{pair_12_match}}, {{pair_23_match}}, {{pair_13_match}}:

### If {{pair_12_match}} is "Match"
Adopt {{summary_1}} as the final summary.
Display "🎯 Ensemble Judgment: Adopting Agent 1&2 summary".
Display "📝 Final Summary: {{summary_1}}".

### If {{pair_23_match}} is "Match"
Adopt {{summary_2}} as the final summary.
Display "🎯 Ensemble Judgment: Adopting Agent 2&3 summary".
Display "📝 Final Summary: {{summary_2}}".

### If {{pair_13_match}} is "Match"
Adopt {{summary_1}} as the final summary.
Display "🎯 Ensemble Judgment: Adopting Agent 1&3 summary".
Display "📝 Final Summary: {{summary_1}}".

### If all are "Mismatch"
Display "🚨 Ensemble Judgment: No matching summaries found".
Display "⛔ Summary output blocked due to lie detection".
Display "💡 Reason: All agents reported different content, making it impossible to identify a reliable summary".

## System Completion

Display "=== Ensemble Summarization System Completed ===".