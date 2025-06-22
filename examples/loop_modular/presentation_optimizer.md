# Presentation Quality Optimization System (Intermediate)

**Overview**: Advanced Loop & Modular Programming system that iteratively improves presentation materials across multiple evaluation axes. Evaluates quality along 3 axes (content, structure, presentation) and continuously optimizes until goals are achieved.

**Learning Objectives**: 
- Management of multiple state variables
- Composite conditional termination assessment
- Loop control with safety mechanisms
- Advanced modular design

---

## Initial Setup

Set the presentation theme as "Future of AI Technology" and save to {{theme}}.

Set the quality scores as follows:
- Set content quality to 40 and save to {{content_score}}
- Set structure quality to 35 and save to {{structure_score}}
- Set presentation quality to 30 and save to {{presentation_score}}

Set improvement iteration to 0 and save to {{iteration}}.
Set maximum improvement iterations to 10 and save to {{max_iterations}}.
Set improvement history to empty and save to {{improvement_history}}.

Display "=== Presentation Quality Optimization System Started ===".
Display "Theme: {{theme}}".

## Initial Presentation Content Recording

As a baseline before improvement, please generate initial presentation content corresponding to the current quality level (content 40, structure 35, presentation 30) and save to {{initial_presentation}}:

Create presentation content about "{{theme}}" with the following quality levels:
- Basic information only (content quality level 40)
- Simple 3-part structure (structure quality level 35)
- Plain and basic expressions (presentation quality level 30)

Create this including the actual slide structure and key points for each slide.

## Quality Optimization Loop

Repeat the following until ALL of the following conditions are met:
- {{content_score}} reaches 80 or above
- {{structure_score}} reaches 80 or above  
- {{presentation_score}} reaches 80 or above

**Safety mechanism**: If {{iteration}} reaches {{max_iterations}}, terminate the loop.

Add 1 to {{iteration}}.

Display "=== Optimization Cycle {{iteration}} Started ===".

Execute quality_analyzer.md.

Display current overall quality status:
- Overall progress: Calculate average of three scores
- Remaining gap to target (80 points)
- Priority axis for next improvement

Display "=== Optimization Cycle {{iteration}} Completed ===".

If termination conditions are not met, continue to next cycle.

## Final Quality Evaluation

Display "=== Final Quality Evaluation ===".

Please evaluate the final quality achievement:
- Final content quality: {{content_score}} (improvement from initial 40)
- Final structure quality: {{structure_score}} (improvement from initial 35)  
- Final presentation quality: {{presentation_score}} (improvement from initial 30)
- Total improvement iterations: {{iteration}}
- Improvement trajectory: {{improvement_history}}

## Optimized Presentation Generation

Based on the final quality scores, please generate the optimized presentation content and save to {{final_presentation}}:

Create presentation content about "{{theme}}" reflecting the achieved quality levels:
- Rich, detailed content (content quality {{content_score}} level)
- Sophisticated logical structure (structure quality {{structure_score}} level)
- Professional, engaging presentation (presentation quality {{presentation_score}} level)

Create including actual slide structure and detailed content for each slide.

## Improvement Impact Analysis

Please compare {{initial_presentation}} and {{final_presentation}} and analyze the improvement impact:

1. **Content Enhancement**: How did content depth and accuracy improve?
2. **Structure Improvement**: How did logical flow and organization improve?
3. **Presentation Enhancement**: How did clarity and engagement improve?
4. **Overall Value**: What is the measurable improvement in presentation effectiveness?

Display optimization success summary and recommendations for future presentations.

---

**Advanced Loop & Modular Programming Features**:
1. **Multi-variable Convergence**: Loop continues until ALL quality targets are met
2. **Safety Mechanisms**: Maximum iteration limit prevents infinite loops
3. **Complex State Management**: Multiple scores and history tracking across iterations
4. **Comparative Analysis**: Before/after comparison of actual presentation content
5. **Adaptive Optimization**: Each cycle builds upon previous improvements through modular processing

This intermediate example demonstrates how Loop & Modular Programming can handle sophisticated optimization workflows with multiple convergence criteria, safety mechanisms, and comprehensive quality tracking.