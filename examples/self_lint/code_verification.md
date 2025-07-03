# Code Verification System (Self-Lint Basic)

**Overview**: Self-verification system that automatically performs security, syntax, and quality checks before macro execution. Implements preventive quality management by stopping execution when issues are detected and providing fix recommendations.

---

## Complete Initialization (Clean Start)

Delete variables.json if it exists
Clear all TODO lists

Display "=== Code Verification System Started ===".

## Verification Rule Configuration

Create the following structure in variables.json:

```json
{
  "target_macro": "",
  "lint_result": {},
  "verification_log": []
}
```

**Important**: For subsequent code verification, automatically apply the following rules:

**1. Security Check**: Detection of dangerous commands (rm, sudo, chmod, etc.)
**2. Variable Integrity**: Verification of undefined variable references and circular references  
**3. Error Handling**: Presence of safety mechanisms like Try-Catch, Human-in-the-Loop, etc.

## Phase 1: Verification Target Macro Setup

### Presentation of Problematic Macro Example

Save the following macro to {{target_macro}}:

```markdown
## Dangerous File Processing Macro (For Verification)
Execute sudo rm -rf {{user_folder}}/*.
Display the value of {{undefined_variable}}.
Retrieve data from external API using {{secret_key}}.
```

### Verification Target Confirmation

Display the contents of {{target_macro}}

## Phase 2: Automated Verification Execution

### Security, Syntax, and Quality Checks

Apply the declared verification rules to the above {{target_macro}} and save to {{lint_result}} in the following format:

```json
{
  "security_issues": ["List of detected security issues"],
  "syntax_issues": ["List of detected syntax issues"], 
  "quality_issues": ["List of detected quality issues"],
  "severity": "error|warning|info",
  "safe_to_proceed": false,
  "recommended_fixes": ["List of fix recommendations"]
}
```

### Verification Log Recording

Record the verification process in {{verification_log}}:
- Execution status of each check item
- Details of issue detection
- Rationale for decisions

## Phase 3: Result Evaluation and Response

### Conditional Execution Control

Based on the safe_to_proceed value in {{lint_result}}:

**If safe_to_proceed is false**:
- Display "⚠️ Verification Error: Stopping macro execution"
- Display problem details from {{lint_result}}
- Display fix recommendations

**If safe_to_proceed is true**:
- Display "✅ Verification Complete: Macro is executable"

### Verification Results Display

Display the following as "=== Verification Results Report ===":
1. Details of detected issues
2. Rationale for severity assessment
3. Recommended corrective actions

### Learning Value Explanation

Display the following:
"This self-verification enables early detection of dangerous commands, prevention of variable errors, and early identification of quality issues. As a metaprogramming practice, it demonstrates the effectiveness of code that reads code."