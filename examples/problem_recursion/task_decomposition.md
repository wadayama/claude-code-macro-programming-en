# Task Decomposition System (Beginner)

**Overview**: Step-by-step solution system through recursive problem division using TODO tool. Decomposes large problems into comprehensible units and achieves final integrated solution by accumulating reliable progress.

**Learning Objectives**: 
- Acquisition of recursive decomposition thinking
- State management through TODO tool integration
- Understanding decomposition decision logic
- Practice of integration processes

**Main Task**: Curry recipe creation

---

## Phase 1: Initial Problem Division

### Problem Setting and Analysis

Please set the main task "Curry Recipe" to {{main_task}}.

Analyze {{main_task}} and identify the major components needed for a cooking recipe:
- Ingredient preparation
- Tool preparation
- Cooking process
- Serving method

### First-Level Subtask Creation

Based on the above analysis, please add the following subtasks to the TODO list:

1. "Create ingredient list" - Priority: High
2. "Prepare cooking utensils" - Priority: Medium
3. "Create cooking procedure" - Priority: High
4. "Plating and serving method" - Priority: Low

**Decomposition rationale**: Divided into 4 independent domains necessary for curry making. Each domain can be prepared in parallel, and priorities can be clearly set.

Please check the TODO list status and confirm that 4 pending tasks have been correctly added.

## Phase 2: Recursive Decomposition Assessment & Execution

Please process tasks with "pending" status from the current TODO list one by one in priority order:

#### Decomposition Decision Thinking Process

For each pending task, judge using the following procedure:

1. **Complexity Assessment**: Is this task within the range that humans can understand and execute at once?
2. **Decomposability**: Can it be divided into more specific independent subtasks?
3. **Execution Decision**: Should it be executed directly or further decomposed?

### Task Processing Cycle

For each pending task, execute one of the following:

**If task can be executed directly** (small enough):
→ Mark the task as "in_progress" 
→ Execute the specific task and save results to appropriate variable
→ Mark the task as "completed"
→ Record execution results

**If task requires further decomposition** (too complex):
→ Mark the current task as "in_progress"
→ Create more specific subtasks and add to TODO list
→ Mark the original task as "completed" (decomposition completed)
→ Continue processing new subtasks

### Example: Processing "Create ingredient list"

Mark "Create ingredient list" as in_progress.

**Decomposition assessment**:
- Complexity: Medium complexity, can be further decomposed for clarity
- Decomposability: Can be divided by ingredient categories

**Decomposition execution**:
Add the following subtasks to TODO list:
1. "Main ingredients (meat, vegetables)" - Priority: High
2. "Spices and seasonings" - Priority: High  
3. "Base ingredients (oil, flour, etc.)" - Priority: Medium

Mark "Create ingredient list" as completed (decomposition completed).

## Phase 3: Recursive Processing Continuation

Please continue processing all pending tasks using the same decomposition logic:

For each remaining pending task:
1. Assess complexity and decomposability
2. Either execute directly or decompose further
3. Update TODO list status appropriately
4. Save execution results to variables

Continue until no pending tasks remain in the TODO list.

## Phase 4: Integration and Final Assembly

Once all subtasks are completed, please integrate the results:

Gather all execution results and create a comprehensive curry recipe including:
- Complete ingredient list with quantities
- Required cooking utensils
- Step-by-step cooking instructions
- Plating and serving suggestions

Save the integrated recipe to {{final_recipe}}.

## Phase 5: System Evaluation

Please evaluate the decomposition process:

1. **Decomposition effectiveness**: How did breaking down the problem improve understanding?
2. **TODO management**: How did the TODO tool help track progress?
3. **Integration quality**: How well do the decomposed parts work together?
4. **Learning outcome**: What insights were gained about recursive problem solving?

Display a summary of the task decomposition experience and the final curry recipe.

---

**Problem Solving & Recursion Pattern Characteristics**:
1. **Recursive Thinking**: Large problems broken into smaller, manageable pieces
2. **Decision Logic**: Clear criteria for when to decompose vs. execute
3. **State Management**: TODO tool tracks progress across decomposition levels
4. **Integration Process**: Decomposed solutions assembled into final result
5. **Adaptive Approach**: Process adjusts based on complexity assessment at each level

This example demonstrates how Problem Solving & Recursion enables systematic approach to complex tasks through structured decomposition and integration, making large problems tractable and solutions comprehensive.