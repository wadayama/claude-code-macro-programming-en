# 🎌 Haiku Generation Multi-Agent System

## Complete Initialization (Clean Start)

Clear all variables
Delete all files in agents/ folder
Clear all TODO lists

## System Configuration

Set {{agent_count}} to 5.

Display "=== Haiku Generation Multi-Agent System Start ===".

## Theme Generation

Generate {{agent_count}} creative and unusual haiku themes. Focus on unique and interesting concepts rather than seasonal or natural elements.

Output each theme in the following format:
1. [Theme1]
2. [Theme2]
(Continue up to {{agent_count}} themes)

Output only the themes, no additional explanation needed.

## Theme Distribution

Distribute the generated themes to each agent:

Specific examples:
- Save the 1st theme to {{agent_1_theme}}
- Save the 2nd theme to {{agent_2_theme}}

Generalization: For the 3rd and subsequent themes, use {{agent_N_theme}} format (N is number 3,4,5...) and continue up to {{agent_count}} themes

Save all themes to {{themes}}.

## Multi-Agent Haiku Generation

**⚠️ Important Notice**: The agent.md file is read-only. While you can read its contents, you must never modify or overwrite it. Always save to new files in the agents/ folder.

**Use Task tool to launch {{agent_count}} agent processes in parallel:**

Execute {{agent_count}} Tasks in parallel with the following pattern:

Specific examples:
### Task 1: Agent 1 Execution
1. Read agent.md content in read-only mode, replace all <<ID>> with "1" and save to agents/agent_1.md
2. Then execute the following command:
   cat agents/agent_1.md | claude -p --dangerously-skip-permissions 

### Task 2: Agent 2 Execution
1. Read agent.md content in read-only mode, replace all <<ID>> with "2" and save to agents/agent_2.md
2. Then execute the following command:
   cat agents/agent_2.md | claude -p --dangerously-skip-permissions 

Generalization: Task 3 and subsequent tasks follow the same pattern, replacing <<ID>> with corresponding numbers and executing in parallel up to {{agent_count}} tasks.

Display "{{agent_count}} agent processes completed in parallel."

## Haiku Evaluation and Selection

Evaluate the collected haiku and select the most unusual and impressive one:

**Generated Themes**: {{themes}}

**Haiku Candidates**:
Evaluate {{agent_count}} haiku with the following pattern:

Specific examples:
1. {{agent_1_haiku}}
2. {{agent_2_haiku}}

Generalization: For the 3rd and subsequent haiku, use {{agent_N_haiku}} format (N is number 3,4,5...) and continue up to {{agent_count}} haiku.

Evaluation criteria:
- Originality and unusualness
- Beauty of poetic expression
- Strength of impact

Exclude empty results from evaluation.

Select the most excellent haiku and display the evaluation results in the following format:
**Best Haiku**: [Copy the selected haiku exactly]
**Selection**: Haiku[number]
**Reason**: [Specific reason in 1-2 sentences]

Save this evaluation result (all three items: best haiku, selection, and reason) to {{best_selection}}.

Display "=== Haiku Generation Multi-Agent System Complete ===".