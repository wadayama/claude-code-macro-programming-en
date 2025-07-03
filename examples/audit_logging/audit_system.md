# Outfit Recommendation Audit System (Basic)

**Overview**: Weather-based outfit recommendation system integrated with audit logging functionality. Automatically records all decision processes to ensure transparency and verifiability of decision rationale.

---

## Complete Initialization (Clean Start)

Delete variables.json if it exists
Clear all TODO lists

Display "=== Outfit Recommendation Audit System Started ===".

## Audit Rule Configuration

Create the following structure in variables.json:

```json
{
  "weather": "",
  "temperature": 0,
  "outfit": "",
  "final_advice": "",
  "audit_log": []
}
```

**Important**: For all subsequent actions, automatically record to audit_log in the following format:
```json
{
  "timestamp": "current_time",
  "event_type": "[action_type]",
  "content": "[detailed_execution_content]",
  "source": "system"
}
```

## Phase 1: Basic Variable Setup

### Weather Information Collection and Storage
From the information "Today is sunny with a temperature of 25 degrees":
- Save weather to {{weather}}
- Save temperature to {{temperature}}

### Variable Status Confirmation
Display the current values of {{weather}} and {{temperature}}

## Phase 2: Conditional Decision Making

### Outfit Recommendation Logic
Save the following to {{outfit}} based on the value of {{temperature}}:

- If {{temperature}} is 30 degrees or higher:
  → "Short sleeves, shorts, hat, sunscreen"

- If {{temperature}} is 20 degrees or higher but less than 30 degrees:
  → "Light long sleeves, light pants, sneakers"

- If {{temperature}} is 15 degrees or higher but less than 20 degrees:
  → "Long sleeves, jeans, light jacket"

- If {{temperature}} is less than 15 degrees:
  → "Heavy coat, knitwear, scarf, gloves"

### Weather-based Additional Adjustments
If {{weather}} contains "rain":
- Add "umbrella, raincoat" to {{outfit}}

## Phase 3: Final Result Integration

### Comprehensive Recommendation Creation
Combine {{weather}}, {{temperature}}, and {{outfit}} to create complete outdoor preparation advice in {{final_advice}}

### Result Display
Display {{final_advice}} as "=== Outfit Recommendation Result ==="

### Audit Trail Display
Display all entries in audit_log as "=== Complete Audit Trail ==="

### Significance of Auditing Explanation
Display the following:
"This audit record ensures traceability of outfit decision rationale, verification of temperature data, and transparency of the recommendation process. The timestamp of each entry enables chronological verification of the decision process."