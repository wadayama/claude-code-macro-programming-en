# Variable Debugging System (Beginner)

**Overview**: Basic practice of variable state tracking using debug mode. Through a weather-based outfit recommendation system, visualize the process of variable setting, referencing, and updating in detail to master debugging techniques in natural language macro programming.

---

## Complete Initialization (Clean Start)

Delete variables.json if it exists
Clear all TODO list items

Display "=== Variable Debugging System Started ===".

## Phase 1: Basic Variable Setting

Load debugger.md first, then execute the following in debug mode:

### Weather Information Acquisition & Storage
From the information "Today is sunny with a temperature of 25 degrees":
- Save the weather to {{weather}}
- Save the temperature to {{temperature}}

### Variable State Confirmation
Display the current values of {{weather}} and {{temperature}}

## Phase 2: Conditional Judgment

Execute the following conditional branching in debug mode:

### Outfit Recommendation Logic
Save the following to {{outfit}} based on the value of {{temperature}}:

- If {{temperature}} is 30 degrees or higher:
  → "Short sleeves, shorts, hat, sunscreen"

- If {{temperature}} is 20 degrees or higher but less than 30 degrees:
  → "Light long sleeves, light pants, sneakers"

- If {{temperature}} is 15 degrees or higher but less than 20 degrees:
  → "Long sleeves, jeans, light jacket"

- If {{temperature}} is less than 15 degrees:
  → "Heavy coat, knit sweater, scarf, gloves"

### Weather-based Additional Adjustment
If {{weather}} contains "rain":
- Add "umbrella, raincoat" to {{outfit}}

## Phase 3: Final Result Integration

Execute the following in debug mode:

### Comprehensive Recommendation Creation
Combine {{weather}}, {{temperature}}, and {{outfit}} to create complete outdoor preparation advice and save to {{final_advice}}

### Result Display
Display {{final_advice}} as "=== Outfit Recommendation Result ==="