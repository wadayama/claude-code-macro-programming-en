# Macro Programming Features Guide

This file describes how to use macro programming features in Claude Code.

## Variable System

### Basic Syntax
- **Variable Reference**: `{{variable_name}}`
- **Variable Storage**: "Save ... to {{variable_name}}"

### Usage Examples
```
# Storage example
"Save 3 key points for Python beginners to {{basics}}"

# Reference example
"Create a learning plan based on {{basics}}"
```

## Conditional Branching

### Basic Syntax
Use natural language conditional instructions:
- "If..."
- "Depending on..."
- "When..."
- "According to..."

### Usage Examples
```
"If {{user_level}} is beginner, suggest basic course; if advanced, suggest advanced course"
"Choose appropriate tech stack according to {{project_type}}"
```

## Persistence Features

### Basic Syntax
- **Persistent Storage**: "Save {{variable_name}} to filename.json for persistence"
- **File Loading**: "Load filename.json and set to {{variable_name}}"

### Usage Examples
```
# Persistent storage
"Save {{project_config}} to config.json for persistence"

# File loading
"Load config.json and set to {{saved_config}}"
```

## External Module Execution

### Basic Syntax
- **Module Execution**: "Execute filename.md"

### Usage Examples
```
"Execute data_analysis_workflow.md"
"Execute setup_instructions.md"
```

## Tool Usage

### Natural Language Instructions
You can instruct tool usage with natural language like:

- **Web Search**: "Search the web for", "Look up..."
- **File Operations**: "Read the file", "Edit..."
- **Task Management**: "Use TODO tool", "Add task"
- **Git Operations**: "Commit", "Create branch"
- **Execution**: "Run...", "Execute tests"

### Usage Examples
```
"Search the web for latest AI technologies and save to {{ai_trends}}"
"Read package.json file and check dependencies"
"Use TODO tool to organize today's tasks"
```

## Notes

- Variable names must be enclosed in `{{}}`
- Use appropriate file extensions (.json, .md, etc.) for persistent files