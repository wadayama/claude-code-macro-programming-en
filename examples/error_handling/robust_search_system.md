# Robust Information Collection System (Error Handling Basic)

**Overview**: Latest AI technology trend research system via web search integrated with error handling functionality. Implements preventive quality management through Try-Catch-Finally and Graceful Degradation for robust system design that assumes failure.

---

## Complete Initialization (Clean Start)

Delete variables.json if it exists
Clear all TODO lists

Display "=== Robust Information Collection System Started ===".

## Error Handling Rule Configuration

Create the following structure in variables.json:

```json
{
  "search_query": "",
  "search_result": "",
  "fallback_result": "",
  "final_report": "",
  "error_log": [],
  "quality_level": ""
}
```

**Important**: For all subsequent processing, automatically apply the following error handling rules:

**Try-Catch-Finally**:
- Always execute alternative measures when main processing fails
- Record execution logs in {{error_log}} regardless of success/failure

**Graceful Degradation**:
- Ideal operation: Detailed information via latest web search
- Practical operation: Basic information via existing knowledge
- Minimum operation: General knowledge overview only

## Phase 1: Web Search Information Collection Task

### Search Query Configuration

Save "Latest AI technology trends 2025" to {{search_query}}

### Try-Catch-Finally Implementation

**Try Processing**: Execute the following
- Execute web search with {{search_query}}
- Save search results to {{search_result}}

**Catch Processing**: If web search fails
- Display "Web search failed. Responding with existing knowledge"
- Save general AI technology trend information to {{fallback_result}}
- Record failure reason to {{error_log}}

**Finally Processing**: Regardless of success/failure
- Record execution status (success/failure, data source used) to {{error_log}}
- Record processing completion with timestamp

## Phase 2: Graceful Degradation Implementation

### Stepwise Information Quality Assessment

Set {{quality_level}} based on content of {{search_result}} and {{fallback_result}}:

**Ideal Level (Web Search Success)**:
- Set {{quality_level}} to "ideal"
- Create detailed technology trend report including latest information

**Practical Level (Using Existing Knowledge)**:
- Set {{quality_level}} to "practical"  
- Create report with basic technology trends and precautions

**Minimum Level (Significantly Limited Information)**:
- Set {{quality_level}} to "minimum"
- Provide only general AI field overview

### Stepwise Report Generation

Create {{final_report}} according to {{quality_level}}:

**For Ideal Level**:
- Detailed analysis of latest AI technology trends 2025
- Specific technology examples and market impact
- Future predictions and recommended actions

**For Practical Level**:
- Basic AI technology trends
- Overview of major technology fields
- Note: "Separate confirmation of latest information recommended"

**For Minimum Level**:
- General AI technology overview only
- Message: "Re-execution recommended for detailed information acquisition"

## Phase 3: Integrated Results Display

### Final Report Display

Display {{final_report}} as "=== AI Technology Trend Research Results ==="

### Quality Level Display

Display "=== Information Quality Level: {{quality_level}} ==="

### Error Handling Log Display

Display all entries in {{error_log}} as "=== Execution Log ==="

### Learning Value Explanation

Display the following:
"This error handling system enables automatic alternative processing when web search fails, stepwise service provision according to information quality, and complete execution history recording. Experience robust system design that assumes failure through the combination of Try-Catch-Finally and Graceful Degradation."