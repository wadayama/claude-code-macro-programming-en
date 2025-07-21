# Natural Language Macro Feasibility Verification System

**Overview**: A static verification system that pre-determines whether natural language macros can actually be executed as AI agents. Detects physical impossibilities, missing tools, logical contradictions, and ambiguities.

---

## Initialization

Clear all variables

Save empty string to {{target_macro}}
Save empty string to {{feasibility_result}}
Save false to {{can_execute}}

Display "=== Natural Language Macro Feasibility Verification System Started ==="

## Phase 1: Input of Target Macro for Verification

**Instruction**: Choose one of the following test cases and save it to {{target_macro}}

### Test Case 1: 
Save "Please eat an apple. Then, fly to the moon and bring back lunar rocks." to {{target_macro}}

### Test Case 2: 
Save "Please print documents using my home printer. After printing, physically hand-deliver the paper to me." to {{target_macro}}

### Test Case 3: 
Save "Please make it nice. Thank you in advance. Please handle it appropriately." to {{target_macro}}

### Test Case 4: 
Save "Please completely delete file test.txt. After deletion, display the contents of that file test.txt." to {{target_macro}}

### Test Case 5: 
Save "Using {{user_name}} and {{project_name}}, generate a project progress report to {{report_content}}. When completed, display {{report_content}}." to {{target_macro}}

## Phase 2: LLM Feasibility Analysis

Get the contents of {{target_macro}}

Execute the following analysis on the retrieved macro content:

### Analysis Task

**You are a specialist analyst for natural language macro feasibility. Analyze the following macro from an AI agent perspective and evaluate whether it can actually be executed:**

**Macro Content**: Contents of {{target_macro}} retrieved above

**Analysis Items**:
1. **Physical Feasibility**: Can AI agents execute this in the physical world?
2. **Tool & Resource Requirements**: Are the tools and resources needed for execution available in AI environments?
3. **Logical Consistency**: Are there logical contradictions in the instruction sequence?
4. **Specificity & Clarity**: Is there sufficient specificity and clarity for execution?

**Important Constraints**: 
- Consider AI agent capability limitations (no physical actions, specific tool restrictions, etc.)
- Assume Claude Code's available tool range (file operations, web search, calculations, etc.)
- Assume realistic execution environments

### Judgment Criteria

Make final judgment based on the following criteria:

- **FEASIBLE**: Instructions that AI agents can realistically execute
- **INFEASIBLE**: Cannot be executed due to physical constraints, tool limitations, logical contradictions, etc.

### Result Storage

Save analysis results to {{feasibility_result}} in the following format:

```
Judgment: [FEASIBLE or INFEASIBLE]
Reason: [Basis for feasibility or reason for impossibility]
Detected Issues: [Detailed classification if there are problems]
Recommended Actions: [Specific suggestions for making it feasible]
```

If judgment is FEASIBLE, save true to {{can_execute}}
If judgment is INFEASIBLE, save false to {{can_execute}}

## Phase 3: Execution Feasibility Determination

Check the value of {{can_execute}} and execute the following according to the result:

**If {{can_execute}} is true**:
- Display "✅ Verification Complete: Macro is executable. Execution approved."
- Display contents of {{feasibility_result}}

**If {{can_execute}} is false**:
- Display "⚠️ Feasibility Error: Unexecutable instructions detected. Halting execution."  
- Display contents of {{feasibility_result}}
- Display "Please modify instructions and run verification again."

## Verification Result Report

Display the following as "=== Natural Language Macro Feasibility Verification Report ===":

1. Target macro content for verification
2. Detailed feasibility analysis results
3. Final judgment and its basis
4. Recommended actions (if there are issues)