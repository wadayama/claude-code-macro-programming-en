# Natural Language Macro Programming Debugger Specification

This specification defines the detailed functionality and execution guidelines for debugging in natural language macro programming.

## 🔧 Debug Mode Syntax Definition

### Basic Debug Instructions
```
"Execute [processing content] in debug mode"
```

### Detail Level Specification
- **Simple Debug**: "Execute in simple debug mode"
- **Standard Debug**: "Execute in debug mode"
- **Detailed Debug**: "Execute in detailed debug mode"

### Element-Specific Debug
- **Variable Tracking**: "Execute while debug tracking variable {{name}}"
- **Conditional Branching**: "Execute while debugging conditional branching"
- **Error Details**: "Execute with detailed explanations when errors occur"

## 📋 Standard Output Format

### Basic Output Format
```
[DEBUG] Step [number]: [description of execution content]
[DEBUG] Variable State: {{variable_name}} = [current value]
[DEBUG] Decision Rationale: [reason for condition evaluation]
[DEBUG] Next Action: [next processing to execute]
```

### Variable Operation Output Example
```
[DEBUG] Step 1: Saving weather information to variable {{weather}}
[DEBUG] Execution Content: Retrieve today's weather via web search
[DEBUG] Variable State: {{weather}} = "Sunny, temperature 25°C, humidity 60%"
[DEBUG] Decision Rationale: Sunny → sun protection needed, 25°C → heat protection needed
[DEBUG] Next Action: Generate clothing suggestions based on {{weather}}
```

### Conditional Branching Output Example
```
[DEBUG] Step 2: Evaluating condition "{{score}} >= 80"
[DEBUG] Variable State: {{score}} = 85
[DEBUG] Condition Analysis: 85 >= 80 = true
[DEBUG] Decision Rationale: 85 is 80 or above, proceeding to high evaluation branch
[DEBUG] Branch Decision: Select excellent evaluation message generation route
[DEBUG] Next Action: Generate excellent evaluation message
```

### Compound Condition Processing Output Example
```
[DEBUG] Compound Condition Analysis:
- Condition A: {{weather}} == "rain" → "rain" == "rain" = true
- Condition B: {{temperature}} < 20 → 15 < 20 = true
- Condition C: {{plan}} == "outdoor" → "outdoor event" contains "outdoor" = true
[DEBUG] Compound Judgment: (A AND B AND C) = (true AND true AND true) = true
[DEBUG] Decision Rationale: All conditions satisfied, executing rainy weather outdoor countermeasure route
```

## 🎯 Detail Level Specifications

### Simple Debug Mode
- Display only important variable changes
- Report only major conditional branching results
- Minimize output volume

### Standard Debug Mode  
- Display all variable operations
- Explain detailed evaluation processes of conditional branching
- Explicitly show decision rationales and next actions

### Detailed Debug Mode
- Display intermediate calculation processes in detail
- Explain internal operations of error handling
- Report including performance information

## ⚠️ Error-Time Debug Output

### Standard Format for Error Occurrence
```
[DEBUG] Error Detection: [error overview]
[DEBUG] Error Details: [specific error content]
[DEBUG] Occurrence Location: Step [number] - [processing content]
[DEBUG] Variable State: [variable values at error occurrence]
[DEBUG] Cause Analysis: [estimated cause of error]
[DEBUG] Correction Suggestion: [proposed solution]
[DEBUG] Alternative Execution: [possible alternative processing]
```

### Error Handling Example
```
[DEBUG] Error Detection: Invalid budget value set
[DEBUG] Error Details: {{budget}} = -50000 (negative value is invalid)
[DEBUG] Occurrence Location: Step 3 - Budget data validation processing
[DEBUG] Variable State: {{budget}} = -50000, {{required_qty}} = 0
[DEBUG] Cause Analysis: Insufficient input data validity check
[DEBUG] Correction Suggestion: Correct budget to positive value (e.g., 150,000 yen)
[DEBUG] Alternative Execution: Continue processing with default budget of 100,000 yen
```

## 🔍 Runtime Operation Specifications

### Debug Information Generation Principles
1. **Transparency**: Explicitly show all decision processes
2. **Traceability**: Completely record variable transitions
3. **Ease of Understanding**: Explanations understandable by non-technical users
4. **Practicality**: Provide information directly useful for problem solving

## 📚 Usage Guidelines

### Debug Mode Execution Steps
1. **Load debugger.md**: Enable debug functionality
2. **Execute Debug Instructions**: Specify appropriate detail level
3. **Analyze Output**: Identify problems based on debug information

### Usage Precautions
- Debug output may become voluminous
- Pay attention to output content when confidential information is involved
- Particularly useful for long-term workflows