# Adaptive Learning System (Conditional Execution - Beginner)

## Complete Initialization (Clean Start)

Delete variables.json if it exists
Clear all TODO lists

Display "=== Conditional Execution System Started ===".

## Learner Level Assessment

Please choose the most appropriate option for your programming learning experience:

**A. Beginner (No experience or less than 6 months)**
- Just started programming or have no experience at all
- Want to learn basic concepts such as variables, conditional statements, and loops

**B. Intermediate (6 months to 2 years)** 
- Can write basic programs but want to challenge more complex processing
- Want to learn about functions, classes, and data structures

**C. Advanced (2+ years)**
- Have experience with multiple projects and are interested in design and architecture
- Want to deeply learn algorithms and design patterns

**Please enter your choice (A, B, or C).**

Save your response to {{learner_level}}.

## User Response Confirmation

First, display the contents of {{learner_level}} to confirm the user's selection.

## Personalized Curriculum Provision

Execute the following based on the value of {{learner_level}}:

If {{learner_level}} is "A":
→ Display "Creating beginner curriculum"
→ Research learning materials for programming basics, variables, conditional statements, and loops, and save to {{beginner_curriculum}}

If {{learner_level}} is "B":
→ Display "Creating intermediate curriculum"  
→ Research learning materials for functions, classes, data structures, and small-scale project development, and save to {{intermediate_curriculum}}

If {{learner_level}} is "C":
→ Display "Creating advanced curriculum"
→ Research learning materials for algorithms, design patterns, and architecture, and save to {{advanced_curriculum}}

## Learning Goal Setting

Before creating the curriculum, please tell us your specific learning goals:

**Please select the most important goal from the following:**

**1. Skill acquisition for employment/career change**
**2. Personal project development**  
**3. Tool creation for work efficiency**
**4. Programming learning as a hobby/interest**

**Please enter your choice (number 1-4).**

Save your response to {{learning_goal}}.

## Learning Plan Creation

Based on {{learner_level}} and {{learning_goal}}, create a detailed 3-month learning schedule.

For each level and goal combination, present a specific plan including:
- Weekly learning topics
- Recommended study hours
- Practical project proposals
- Milestones for goal achievement

## Curriculum Approval Confirmation

Display the created learning plan and confirm the following:

"Is this learning plan acceptable? If you have any modification requests, please be specific. If acceptable, please enter 'Approved'."

Save the user's response to {{plan_approval}}.

## Progress Management Proposal

Only if {{plan_approval}} is "Approved", execute the following:
→ Propose learning progress measurement methods and achievement verification methods appropriate for {{learner_level}} and {{learning_goal}}
→ Present regular feedback methods and learning effectiveness measurement indicators

