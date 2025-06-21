# 🎌 Haiku Generation Multi-Agent System

## Theme Generation
Please generate 4 creative and unusual haiku themes. Focus on unique and intriguing concepts rather than seasonal or natural elements.

Output each theme in the following format:
1. [Theme 1]
2. [Theme 2] 
3. [Theme 3]
4. [Theme 4]

Output only the themes, no additional explanations needed. Please save the results to {{themes}}.

## Parallel Haiku Creation

**Please execute the following 4 tasks in parallel using the Task tool:**

### Task 1: First Theme Haiku
Based on the first theme in {{themes}}, please create a haiku. Follow the 5-7-5 syllable structure and express the strangeness and uniqueness of the theme. Use poetic and impactful words.

Output only the haiku, no additional explanations needed. Please save the result to {{haiku_1}}.

### Task 2: Second Theme Haiku
Based on the second theme in {{themes}}, please create a haiku. Follow the 5-7-5 syllable structure and express the strangeness and uniqueness of the theme. Use poetic and impactful words.

Output only the haiku, no additional explanations needed. Please save the result to {{haiku_2}}.

### Task 3: Third Theme Haiku
Based on the third theme in {{themes}}, please create a haiku. Follow the 5-7-5 syllable structure and express the strangeness and uniqueness of the theme. Use poetic and impactful words.

Output only the haiku, no additional explanations needed. Please save the result to {{haiku_3}}.

### Task 4: Fourth Theme Haiku
Based on the fourth theme in {{themes}}, please create a haiku. Follow the 5-7-5 syllable structure and express the strangeness and uniqueness of the theme. Use poetic and impactful words.

Output only the haiku, no additional explanations needed. Please save the result to {{haiku_4}}.

## Haiku Evaluation and Selection
Please evaluate the following haiku and select the most unusual and impactful one:

**Generated Themes**: {{themes}}

**Haiku Candidates**:
1. {{haiku_1}}
2. {{haiku_2}}
3. {{haiku_3}}
4. {{haiku_4}}

Evaluation Criteria:
- Originality and strangeness
- Beauty of poetic expression
- Strength of impact

Please respond in the following format:
**Best Haiku**: [Copy the selected haiku exactly]
**Selection**: Haiku [number]
**Reason**: [Specific reason in 1-2 sentences]

Please save the result to {{best_selection}}.

## Final Report
Please display a comprehensive summary of the haiku generation process.

**Generated Themes**: {{themes}}

**All Created Haiku**:
1. {{haiku_1}}
2. {{haiku_2}}
3. {{haiku_3}}
4. {{haiku_4}}

**Final Selection Result**: {{best_selection}}

---

## System Architecture Notes

This haiku generation system demonstrates several key Natural Language Macro Programming patterns:

### 1. Sequential Pipeline Pattern
- Theme generation → Parallel haiku creation → Evaluation → Final report
- Clear dependency chain with variable passing between stages

### 2. Parallel Processing Pattern
- Four haiku creation tasks executed simultaneously
- Efficient utilization of Claude Code's parallel processing capabilities

### 3. Variable Management
- `{{themes}}` - Stores generated themes for distribution to parallel tasks
- `{{haiku_1}}` through `{{haiku_4}}` - Individual haiku storage
- `{{best_selection}}` - Final evaluation results

### 4. Task Decomposition
- Complex creative process broken into manageable subtasks
- Each task has clear inputs, outputs, and success criteria

This example showcases how natural language instructions can orchestrate sophisticated multi-agent workflows while maintaining simplicity and readability.