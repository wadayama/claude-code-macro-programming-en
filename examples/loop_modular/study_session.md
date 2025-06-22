# Learning Processing Module

**Overview**: Processing module for learning progress management system. Provides appropriate learning content based on current learning level and updates scores.

**Variable Management**:
- `{{score}}`: Current learning score (reference & update)
- `{{learning_log}}`: Learning history (append)
- `{{session}}`: Current session number (reference only)

---

## Current Status Check

Check the current learning score {{score}} and display "Current score: {{score}} points".

## Learning Level Assessment & Execution

Execute the following learning processes based on the value of {{score}}:

If {{score}} is less than 50:
→ Display "Executing basic learning"
→ Conduct review of basic concepts and comprehension check
→ Add 15 to {{score}}
→ Append "Basic learning completed: +15 points" to {{learning_log}}

If {{score}} is 50 or more but less than 65:
→ Display "Executing applied learning"
→ Conduct practical problem solving and application skill improvement
→ Add 12 to {{score}}
→ Append "Applied learning completed: +12 points" to {{learning_log}}

If {{score}} is 65 or more:
→ Display "Executing advanced learning"
→ Conduct training in advanced concepts and creative thinking
→ Add 8 to {{score}}
→ Append "Advanced learning completed: +8 points" to {{learning_log}}

## Learning Outcome Recording

Display the post-learning score {{score}} and show "Session {{session}} completed. New score: {{score}} points".

Verify the type and effectiveness of learning executed, and present recommended items for next learning session if available.

---

**Modular Design Characteristics**:
1. **Self-contained Logic**: Complete learning process within single module
2. **Variable Interface**: Clear input/output variable contract
3. **Conditional Processing**: Score-based adaptive learning paths
4. **State Management**: Score updates and log append operations
5. **Reusability**: Can be called repeatedly with different session contexts

This module demonstrates how natural language macro programming can create reusable, stateful components that maintain learning progress and adapt behavior based on current state.