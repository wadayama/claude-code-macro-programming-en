# Quality Analysis & Improvement Module

**Overview**: Core processing module for presentation quality optimization system. Independently analyzes content, structure, and presentation along 3 axes and executes improvement processes suited to each axis.

**Variable Management**:
- `{{content_score}}`: Content quality score (reference & update)
- `{{structure_score}}`: Structure quality score (reference & update)
- `{{presentation_score}}`: Presentation quality score (reference & update)
- `{{improvement_history}}`: Improvement history (append)
- `{{iteration}}`: Current improvement iteration (reference only)
- `{{theme}}`: Presentation theme (reference only)

---

## Current Quality Analysis

Analyze the current quality situation:

Display "--- Quality Analysis Cycle {{iteration}} ---".

Display the current scores:
- Content quality: {{content_score}} points
- Structure quality: {{structure_score}} points
- Presentation quality: {{presentation_score}} points

Please identify the axis most in need of improvement and determine improvement strategy.

## Content Quality Improvement

Execute content improvement based on the value of {{content_score}}:

If {{content_score}} is less than 60:
→ Display "Executing content foundation strengthening"
→ Process as "Clarifying core concepts of {{theme}} and building logical structure"
→ Add 12 to {{content_score}}
→ Append "Content foundation strengthening: +12 points" to {{improvement_history}}

If {{content_score}} is 60 or more but less than 75:
→ Display "Executing content deepening improvement"
→ Process as "Adding detailed analysis and concrete examples for {{theme}}"
→ Add 9 to {{content_score}}
→ Append "Content deepening improvement: +9 points" to {{improvement_history}}

If {{content_score}} is 75 or more:
→ Display "Executing content refinement"
→ Process as "Integrating latest insights and unique perspectives on {{theme}}"
→ Add 6 to {{content_score}}
→ Append "Content refinement: +6 points" to {{improvement_history}}

## Structure Quality Improvement

Execute structure improvement based on the value of {{structure_score}}:

If {{structure_score}} is less than 60:
→ Display "Executing basic structure design"
→ Process as "Optimizing basic structure of introduction, main body, and conclusion"
→ Add 11 to {{structure_score}}
→ Append "Basic structure design: +11 points" to {{improvement_history}}

If {{structure_score}} is 60 or more but less than 75:
→ Display "Executing structure flow improvement"
→ Process as "Improving logical connections and flow between sections"
→ Add 8 to {{structure_score}}
→ Append "Structure flow improvement: +8 points" to {{improvement_history}}

If {{structure_score}} is 75 or more:
→ Display "Executing structure refinement"
→ Process as "Applying structural techniques for audience attention maintenance and comprehension facilitation"
→ Add 5 to {{structure_score}}
→ Append "Structure refinement: +5 points" to {{improvement_history}}

## Presentation Quality Improvement

Execute presentation improvement based on the value of {{presentation_score}}:

If {{presentation_score}} is less than 60:
→ Display "Executing basic presentation improvement"
→ Process as "Improving to expressions emphasizing clarity and comprehensibility"
→ Add 13 to {{presentation_score}}
→ Append "Basic presentation improvement: +13 points" to {{improvement_history}}

If {{presentation_score}} is 60 or more but less than 75:
→ Display "Executing presentation appeal enhancement"
→ Process as "Strengthening expression techniques and visual elements that capture audience interest"
→ Add 10 to {{presentation_score}}
→ Append "Presentation appeal enhancement: +10 points" to {{improvement_history}}

If {{presentation_score}} is 75 or more:
→ Display "Executing presentation completion improvement"
→ Process as "Applying professional-level expression techniques"
→ Add 7 to {{presentation_score}}
→ Append "Presentation completion improvement: +7 points" to {{improvement_history}}

## Improvement Results Verification

Display the post-improvement quality scores:
- Content quality: {{content_score}} points (display improvement effect)
- Structure quality: {{structure_score}} points (display improvement effect)
- Presentation quality: {{presentation_score}} points (display improvement effect)

Display "Quality improvement cycle {{iteration}} completed".

If there are axes that should be prioritized in the next improvement, please present them as recommendations.

---

**Advanced Modular Design Features**:
1. **Multi-dimensional Processing**: Independent improvement logic for 3 quality axes
2. **Adaptive Scoring**: Different improvement increments based on current quality levels
3. **Historical Tracking**: Comprehensive logging of all improvement actions
4. **Strategic Analysis**: Identification of priority areas for future improvements
5. **Scalable Architecture**: Easy to extend with additional quality dimensions

This module demonstrates sophisticated modular design where complex multi-dimensional quality improvement is handled through structured, reusable logic that maintains state and provides strategic guidance.