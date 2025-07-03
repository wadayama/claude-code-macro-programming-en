# 🕐 Time-based User State Model (Pattern 7 Beginner)

**Overview**: Agent system that estimates user busyness through time sensing and automatically adjusts response style

---

## Complete Initialization (Clean Start)

Delete variables.json if it exists
Clear all TODO lists

Display "=== Time-based User State Model Started ===".

## 🎯 System Design

### User State Model
```
Time Period       → User State          → Response Style
Early morning (6-9)  → Relaxed           → Detailed explanation
Morning (9-12)       → Busy at office    → Brief summary
Afternoon (12-18)    → Busy on external work → Brief summary
Evening (18+)        → Relaxed time      → Detailed explanation
```

### Processing Flow
`Time Sensing → User State Estimation → Response Style Decision → Execution`

---

## Step 1: Environment Sensing (Time Information Acquisition)

Check the current time and set to {{current_time}}.

Determine the current hour from {{current_time}} and set to {{hour}}.

Display "=== Environment Sensing Results ===".
Display "Current time: {{current_time}} (around {{hour}} o'clock)".

---

## Step 2: Environment Model Application (User State Estimation)

Please apply the following user model based on {{hour}}:

**For early morning (6-9)**:
→ Set {{user_state}} to "Early morning - relaxed"
→ Set {{busy_level}} to "Low"
→ Set {{response_style}} to "Detailed explanation"

**For morning (9-12)**:
→ Set {{user_state}} to "Morning - busy with office work"
→ Set {{busy_level}} to "High"
→ Set {{response_style}} to "Brief summary"

**For afternoon (12-18)**:
→ Set {{user_state}} to "Afternoon - busy with external work"
→ Set {{busy_level}} to "High"
→ Set {{response_style}} to "Brief summary"

**For evening (18+)**:
→ Set {{user_state}} to "Evening - relaxation time"
→ Set {{busy_level}} to "Low"
→ Set {{response_style}} to "Detailed explanation"

Save the following information to user_state.json:
```json
{
  "timestamp": "{{current_time}}",
  "hour": "{{hour}}",
  "user_state": "{{user_state}}",
  "busy_level": "{{busy_level}}",
  "response_style": "{{response_style}}"
}
```

Display "=== Environment Model Estimation Results ===".
Display "Estimated user state: {{user_state}}".
Display "Busyness level: {{busy_level}}".
Display "Determined response style: {{response_style}}".

---

## Step 3: State-based Action Execution

Display "=== Response Style Execution Test ===".

Please answer the question "Please tell me tips for programming learning" according to {{response_style}}:

**For "Brief summary"**:
Explain concisely in 3 lines or less with only key points, and add "Due to busy hours, I provided only an overview. Please ask for details during your free time."

**For "Detailed explanation"**:
Explain thoroughly and carefully including specific examples and procedures, and add "Since you have free time, I'll explain in detail."

Please actually execute the response according to the above conditions.

After completing the response, display "Response adjustment considering user busyness completed".

---

## Step 4: Environment Model Effect Verification

Load user_state.json and set to {{model_state}}.

Display "=== Environment Model Effect Verification ===".

Verify effectiveness from the following perspectives:

### Environment Sensing Accuracy
- Was current time accurately acquired and determined?
- Was time period classification performed appropriately?

### User State Estimation Accuracy  
- Was user busyness appropriately estimated from time information?
- Was the assumed user model correctly applied?

### Behavior Switching Effect
- Did response style switch according to user state?
- Was it possible to explain briefly when busy and in detail when relaxed?

### Environment Model Value
- Was it possible to provide consideration (responding to busyness) that users didn't explicitly request?
- Could the agent give an impression of "understanding the user"?

Display "Adaptive response system using time-based user state model verified".


