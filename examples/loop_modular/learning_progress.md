# Learning Progress Management System (Beginner)

**Overview**: Basic example of TODO-list based Loop Processing that progressively improves learning scores. Achieves reliable, highly visible loop processing by using TODO task management without traditional counter control.

**Learning Objectives**: 
- Understanding basic TODO-list based loops
- Utilizing clean start functionality
- Implementing conditional loop termination
- Complete visibility of execution state

---

## Complete Initialization (Clean Start)

Delete variables.json if it exists
Clear all TODO list items

Display "=== Learning Progress Management System Started ===".

## Variable Initialization

Set {{score}} to 30
Set {{session}} to 0
Set {{learning_log}} to empty

## Loop Task Creation

Add the following task pair to TODO list up to 5 times:
- Execute one learning session
- If {{score}} is 70 or above, delete remaining tasks and terminate

## Execution

Execute TODO list tasks sequentially from top

For each "Execute one learning session" task:
1. Add 1 to {{session}}
2. Display "--- Learning Session {{session}} Started ---"
3. Add 12 to {{score}} (learning effect)
4. Append "Learning+12 points" to {{learning_log}}
5. Display "--- Learning Session {{session}} Completed ---"
6. Display "Current score: {{score}}"

## Final Report

After all TODO tasks complete:

Display "=== Learning Results Report ===".

Report the following learning outcomes:
- Final learning score: {{score}}
- Number of learning sessions executed: {{session}}
- Learning trajectory: {{learning_log}}

Summarize learning effectiveness and future recommendations.

---

## Execution Example and Expected Results

**Initial State**: Score 30, Session 0
**Goal**: Score 70 or above
**Expected Execution Pattern**: 
- Session 1: 30→42 (continue)
- Session 2: 42→54 (continue)  
- Session 3: 54→66 (continue)
- Session 4: 66→78 (condition met! delete remaining tasks)

**Technical Features**: 
- No counter management required for stability
- Complete progress visibility through TODO list state
- Reliable conditional termination through dynamic task deletion