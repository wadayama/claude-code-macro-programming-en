# Code Creation & Review Collaboration System (SQLite Version Orchestrator)

## System Overview
Expert collaboration system where Python code creation and review are processed by two specialized agents in relay format
Supports high-speed and secure variable management utilizing SQLite variable management system

## Execution Flow
Code Creation → Code Review → Final Evaluation Report

## Initialization

### System State Reset
Please clear all variables

### Task Theme Setting
Save "Password Strength Checker" to {{task_theme}}

"=== SQLite Version Code Creation & Review Collaboration System Started ===" display this message
"Task Theme: {{task_theme}}" retrieve and display this

## Specialized Agent Execution Phase

### Phase 1: Code Creation Agent Execution
Display "--- Phase 1: Code Creation Agent Running ---"

Execute the code creation agent:
```
cat agents/code_writer.md | claude -p --dangerously-skip-permissions
```

### Phase 2: Code Review Agent Execution  
Display "--- Phase 2: Code Review Agent Running ---"

Execute the code review agent:
```
cat agents/code_reviewer.md | claude -p --dangerously-skip-permissions
```

## Final Results Display

### Display Created Code
Display "=== Created Python Code ==="
Retrieve and display {{generated_code}}

### Display Review Report
Display "=== Code Review Report ==="
Retrieve and display {{review_report}}

### System Completion Report
Display "=== SQLite Version Code Creation & Review Collaboration System Completed ==="

## Variable Monitoring
To monitor variable state during system execution, run the following in a separate terminal:
```
uv run python watch_variables.py --continuous
```

## Error Handling

When problems occur in each phase:
1. Save error content to {{error_log}}
2. Execute alternative processing if possible
3. For critical errors, stop processing and request human intervention