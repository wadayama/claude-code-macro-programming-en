# Learning Progress Management System (Beginner)

**Overview**: Basic example of Loop & Modular Programming that progressively improves learning scores. Main loop manages learning cycles while external modules execute specific learning processes.

**Learning Objectives**: 
- Separation of loop control and processing logic
- State variable management
- Conditional termination assessment
- External module execution

---

## Initial Setup

Please set the learning score to 30 and save to {{score}}.
Please set the learning count to 0 and save to {{session}}.
Please set the learning history to empty and save to {{learning_log}}.

Please display "=== Learning Progress Management System Started ===".

## Learning Cycle

Please repeat the following until {{score}} reaches 70 or above:

Add 1 to {{session}}.

Display "--- Learning Session {{session}} Started ---".

Please execute study_session.md.

Display "--- Learning Session {{session}} Completed ---".

If {{score}} reaches 70 or above, display "Goal achieved! Learning completed".

## Final Report

Please display "=== Learning Results Report ===".

Please report the following learning outcomes:
- Final learning score: {{score}}
- Number of learning sessions executed: {{session}}
- Learning trajectory: {{learning_log}}

Please summarize learning effectiveness and future recommendations.

---

## Execution Example and Expected Results

**Initial State**: Score 30, Session 0
**Goal**: Score 70 or above
**Expected Cycle Count**: 3-4 sessions
**Learning Point**: Improved readability through module separation

**Loop & Modular Programming Pattern Characteristics**:
1. **Loop Control**: Main system manages iteration and termination conditions
2. **Modular Execution**: Specific learning logic separated into study_session.md
3. **State Persistence**: Variables maintain state across loop iterations
4. **Progressive Improvement**: Each iteration builds upon previous results
5. **Clean Separation**: Loop management and business logic are distinct concerns

This example demonstrates how Loop & Modular Programming enables maintainable, scalable systems by separating control flow from business logic while maintaining state across multiple iterations.