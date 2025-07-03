# Ambiguous Request Interpretation System (Conditional Execution - Intermediate)
# Natural Language Ambiguity Fallback Experience

## Complete Initialization (Clean Start)

Delete variables.json if it exists
Clear all TODO lists

Display "=== Ambiguous Request Interpretation System Started ===".

## Ambiguous Request Input (Utilizing Natural Language Ambiguity)
Please input a research request using **intentionally ambiguous expressions** like the following:

**Examples**:
- "Research about AI"
- "Want to know about educational impact"
- "Tell me the latest trends"
- "I need detailed information"
- "More about that"

Save your ambiguous request to {{user_request}}.

## Ambiguity Level Assessment & Interpretation
Please assess the ambiguity level of {{user_request}} and evaluate the following items:
- Target clarity (about what?)
- Scope clarity (how detailed?)
- Context presence (what prerequisites?)

Save the assessment results to {{ambiguity_level}} and interpreted content to {{interpretation}}.

## Ambiguity-Based Fallback Execution
Based on {{ambiguity_level}} and {{interpretation}}, execute the following ambiguity fallback strategy:

### High Ambiguity (unclear target & scope)
If {{user_request}} is like "Research about AI" or "Tell me in detail":
→ Execute as "Researching 'ChatGPT's Impact on Education' as the most likely interpretation" and save to {{research_result}}
→ Record "This is a high-confidence guess interpretation. Please clarify your request if you had different intentions" to {{uncertainty_note}}

### Moderate Ambiguity (partially clear)
If {{user_request}} is like "Want to know about educational impact" or "Tell me the latest trends":
→ Execute as "Interpreting from context as 'Latest Impact of AI Technology on Education' for research" and save to {{research_result}}
→ Record "Includes partial assumptions. Precision can be improved with more specific requests" to {{interpretation_note}}

### Minor Ambiguity (mostly clear)
If {{user_request}} is like "Latest information about ChatGPT's impact on education":
→ Execute research definitively as a clear request and save to {{research_result}}
→ Record "Processed as a clear request" to {{confidence_note}}

### Incomprehensible Level (extreme ambiguity)
If {{user_request}} is like "About that" or "The previous one" with complete lack of context:
→ Execute as "Providing overview of general AI education topics due to insufficient context" and save to {{fallback_result}}
→ Record "Providing generic information due to interpretation difficulty. Re-input of specific request is recommended" to {{clarification_request}}

## Experience & Evaluation of Ambiguity Processing Results
Confirm the following and experience natural language ambiguity fallback first-hand:

1. **Inference Validity**: Whether {{interpretation}} matched your intentions
2. **Fallback Value**: Whether {{research_result}} had useful value despite ambiguity
3. **Transparency**: Whether speculative parts were clearly indicated through {{uncertainty_note}}, {{interpretation_note}}, etc.
4. **Improvement Potential**: How results would improve with clearer requests

## 【Experiment】Comparative Experience with Different Ambiguity Levels
Please try the following to experience the effectiveness of ambiguity fallback:

1. **More ambiguous requests**: Re-run the above with more ambiguous inputs and experience speculative processing
2. **Clearer requests**: Re-run with more explicit requests and confirm quality improvements
3. **Multiple ambiguous requests**: Run with various ambiguous requests and verify consistency of inferences

