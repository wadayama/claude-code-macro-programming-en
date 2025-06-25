# Claude Code Natural Language Macro Programming Guide

**Claude Code** is a specialized coding environment that extends Anthropic's AI assistant Claude ([Official Documentation](https://docs.anthropic.com/en/docs/claude-code)). It integrates powerful tool suites including file operations, Bash execution, and web search, supporting a wide range of tasks from programming to document creation. This guide presents methods for utilizing Claude Code not merely as a coding tool, but as an agent execution environment programmable through natural language.

## 🤖 Core Concept: Agent Programming Using Claude Code as Interpreter

This guide presents a **Natural Language Macro Programming** approach that **executes structured tasks using natural language as macro code, with LLM as interpreter**. This guide uses Claude Code as an execution environment.

While conventional programming requires computers to interpret programming languages with specific syntax, natural language macro programming enables:

- **Natural language and Markdown notation** as program descriptions
- **Claude Code** functioning as an interpreter that parses and executes these descriptions
- **Advanced control structures** (Task tool, TODO tool, variable management, conditional branching, parallel execution) realized through natural language
- **Agent systems** for automating and optimizing complex tasks

Even people without programming experience can design agent behaviors using intuitive natural language and have Claude Code execute them.

*The macro syntax used in this guide operates based on the grammar defined in CLAUDE.md. Users write macros in natural language, and Claude executes them according to the grammar rules defined in CLAUDE.md.* **Before actual execution, the CLAUDE.md file must be loaded into Claude Code.**

## 🌍 Framework Generality and Design Philosophy

This "Natural Language Macro Programming" concept and design philosophy is not bound to any specific LLM. It is expected to be sufficiently applicable to other high-performance LLMs that meet certain conditions.

The core of this framework lies not in tools or specific products, but in **"the approach itself of executing structured tasks using LLM as natural language interpreter."** Claude Code is positioned as one excellent execution environment that realizes this approach.

**Applicable Conditions**:
- Ability to understand and execute complex natural language instructions
- Variable management and state retention capabilities
- Ability to integrate with external tools and modules
- Ability to interpret structured documents in Markdown format

## 🔗 Complementary Relationship with Existing Prompt Techniques

Natural language macro programming is not competitive with existing prompt techniques such as CoT (Chain of Thought) and ReAct, but rather operates as a complementary technology at different layers.

### Differences in Technical Layers

**Existing Prompt Techniques (CoT, ReAct, etc.)**:
- **Purpose**: Optimization of individual reasoning processes
- **Scope**: Improvement of thought processes within single tasks
- **Examples**: Enhanced problem analysis accuracy, step-by-step reasoning implementation

**Natural Language Macro Programming**:
- **Purpose**: Construction, control, and integration of entire systems
- **Scope**: Multi-task coordination, state management, flow control
- **Examples**: Pipeline design, parallel processing, error handling

### Practical Combination Examples

```markdown
## CoT + Sequential Pipeline Combination
Step 1: Analyze complex problems step-by-step using CoT
Step 2: Save analysis results to {{analysis_result}}
Step 3: Execute solutions sequentially through Sequential Pipeline

## ReAct + Parallel Processing Combination
Execute ReAct-based information gathering in each parallel task,
then integrate results through Parallel Processing
```

By leveraging the strengths of existing techniques while utilizing natural language macro programming for overall system design and control, more advanced and practical AI systems can be constructed.

## 🔍 High Explainability and Contribution to Responsible AI Development

Natural Language Macro Programming possesses **high explainability**, an extremely important characteristic for Responsible AI development:

**Explainability Features**:
- **Natural language description**: Processing steps expressed in human-understandable form
- **Transparent execution process**: Clear inputs, outputs, and decision rationale for each step
- **Auditability**: Easy verification and tracking of system behavior retrospectively
- **Debuggability**: Intuitive problem identification and correction when issues arise

**Contribution to Responsible AI Development**:
- Higher transparency in decision-making processes compared to traditional black-box AI systems
- Easier accountability for AI system operations
- Enables appropriate human oversight and control
- Facilitates discovery and correction of errors and biases

## ⚠️ Probabilistic Behavior Characteristics

The natural language macro programming techniques presented in this guide are based on the probabilistic operational characteristics of Large Language Models (LLMs):

- **High-probability operations**: Variable management (`{{variable_name}}`), external module execution (`filename.md execution`), etc., in the case of sufficiently excellent LLMs, operate with very high probability as expected. Variable management is not true programming variables but probabilistic emulation based on pattern recognition within LLM context
- **Non-deterministic nature**: 100% deterministic operation cannot be expected due to LLM characteristics
- **Practical reliability**: Operates at a level with sufficient reliability for actual use
- **Error handling capabilities**: Continues to provide partial value through graceful degradation and systematic error recovery

## 🎯 Learning Objectives

1. **Fundamental Concepts of Natural Language Macro Programming**
   - Information management and result passing
   - Implementation of conditional branching and multitask processing

2. **9 Design Patterns**
   - Sequential Pipeline
   - Parallel Processing
   - Conditional Execution
   - Loop & Modular Programming
   - Problem Solving & Recursion
   - Learning from Experience
   - Environment Sensing, Knowledge-base and Environment Model
   - Human-in-the-Loop
   - Error Handling

3. **Practical System Construction Capabilities**
   - Hands-on practice with graduated samples
   - Application examples including haiku generation systems
   - Methods for business process automation

---

**Version**: 1.0  
**Authors**: Tadashi Wadayama & Claude Code (Anthropic Inc.)  
**Created**: 2025-06-21  
**License**: MIT License (2025)

---

## 🎯 Research Purpose and Significance

### Research Background and Challenges

With the rapid development of modern AI technology, new approaches to designing human-machine collaborative systems are increasingly demanded. Traditional programming paradigms assume specialized knowledge, creating high barriers to entry for non-experts in building agent systems. This research aims to address these challenges through structured task description utilizing Claude Code's natural language processing capabilities and Markdown notation.

### Proposed Approach

This research proposes a novel methodology called "Natural Language Macro Programming," consisting of the following elements:

1. **Establishment of Systematic Design Patterns**
   - Construction of a graduated learning system through 9 design patterns
   - Design methodologies comprehensively covering from basic processing to advanced human collaboration
   - Development of reusable and extensible pattern libraries

2. **Natural Language Structured Description Methods**
   - Intuitive task description methods independent of programming syntax
   - Utilization of Markdown notation with high affinity to human cognitive processes
   - Description rules considering the balance between ambiguity control and structuring

3. **Graduated Learning Model Design**
   - Systematic progression from basic patterns (sequential, parallel, conditional) to advanced patterns (learning, environment understanding, human collaboration, error handling)
   - Educational approach integrating theoretical learning with practical application
   - Demonstration of versatility through application examples in diverse fields

### Shared Documentation in Collaboration with Claude Code

When considering having Claude Code write natural language macro programming code, by including this document in the context, you can provide specific instructions such as: "For sales data, execute parallel analysis along 3 axes (regional, product, time series) using the Parallel Processing pattern, integrate results into {{analysis_result}}, and execute report creation through Sequential Pipeline." This enables specifying design patterns when having Claude Code create prompts, utilizing the design patterns presented here as a common language in human-AI collaboration.

### Significance and Future Prospects

The approach proposed in this research is expected to provide methodological foundations for human-AI collaborative system design, which is an important challenge in the social implementation of AI technology.

---

## 📋 Representative Syntax of Claude Code Natural Language Macro Programming

```markdown
- Conditional branching: Natural language conditional instructions ("if...", "depending on...", etc.)
- `{{variable_name}}`: Variable reference
- Variable storage: "Save ... to {{variable_name}}"
- Persistent storage: "Save {{variable_name}} to filename.json for persistence"
- File loading: "Load filename.json and set to {{variable_name}}"
- External module execution: "Execute filename.md"
- File search: "Search for files containing 'keyword'"
- Parallel execution: "Execute the following tasks in parallel:"
- Loop processing: "Repeat the following process until [condition]:"
```

## 🔧 Basic Variable Management

Claude Code can manage variables through natural language instructions, enabling information passing between different processing steps.

### Variable Operations

```markdown
## Data Analysis Pipeline
Analyze the sales data and save the results to {{analysis_result}}.

Based on {{analysis_result}}, create a summary report and save it to {{final_report}}.

Save {{final_report}} to report.json for permanent storage.
```

### Variable Management Features

A unified natural language notation is used:

```markdown
# Result Storage
Analyze data and save results to {{analysis_result}}.

# Result Reference  
Based on {{analysis_result}}, create a report.
```

### Control Structures

Conditional branching can be described flexibly in natural language:

```markdown
## Data Processing
If {{file_size}} is 1MB or larger, execute detailed analysis.
Otherwise, execute basic analysis.
```

### Module Execution

Modular design is possible by calling external module files:

```markdown
## Data Processing Pipeline
Execute data_collection.md.
Execute data_analysis.md.
Execute report_generation.md.

## Conditional Module Execution
Depending on {{data_type}}, execute the following:
- For text data: Execute text_analysis.md
- For numerical data: Execute numerical_analysis.md
```

**Module Execution Benefits**:
- **Reusability**: Manage common processes as independent modules
- **Maintainability**: Develop and test each module independently
- **Scalability**: Practical construction of large-scale systems
- **Collaboration**: Easy responsibility sharing in team development

---

## 📚 Basic Syntax Sample Collection

### 1. Sequential Execution: Python Learning Guide Creation

```markdown
## Basic Information Collection
Research "Python Introduction" on the web and save 3 key points for beginners to {{basics}}.

## Learning Plan Creation
Based on {{basics}}, create a 1-week learning schedule and save to {{schedule}}.

## Final Guide Creation
Combine {{basics}} and {{schedule}} to create a "Python Introduction Guide".
```

### 2. Parallel Execution: Morning Routine Analysis

```markdown
## Morning Routine Analysis
**Execute the following 3 tasks in parallel using the Task tool:**

### Grooming Analysis
Analyze morning grooming activities (washing face, brushing teeth, dressing, etc.) and save characteristics and efficiency tips to {{grooming}}.

### Breakfast Preparation Analysis  
Analyze breakfast preparation (menu selection, cooking, nutritional balance, etc.) and save characteristics and ideas to {{breakfast}}.

### Departure Preparation Analysis
Analyze departure preparation (item confirmation, transportation, time management, etc.) and save characteristics and tips to {{departure}}.

## Comprehensive Morning Routine Proposal
Combine {{grooming}}, {{breakfast}}, and {{departure}} to propose efficient and fulfilling morning routines.
```

### 3. Conditional Branching: File Processing System

```markdown
## File Confirmation
Check the size (character count) of README.md file and save to {{file_size}}.

## Processing Method Decision
Depending on {{file_size}}, execute the following:
- If less than 100 characters: Output "Concise file. Displaying full text" and save full text to {{content}}
- If 100 characters or more: Output "Detailed file. Creating summary" and save summary to {{content}}

## Result Display
Display results in appropriate format using {{content}}.
```

### 4. File Persistence: Learning Progress Management

```markdown
## Today's Learning Record
Save today's learning content as "Claude Code Basic Operations" to {{today_study}}, and
save {{today_study}} to study_log.json for persistence.

## Progress Confirmation
Load study_log.json and set to {{study_history}},
summarize and display consecutive learning days and content.
```

### 5. Integration Example: Market Research System

```markdown
## Research Preparation
Save "AI Market Trends" as research theme to {{theme}}.

## Parallel Information Gathering
**Execute the following 3 tasks in parallel using the Task tool:**

Research the following about {{theme}}:

### Technology Trends
Save latest AI technology trends to {{tech_trends}}.

### Market Size
Save AI market size and growth forecasts to {{market_size}}.

### Company Strategies
Save major AI companies' strategies to {{company_strategies}}.

## Conditional Report Creation
Confirm completeness of {{tech_trends}}, {{market_size}}, {{company_strategies}}:
- If all 3 collected: Create comprehensive market analysis report integrating {{tech_trends}}, {{market_size}}, {{company_strategies}}
- If 2 or fewer: Create basic report with available information and note missing parts

## Result Storage
Save final report to ai_market_report.json for persistence.
```

---

## 🔄 Basic Design Patterns

### Pattern 1: Sequential Pipeline

**Overview**: Basic pattern for processing data step by step. Achieves reliable results through linear flow of `collection → processing → output`.

**Processing Flow**: `Input → Process1 → Process2 → Process3 → Output`

**Application Criteria**:
- ✅ Processing has clear sequential order
- ✅ Results from previous stage become input for next stage
- ✅ Want to test and improve each stage independently
- ❌ Each process is completely independent (→Consider Parallel Processing)

**Practical Example: Blog Article Creation System**
```markdown
## Topic Research
Research "Remote Work Benefits" on the web and save 5 main points to {{research}}.

## Structure Creation
Based on {{research}}, create readable blog article structure (3-5 headings) and save to {{structure}}.

## Article Writing
Following {{structure}}, write 1500-word blog article and save to {{article}}.

## Final Review
Proofread {{article}} for readability and accuracy to create final version.
```

**Key Learning Point**: Variable design ensuring each stage utilizes previous results is crucial

### 🛡️ Robust Sequential Pipeline (Large-scale Task Support)

**Problem Recognition**: When each stage involves large, complex tasks, the following issues may occur:
- Difficulty recovering from mid-process failures
- Lack of progress management in long-running executions  
- Difficulty resuming after session interruptions
- Opacity of partial completion status

**Solution Approach**: Integration with TODO list tools to improve robustness and traceability

**Improvement Points**:
- **Gradual Decomposition**: Break down each main stage into subtasks for TODO management
- **Progress Visualization**: Real-time confirmation of completion status
- **State Persistence**: Support for continued execution across sessions
- **Failure Recovery**: Efficient recovery from partial failures

**Practical Example: Large-scale Research Report Creation System**
```markdown
## Phase 1: Research Plan Development
Add the following subtasks to TODO list:
1. "Research theme refinement and scope setting" - Priority: High
2. "Identify major information sources and confirm accessibility" - Priority: High  
3. "Determine research methodology and execution plan" - Priority: Medium
4. "Set schedule and milestones" - Priority: Medium

Execute each task sequentially and update status to "completed" upon completion.

## Phase 2: Literature Survey Execution
After previous phase completion, add to TODO list:
1. "Search and collect academic papers" - Priority: High
2. "Analyze industry reports" - Priority: High
3. "Acquire and organize statistical data" - Priority: Medium
...

## Progress Confirmation
Upon each phase completion, confirm overall progress and determine transition to next phase.
```

**Application Criteria**:
- ✅ Large-scale tasks requiring 30+ minutes total execution time
- ✅ Processing that may span multiple sessions
- ✅ Business where recovery from partial failures is important
- ✅ Projects requiring progress visualization and tracking
- ❌ Lightweight tasks completing within 5 minutes (→Use basic version)

**Key Learning Point**: Master systematic management techniques for large-scale tasks through TODO list and Sequential Pipeline integration

---

### Pattern 2: Parallel Processing

**Overview**: Processing pattern that achieves efficiency and multi-perspective insights through simultaneous execution of independent tasks.

**Processing Flow**: `Input → [TaskA, TaskB, TaskC] → Integration → Output`

**Application Criteria**:
- ✅ Each process is mutually independent
- ✅ Need analysis from different perspectives on same data
- ✅ Processing time reduction is important
- ❌ Processing has strict sequential order (→Consider Sequential Pipeline)

**Practical Example: Weekend Activities Analysis System**
```markdown
## Analysis Target Setting
Save "Fulfilling Weekend" as analysis target to {{weekend}}.

## Parallel Activity Analysis
**Execute the following 3 tasks in parallel using the Task tool:**

Analyze the following activities for {{weekend}}:

### Indoor Activity Analysis
Analyze characteristics of home activities (reading, movies, cooking, etc.) and save to {{indoor}}.

### Outdoor Activity Analysis
Analyze characteristics of outdoor activities (walking, sports, travel, etc.) and save to {{outdoor}}.

### Social Activity Analysis
Analyze characteristics of social activities (dining with friends, event participation, etc.) and save to {{social}}.

## Weekend Plan Proposal Report
Combine {{indoor}}, {{outdoor}}, {{social}} to propose balanced weekend activities.
```

**Key Learning Point**: Ensuring each parallel task is independent and always including an integration stage is crucial

---

## 🎌 Practical Example Explanation: Haiku Generation Agent System

### System Overview

The haiku generation agent system is a practical example combining **Sequential Pipeline** and **Parallel Processing**. By implementing the creative process as a macro, it efficiently generates consistently high-quality haiku.

### 📁 Implementation File

- **[haiku_direct.md](./haiku_direct.md)** - Complete implementation code
- **Learning Purpose**: Combination techniques of Sequential Pipeline and Parallel Processing
- **Execution Method**: Run the file directly in Claude Code

### 🏗️ System Structure Analysis

#### Phase 1: Sequential Pipeline (Sequential Execution)
```
Theme Generation → Parallel Haiku Creation → Haiku Evaluation & Selection → Final Report
```

**Design Decision**: Adopted Sequential Pipeline as each stage depends on previous stage results

#### Phase 2: Parallel Processing (Parallel Execution)
```
Within Parallel Haiku Creation Section:
├── Task 1: Theme 1 Haiku (Parallel)
├── Task 2: Theme 2 Haiku (Parallel)  
├── Task 3: Theme 3 Haiku (Parallel)
└── Task 4: Theme 4 Haiku (Parallel)
```

**Design Decision**: Since each haiku creation is independent, used Parallel Processing for efficiency

### 🔄 Data Flow Design

**Variable Management**:

1. **Theme Sharing**: `{{themes}}` → Common use across all parallel tasks
2. **Individual Results**: `{{haiku_1}}`, `{{haiku_2}}`, `{{haiku_3}}`, `{{haiku_4}}` → Independent storage
3. **Evaluation Integration**: `{{best_selection}}` → Integrated evaluation of parallel results
4. **Final Output**: Comprehensive report referencing all variables

### 💡 Learning Points

#### 1. Appropriate Pattern Combination
- **Outer Framework**: Sequential Pipeline (Overall process)
- **Internal**: Parallel Processing (Haiku generation section)
- **Whole**: Single integrated system

#### 2. Systematic Variable Design
```markdown
# Common Input Variable
{{themes}} → Used across all parallel tasks

# Individual Output Variables  
{{haiku_1}}, {{haiku_2}}, {{haiku_3}}, {{haiku_4}} → Independent results of each task

# Integration Variable
{{best_selection}} → Evaluation and selection of parallel results
```

#### 3. Practical Quality Management
- **Diversity Assurance**: Multi-perspective approach with 4 different themes
- **Objective Evaluation**: Selection process with clear evaluation criteria
- **Comprehensive Recording**: Final report preserving all process results

### 🎯 Implementation Features

#### Intuitive Instructions in Natural Language
```markdown
# Non-technical, natural expressions
"Follow 5-7-5 syllable structure and express the strangeness and uniqueness of the theme"
"Select the most strange and impressive haiku"
```

#### Complete Automation
- Completes without human intervention
- All processes execute automatically
- Ensures consistent quality

### 📈 Application Potential

This system structure can be applied to the following fields:

- **Creative Activities**: Novel, poetry, catchphrase generation
- **Content Production**: Articles, presentation materials, proposal documents
- **Decision Support**: Generation, evaluation, and selection of multiple options
- **Quality Assurance**: Quality improvement through multi-perspective verification

### 🎓 Learning Effects

Understanding `haiku_direct.md` is expected to provide:

1. Mastery of **practical combination of basic patterns**
2. Understanding of **effective variable management design techniques**  
3. Acquisition of **practical system construction capabilities**
4. Embodiment of **the essence of natural language macro programming**

This file serves as a **useful bridge** from basic patterns to practical systems as learning material.

---

### Pattern 3: Conditional Execution

**Overview**: Dynamically selects different processing paths based on situations. Realizes optimal processing based on data characteristics or user situations, constructing flexible and practical systems.

**Processing Flow**: `Input → Condition Judgment → [ProcessA | ProcessB | ProcessC] → Output`

**Application Criteria**:
- ✅ Need to change processing based on data or situations
- ✅ Error handling and exception processing are important
- ✅ Need function control based on user permissions or settings
- ❌ Same processing is always sufficient (→Consider [Sequential Pipeline](./examples/sequential/))
- ❌ Complex problem division needed (→Consider [Problem Solving & Recursion](./examples/problem_recursion/))

**Practical Example: Automatic File Processing and Routing System**
```markdown
## File Information Acquisition
Specify the target file and acquire the following information:
- Save file format to {{file_type}}
- Save file size to {{file_size}}
- Save number of lines in file to {{line_count}}

## Processing Branch by File Format
Branch processing according to {{file_type}}:

CSV format case:
→ Execute data analysis processing and save result to {{analysis_result}}

JSON format case:
→ Execute structure analysis processing and save result to {{structure_result}}

Text format case:
→ Execute natural language processing and save result to {{nlp_result}}

Other format case:
→ Extract basic information only and save to {{basic_info}}

## Processing Method Selection by File Size
Adjust processing method according to {{file_size}}:

10MB or larger case:
→ "Large file detected, executing split processing"
→ Execute chunk split processing with {{chunk_processing}}

Under 1MB case:
→ "Small file detected, executing batch processing"
→ Execute batch processing with {{batch_processing}}

## Result Integration and Output
Integrate processing results into {{final_result}},
and record processing method and execution time to {{processing_log}}
```

**Key Learning Point**: Covering all conditional patterns and setting clear judgment criteria is crucial

---

### 🔤 Ambiguity Tolerance Processing

**Overview**: Design principle leveraging natural language processing characteristics to provide value through speculation-based processing even with unclear requirements. Approach utilizing ambiguity as system flexibility rather than treating it as "errors" in conventional programming.

**4-stage Ambiguity Response Strategy**: `Clear → Partial Speculation → High Speculation → Uninterpretable`

1. **Speculation-based Continuation**: Continue processing through speculation rather than error termination
2. **Confidence Level Indication**: Transparent display of speculation level and uncertainty to users
3. **Gradual Refinement**: Provide guidance for improvement to clearer requirements
4. **Continued Value Provision**: Provide basic framework even in worst conditions

### Practical Example: Gradual Processing of Ambiguous Requests

```markdown
## Ambiguous Request Interpretation
Judge ambiguity level of {{user_request}} and execute the following:

Clear request case:
→ Execute definitively and save to {{definitive_result}}

Partial ambiguity case:
→ Execute as "Will process based on context inference" and save to {{inferred_result}}
→ Record "Includes partial speculation" to {{uncertainty_note}}

High ambiguity case:
→ Execute as "Will process based on most likely interpretation" and save to {{speculative_result}}
→ Record "Interpretation based on high speculation" to {{speculation_note}}

Uninterpretable case:
→ Provide general framework and save to {{fallback_framework}}
→ Record "Recommend re-input of specific request" to {{clarification_request}}
```

### 🆚 Differentiation from Conventional Programming

#### Conventional System Design
```
Ambiguous Input → Error → Processing Stop → User Departure
```

#### Ambiguity Tolerance System
```
Ambiguous Input → Speculative Processing → Useful Results + Uncertainty Indication → Gradual Improvement
```

**Unique Value of Natural Language Macro Programming**:
- **From Binary Judgment to Spectrum**: Gradual evaluation of confidence levels rather than success/failure
- **From Perfection to Practicality**: Provide partially useful value rather than complete understanding
- **From Error to Opportunity**: Design philosophy utilizing ambiguity as flexibility

This ambiguity tolerance processing improves response to ambiguity in natural human-AI dialogue, enabling construction of more practical systems. It provides an approach for agents to perform "speculative continuation" processing rather than "complete stoppage" in situations based on uncertain information.

---

## 📁 Practical Sample Collection

Detailed practical examples of the basic 3 patterns can be learned from the following:

### 🔄 Sequential Pipeline
- **Beginner**: [Blog Article Creation System](./examples/sequential/blog_creation.md) - From theme setting to proofreading
- **Intermediate**: [Academic Research Pipeline](./examples/sequential/research_pipeline.md) - From hypothesis construction to paper writing
- **Advanced**: [Large-scale Research Report Creation System](./examples/sequential/robust_research_system.md) - TODO-integrated robust version

### ⚡ Parallel Processing
- **Beginner**: [Market Analysis System](./examples/parallel/market_analysis.md) - Simultaneous research of technology, market, and competition
- **Intermediate**: [Competitive Research System](./examples/parallel/competitive_research.md) - Parallel corporate analysis of 5 companies

### 🎌 Conditional Execution
- **Beginner**: [Adaptive Learning System](./examples/conditional/adaptive_tutor.md) - Level-specific curriculum provision
- **Intermediate**: [Ambiguous Request Interpretation System](./examples/conditional/content_processor.md) - Natural language ambiguity fallback

---

### Pattern 4: Loop & Modular Programming

**Overview**: Advanced pattern executing iterative processing while maintaining state and separating complex logic into external modules to improve system maintainability and reusability. Gradually constructs from simple iterative processing to practical loop systems with conditional control and safety mechanisms.

**Processing Flow**: `Initialization → [State Update → External Module Execution → Condition Judgment] → Termination Processing`

**Application Criteria**:
- ✅ Iterative processing with state updates needed
- ✅ Want to implement continuous improvement or learning processes
- ✅ Need to execute complex processing logic within loops
- ✅ Loop processing readability and maintainability are important
- ✅ Need loops with conditional control and safety mechanisms
- ❌ Simple repetition without state changes (→Basic iteration is sufficient)

**Modular Design Value**:
- **Readability**: Separation of loop control and processing logic
- **Reusability**: Independent use of processing modules
- **Maintainability**: Independent development and testing of each part
- **Scalability**: Large-scale system construction

### 🔢 Basic Example: Simple Count-up System

First, to understand the most basic concepts of Loop & Modular Programming, start with simple fixed-count loops:

```markdown
## Initial Setup
Set counter to 0 as {{counter}}.
Set total value to 0 as {{total}}.

## 5-time Repeat Loop
Repeat the following 5 times:

Add 1 to {{counter}}.
Add {{counter}} to {{total}}.
Display "Count: {{counter}}, Current total: {{total}}".

## Final Result
Display "Complete! Final count: {{counter}}, Grand total: {{total}}".
```

**Learning Points**:
- **State Variables**: `{{counter}}` and `{{total}}` are updated each loop
- **Fixed Count**: Clear termination condition of 5 times
- **State Accumulation**: Values change gradually through repetition

### 🏗️ Application Example: Modular Quality Improvement System

*Main Loop File (main_improvement.md)*:
```markdown
## Initial Setup
Set quality score to 40 as {{score}}.
Set improvement count to 0 as {{iteration}}.
Set improvement history to empty state as {{improvement_log}}.

## Quality Improvement Loop
Repeat the following until {{score}} reaches 85 or above or {{iteration}} reaches 8:

Display "=== Improvement Cycle {{iteration}} Start ===".

Execute improvement_process.md.

Add 1 to {{iteration}}.

Display "=== Improvement Cycle {{iteration}} Complete ===".

## Final Result Report
Display "Quality improvement process complete".

Report the following information:
- Final quality score: {{score}}
- Improvement cycles executed: {{iteration}}
- Improvement history: {{improvement_log}}

Execute overall improvement process evaluation.
```

*Processing Module File (improvement_process.md)*:
```markdown
## Current Situation Analysis
Confirm current quality score {{score}} and display "Current score: {{score}}".

## Adaptive Improvement Processing
Execute the following improvement processing according to the {{score}} value:

If {{score}} is below 60:
→ Display "Executing basic improvement processing"
→ Add 12 to {{score}}
→ Append "Basic improvement: +12 points" to {{improvement_log}}

If {{score}} is 60 or above but below 75:
→ Display "Executing intermediate improvement processing"  
→ Add 8 to {{score}}
→ Append "Intermediate improvement: +8 points" to {{improvement_log}}

If {{score}} is 75 or above but below 85:
→ Display "Executing advanced improvement processing"
→ Add 5 to {{score}}
→ Append "Advanced improvement: +5 points" to {{improvement_log}}

If {{score}} is 85 or above:
→ Display "Executing fine-tuning processing"
→ Add 2 to {{score}}
→ Append "Fine-tuning: +2 points" to {{improvement_log}}

## Improvement Result Recording
Display the improved new score {{score}}.

Confirm the type and effect of the executed improvement and display "Improvement processing complete".
```

### 🔄 Three Patterns of Termination Conditions

#### 1. Pure Conditional Termination
```markdown
Continue processing until {{score}} reaches target value:
→ No count limit, termination judgment by condition only
→ Reliable goal achievement, predictable convergence
```

#### 2. Multiple Condition Termination
```markdown
Continue until any of the following is satisfied:
→ Quality goal achieved OR zero errors achieved OR improvement stagnation detected
→ Complex termination judgment, flexible control
```

#### 3. Safety Mechanism Termination
```markdown
Main condition: {{score}} >= target value
Safety limit: Maximum {{max_iterations}} times
→ Infinite loop prevention, practical limit setting
```

**Key Learning Points**: 
1. **Separation of loop control and processing logic** manages complexity
2. **Consistent state variable management** realizes predictable behavior  
3. **Appropriate termination condition design** balances practicality and safety
4. **External module execution** enables reusable component design

### 📁 Practical Samples

Detailed practical examples of Loop & Modular Programming:

- **Beginner**: [Learning Progress Management System](./examples/loop_modular/learning_progress.md) - Iterative learning for score improvement
- **Intermediate**: [Presentation Quality Optimization System](./examples/loop_modular/presentation_optimizer.md) - Multi-axis iterative improvement

---

### Pattern 5: Problem Solving & Recursion

**Overview**: Advanced pattern for recursively dividing complex problems using TODO tools and solving them step by step. Decomposes large problems into understandable units, accumulates reliable progress, and achieves final integrated solutions.

**Processing Flow**: `Problem Analysis → Decomposition Judgment → [Recursive Division | Concrete Execution] → Integrated Solution`

**Application Criteria**:
- ✅ Complex multi-stage problem solving needed
- ✅ Problem structure that can be divided step by step
- ✅ Reliable progress management and state retention important
- ✅ Long-term tasks with interruption and resumption capability
- ❌ Simple processing not requiring division (→Consider [Sequential Pipeline](./examples/sequential/))

**Value of Recursive Thinking**:
- **Decomposition**: Divide large problems into understandable units
- **Judgment**: Appropriate evaluation of decomposability of each task
- **Execution**: Concrete completion of non-decomposable tasks
- **Integration**: Systematic combination of distributed results

### 🎯 3-Step Gradual Learning

#### Step 1: TODO Tool Basic Operations
```markdown
## TODO List Basic Operation Experience

Master basic TODO tool operations with simple task "Create shopping list":

Confirm current TODO list.

Add the following tasks to TODO list:
1. "Food confirmation" - Priority: High
2. "Create shopping list" - Priority: High  
3. "Execute shopping" - Priority: Medium

Execute each task sequentially and update status to "completed" upon completion.

Finally confirm all tasks are completed.
```

#### Step 2: Basic Problem Division
```markdown
## Simple Problem Division System

Divide main task "Weekend cleaning plan" and manage with TODO list:

Divide main task into following subtasks and add to TODO list:
1. "Living room cleaning" - Priority: High
2. "Kitchen cleaning" - Priority: High
3. "Bathroom cleaning" - Priority: Medium
4. "Trash disposal" - Priority: Low

For each subtask:
- Determine specific work content
- Update status to completed after work completion
- Report overall cleaning plan results after all completion
```

#### Step 3: Recursive Problem Solving
```markdown
## Advanced Recursive Division System

Recursive implementation with main task "Recipe creation":

## Phase 1: Initial Problem Division
Decompose main task into major subtasks and add to TODO list

## Phase 2: Recursive Decomposition Judgment
For each pending task:
- Judge decomposability
- If decomposable → Create detailed subtasks and add to TODO
- If no decomposition needed → Execute concrete work and mark completed

## Phase 3: Continuous Processing
Repeat Phase 2 as long as pending tasks remain

## Phase 4: Final Integration
After all task completion, integrate results and present as complete recipe
```

### 🔄 Three Benefits of TODO List Tool

#### 1. Complexity Management
```markdown
Large Problem → Understandable Units → Gradual Solution:
→ Division considering human cognitive limits
→ Reliable understanding and execution at each step
```

#### 2. Reliable Progress Assurance
```markdown  
Non-decomposable → Concrete Execution → Completed → Accumulation:
→ Each task completion guarantees overall progress
→ Design leaving no half-finished states
```

#### 3. Interruption and Resumption Capability
```markdown
TODO List → State Retention → Session Spanning → Continued Processing:
→ Flexible management of long-term projects
→ Possible work sharing among multiple people
```

**Key Learning Points**: 
1. **Recursive decomposition thinking** masters programming-like problem solving
2. **TODO tool coordination** realizes reliable state management
3. **Decomposition judgment logic** learns appropriate granularity control
4. **Integration process** practices systematization of distributed results

### 📁 Practical Samples

Detailed practical examples of Problem Solving & Recursion:

- **Beginner**: [Task Decomposition System](./examples/problem_recursion/task_decomposition.md) - Recursive division practice through curry recipe creation (Execution time: 3-5 minutes)
- **Intermediate**: [Project Management System](./examples/problem_recursion/project_management.md) - Complex hierarchical management and complete event planning decomposition (Execution time: 8-12 minutes)

---

### Pattern 6: Learning from Experience

**Overview**: Advanced pattern where agents save processing results to persistent files and improve decision-making quality by learning from accumulated experience. Gradually constructs from simple experience recording to similarity-based knowledge search and failure pattern recognition.

**Processing Flow**: `Experience Recording → Knowledge Accumulation → Experience Search → Knowledge Utilization`

**Application Criteria**:
- ✅ Want to improve judgment accuracy using past experience
- ✅ Want to implement continuous learning and improvement processes  
- ✅ Want to efficiently utilize insights from similar situations
- ✅ Want to construct failure pattern prediction and avoidance systems
- ❌ One-time processing where memory is unnecessary (→Consider basic patterns)

**Value of Experience Learning**:
- **Memory**: Persistence of past success and failure cases
- **Learning**: Extract patterns from experience and convert to insights
- **Search**: Efficient discovery of related experiences in similar situations
- **Utilization**: Improved decision-making based on accumulated knowledge

### 🍳 Basic Example: Cooking Experience Accumulation Learning System

First, practice the basic concept of Learning from Experience through the experience recording→accumulation→utilization cycle:

```markdown
## Initial Cooking Experiment
Trying to make "Fried Rice" for today's dinner.

Ingredients used: 2 cups rice, 2 eggs, green onions, soy sauce, salt
Cooking time: 20 minutes
Evaluation: Bland taste, somewhat sticky (5/10 points)

## Experience Recording
Save the following cooking experience to learning_memory.json for persistence:

{
  "cooking_experiences": [
    {
      "date": "today",
      "dish": "Fried Rice",
      "ingredients": ["2 cups rice", "2 eggs", "green onions", "soy sauce", "salt"],
      "cooking_time": 20,
      "score": 5,
      "problems": ["bland taste", "somewhat sticky"],
      "lessons": "Need seasoning adjustment, strengthen heat"
    }
  ]
}

## Improvement Practice
Load learning_memory.json and set to {{past_experience}}.

Using lessons from {{past_experience}}, make improved fried rice:

Improved ingredients: 2 cups rice, 2 eggs, green onions, soy sauce (more), salt, chicken stock, sesame oil
Cooking time: 18 minutes
Evaluation: Rich taste, fluffy texture (8/10 points)

Add this improvement result to {{past_experience}} and save to learning_memory.json.

## Learning Completion and Cleanup
Display "Cooking learning cycle complete!"

For next execution, delete learning_memory.json file.
```

**Learning Points**:
- **Experience Recording**: Persist specific results in JSON format
- **Lesson Extraction**: Derive specific improvement points from problems
- **Knowledge Utilization**: Improvement practice referencing past experience

### 🔄 Continuous Learning: Loop Pattern + Learning from Experience

In the number guessing game learning system, gradually acquire efficient search strategies using past estimation history:

```markdown
## Game Initial Setup
Select secret number randomly from 1 to 100 and set to {{secret_number}}.
(For verification, please display the secret number)

Load game_history.json and set to {{game_history}}.
Set estimation count to 0 as {{attempt_count}}.

## Learning Estimation Loop
Repeat the following until {{attempt_count}} reaches 10 or correct answer:

Add 1 to {{attempt_count}}.

Display "=== Estimation Count {{attempt_count}} ===".

## Estimation Value Decision Based on Past History
Refer to {{game_history}} to determine next estimation value.

First time case:
→ Select estimation value between 1 and 100

Second time onwards case:
→ Confirm {{game_history}} content and determine next estimation value by your method

Set estimation value to {{current_guess}} and display "Estimation value: {{current_guess}}".

## Feedback Judgment
Calculate difference between {{current_guess}} and {{secret_number}} and provide following gradual feedback:

Difference 20 or more case:
→ {{current_guess}} < {{secret_number}}: "{{current_guess}} is much too small"
→ {{current_guess}} > {{secret_number}}: "{{current_guess}} is much too large"

Difference 5-19 case:
→ {{current_guess}} < {{secret_number}}: "{{current_guess}} is a little small"
→ {{current_guess}} > {{secret_number}}: "{{current_guess}} is a little large"

Difference 1-4 case:
→ "{{current_guess}} is very close!"

Difference 0 case:
→ Display "Correct! {{current_guess}} is the secret number!" and end loop

## History Update
Add estimation result to {{game_history}} and save to game_history.json:
- Estimation count
- Estimation value
- Feedback result
- What you noticed (optional)

## Final Learning Results
After game completion, reflect on learning process from {{game_history}}:
"Number guessing learning complete! Reached correct answer in {{attempt_count}} attempts"
"Freely analyze learning effects and strategies you discovered"

## Learning Completion and Cleanup
For next execution, delete game_history.json file.
```

**Key Learning Points**: 
1. **Experience persistence** realizes long-term memory across sessions
2. **Continuous learning cycle** constructs iterative improvement processes
3. **Insight extraction** discovers general principles from individual experiences
4. **State management** tracks and visualizes learning progress

### 📁 Practical Samples

Detailed practical examples of Learning from Experience:

- **Beginner**: [Writing Style Analysis & Improvement System](./examples/learning_experience/writing_style_learning.md) - Writing experience recording, accumulation, and utilization through JSON persistence (Execution time: 5-8 minutes)
- **Intermediate**: [Prompt Continuous Improvement System](./examples/learning_experience/prompt_improvement_learning.md) - Gradual prompt optimization learning through Loop Pattern integration (Execution time: 8-12 minutes)

---

### Pattern 7: Environment Sensing, Knowledge-base and Environment Model

**Overview**: Knowledge systems and model construction techniques for agents to understand environments and make optimal situation-based decisions. Adds "environment understanding" and "situation judgment" intellectual capabilities to basic pattern execution abilities, realizing more practical and adaptive agent systems.

**Processing Flow**: `Environment Sensing → Knowledge Matching → Situation Estimation → Experience Integration → Action Judgment`

### 📚 Agent Environment Understanding System

**Basic Concept**: Agent systems need to systematically maintain and utilize knowledge about the "environment" in which they operate

**Three-layer Structure of Environment Knowledge**:
```
Environment Knowledge = LLM Common Sense + Knowledge Base + Environment Model
```

**Information Integration Judgment Process**:
```
Sensing Information + Knowledge Base + Environment Model + Experience Learning → Action Judgment
```

### 🔍 Environment Sensing

**Definition**: Basic function for agents to acquire information from real-world and digital environments and understand current situations

**Application Criteria**:
- ✅ Need temporal information like time and date
- ✅ Want to confirm current state of files and databases
- ✅ Want to acquire external system and web information
- ❌ Static information is sufficient (→Handle with knowledge base)

**Systematic Sensing Techniques**:

#### Temporal Information Acquisition
```markdown
## Current Time Acquisition
Execute date command to confirm current date/time and save to {{current_time}}.

## Day-of-week Processing
Determine day of week from {{current_time}} and execute the following:
- Weekday case: Execute business mode processing
- Weekend case: Execute maintenance mode processing
```

#### File and Data State Acquisition
```markdown
## File State Confirmation
Load project_status.json and set to {{project_state}}.

## Data Integrity Check
Analyze {{project_state}} content:
- Confirm completeness of required items
- Verify data update date/time
- Detect abnormal values and missing values
```

#### External Information Acquisition
```markdown
## Web Information Collection
Research "latest technology trends" on web and save 3 important points to {{tech_trends}}.

## Information Reliability Evaluation
For {{tech_trends}}:
- Evaluate information source reliability
- Confirm information freshness
- Obtain confirmation from multiple sources
```

**Practical Example: Weekly Task Management Agent**

Example implementing core agent programming concept "**Environment Sensing→Judgment→Action**":

```markdown
## Environment Sensing: Current Day Acquisition
Execute date command to confirm current day of week and save to {{current_day}}.

## Day-based Task Execution
Execute the following according to {{current_day}} and save results to {{daily_result}}:

Monday case:
→ Execute week-start planning (1-week goal setting)

Tuesday-Thursday case:
→ Execute focused work mode (important task progress confirmation)

Friday case:
→ Execute weekend preparation mode (week reflection and next week preparation)

Saturday-Sunday case:
→ Execute refresh mode (rest and recharge activities)

## Agent Operation Report
Combine {{current_day}} and {{daily_result}} to create today's agent operation report.
```

**Sensing Elements**:
- **Real-world Information**: Time and day acquisition through date command
- **Digital Information**: File and database state confirmation
- **External Information**: Latest information acquisition through web search and API calls
- **State Changes**: Detection of changes and differences from previous execution

### 📖 Knowledge Base

**Definition**: Structured business-specific knowledge in text or JSON format

**Application Criteria**:
- ✅ Business-specific rules and procedures exist
- ✅ Have documented knowledge like FAQ and manuals
- ✅ Need specialized field knowledge systems
- ❌ Can handle with common sense only (→LLM basic knowledge sufficient)

**Implementation Formats**:

#### Text Format Knowledge Base
```markdown
## Customer Support Knowledge Base (customer_kb.md)
### Return Policy
- Within 30 days of purchase
- Unopened and unused items only
- Receipt required

### Frequently Asked Questions
Q: How many days for delivery?
A: Usually 3-5 business days, express delivery next day

### Escalation Criteria
- Refund requests → Manager approval required
- Technical issues → Transfer to technical support team
```

#### JSON Format Knowledge Base
```json
{
  "business_rules": {
    "discount_policy": {
      "vip_customer": 0.15,
      "regular_customer": 0.05,
      "minimum_order": 5000
    },
    "support_hours": {
      "weekday": "9:00-18:00",
      "weekend": "10:00-16:00"
    }
  },
  "contact_info": {
    "technical_support": "tech@company.com",
    "billing": "billing@company.com"
  }
}
```

**Usage Example: Knowledge Base Reference System**
```markdown
## Customer Inquiry Response
Load customer_kb.md and set to {{knowledge_base}}.

## Inquiry Content Analysis
Set customer inquiry "Delivery seems delayed, what's happening?" to {{inquiry}}.

## Knowledge Matching and Response Generation
Refer to {{knowledge_base}} to generate an optimal response to {{inquiry}} and save to {{response}}.

## Response History Recording
Record {{inquiry}} and {{response}} to support_log.json for persistence.
```

### 🌍 Environment Model

**Definition**: Digital twin that captures the environment as a "system with state" and performs state estimation and prediction

**Application Criteria**:
- ✅ Need to track environment state changes
- ✅ Want to understand interactions of multiple elements
- ✅ Future state prediction is important
- ❌ Static information reference only (→Knowledge base sufficient)

**State Representation Design**:

#### Basic State Management
```json
{
  "system_state": {
    "timestamp": "2025-06-20T10:30:00Z",
    "inventory": {
      "product_a": 150,
      "product_b": 75,
      "product_c": 0
    },
    "active_orders": 12,
    "staff_status": {
      "available": 5,
      "busy": 3,
      "offline": 2
    }
  }
}
```

**Usage Example: Inventory Management Agent**
```markdown
## Current Situation Acquisition
Load inventory_status.json and set to {{current_state}}.

## New Order Processing
Set new order "Product A × 20 units" to {{new_order}}.

## State Update Execution
Based on {{current_state}} and {{new_order}}:
- Update inventory quantities
- Judge stock shortage warnings
- Determine automatic ordering necessity

Save the updated state to {{updated_state}} and persist to inventory_status.json.

## Prediction and Alert Function
Analyze {{updated_state}} and extract products expected to be out of stock within 24 hours to {{alerts}}.
```

### 🔄 Integrated Judgment System

**Advanced judgment system integrating 4 information sources**:
`Environment Sensing + Knowledge Base + Environment Model + Experience Learning`

**Practical Example: Meeting Assistant Agent**
```markdown
## Environment Information Collection
Confirm current time with date command and set to {{current_time}}.
Load meeting_schedule.json and set to {{schedule}}.
Load participant_profiles.json and set to {{participants}}.

## Situation Judgment Execution
Integrate {{current_time}}, {{schedule}}, {{participants}}:

15 minutes before meeting case:
→ Send advance reminders to participants
→ Confirm material preparation status
→ Check meeting room equipment operation

During meeting case:
→ Start automatic meeting minutes recording
→ Manage participant speaking time
→ Extract action items

After meeting case:
→ Organize and distribute meeting minutes
→ Set action item follow-ups
→ Propose next meeting schedule

Save the results to {{meeting_action}}.

## Experience Learning Integration
Load similar meeting success patterns from past_meetings.json to {{lessons}} and
utilize for {{meeting_action}} improvement.

Append updated insights to past_meetings.json for persistence.
```

### 🎯 Coordination of Knowledge base and Environment model

**Complementary Utilization**:
- **Knowledge Base**: Invariant rules and knowledge ("what should be done")
- **Environment Model**: Dynamic state and prediction ("what is currently happening")
- **Integrated Judgment**: Optimal action decision combining both

**Pattern Integration Utilization**:
- **Sequential Pipeline**: Sequential processing of knowledge matching→situation judgment→action execution
- **Conditional Execution**: Conditional branching processing according to state
- **Learning from Experience**: Knowledge and model updates from judgment results
- **Parallel Processing**: Parallel reference and integration of multiple knowledge sources

**Key Learning Points**:
1. **Appropriate knowledge separation** to distinguish between knowledge base and environment model usage
2. **State management design** to reliably capture important environment changes
3. **Multiple information integration** to realize judgment leveraging characteristics of each information source
4. **Continuous updates** to gradually improve knowledge and model accuracy

### 📁 Practical Samples

Detailed practical examples of Environment sensing, Knowledge-base and Environment model:

- **Beginner**: [Time-aware User State Estimation System](./examples/environment_sensing/time_based_user_model.md) - State estimation and response adaptation through time sensing
- **Beginner**: [Presentation Structure Advisor](./examples/knowledge_base_patterns/presentation_advisor/presentation_advisor.md) - Individual requirement-responsive structure generation through specialized knowledge

---

### Pattern 8: Human-in-the-Loop (HITL)

**Overview**: Advanced pattern that strategically incorporates human judgment, creativity, and supervision into agent automated processing, constructing safe and responsible systems while maintaining efficiency. Overcomes limitations of complete automation through appropriate intervention point design, realizing complementary human-AI collaboration.

**Processing Flow**: `Automated Processing → Intervention Judgment → [Human Intervention | Continue Execution] → Result Integration → Record Retention`

**Application Criteria**:
- ✅ Creative judgment and strategic direction are important
- ✅ High-risk decisions and responsibility clarification needed
- ✅ Safety assurance and misconduct prevention important
- ✅ Quality standards and final approval needed
- ❌ Routine, low-risk processing (→Consider complete automation)
- ❌ High-frequency cases where intervention costs exceed benefits

**Four Values of HITL**:
- **Creativity Introduction**: Incorporate human intuition and ideas into agent processing
- **Direction Adjustment**: Human correction of strategic judgment and priorities
- **Safety Assurance**: Prevention of unexpected misconduct and harmful outputs
- **Responsibility Clarification**: Human approval and responsibility recording for important decisions

### 🎯 Efficient Intervention Design Principles

**Intervention Point Optimization Concept**:
```
Intervention Effect = (Judgment Quality Improvement + Risk Reduction) - (Time Cost + Complexity Cost)
```

**Strategic Intervention Points**:
1. **Concept and Planning Stage**: Confirmation of overall direction and strategy
2. **Important Branch Points**: Decision-making from multiple options
3. **Quality Confirmation Stage**: Verification of deliverable validity and safety  
4. **Final Approval Stage**: Confirmation of decisions involving responsibility

**Balance Design Maintaining Efficiency**:
- **Hierarchical Intervention**: Adjust intervention density according to importance
- **Conditional Intervention**: Intervention design only under specific conditions
- **Parallel Processing**: Continue parallel work during human judgment
- **Pre-setting**: Speedup through pre-agreement on judgment criteria

### 🤝 Four Claude Code Implementation Patterns

#### 1. Approval Waiting Pattern
```markdown
## Approval Waiting for Important Decisions
Please approve the following proposal:
- Proposal content: {{proposal_content}}
- Expected effects: {{expected_effect}}
- Risk assessment: {{risk_assessment}}

Please respond with "Approved" or "Revision Required".
Will not proceed to next step until approval.

Please set your judgment to {{human_decision}}.
```

#### 2. Option Presentation Pattern
```markdown
## Strategy Selection
In {{current_situation}} situation, the following options are available:

A. {{option_a}} - Benefits: {{merit_a}}, Risks: {{risk_a}}
B. {{option_b}} - Benefits: {{merit_b}}, Risks: {{risk_b}}  
C. {{option_c}} - Benefits: {{merit_c}}, Risks: {{risk_c}}

Which option do you choose? (A/B/C)
Please also provide selection reasoning.

Please set your choice to {{human_choice}}.
```

#### 3. Feedback Integration Pattern
```markdown
## Deliverable Quality Confirmation
Created {{generated_content}}.

Please provide feedback from the following perspectives:
- Content accuracy: Are there any problems?
- Safety: Are there any inappropriate expressions?
- Improvement suggestions: Are there points to add or modify?

Please set feedback to {{human_feedback}}.
```

#### 4. Record Retention Pattern
```markdown
## Human Intervention Record Persistence
Save the following intervention record to hitl_log.json:

{
  "timestamp": "{{current_time}}",
  "intervention_type": "{{intervention_type}}",
  "human_decision": "{{human_decision}}",
  "context": "{{decision_context}}",
  "rationale": "{{human_rationale}}",
  "system_state": "{{system_state}}"
}
```

### 🛡️ Basic Example: Safe Article Creation System

Article creation system practicing basic HITL concepts with approval waiting incorporation:

```markdown
## Article Theme Setting
For article theme "Latest AI Technology Trends", propose the following structure:

1. Current state analysis of AI technology
2. Notable technology trends  
3. Industry impact predictions
4. Future prospects

Is it okay to proceed with this structure?
If there are points to modify or add, please provide instructions.

Please set your approval to {{structure_approval}}.

## Content Generation
Based on {{structure_approval}}, generate content for each section and set to {{draft_content}}.

## Safety Confirmation
Please confirm the following for {{draft_content}}:
- Factual accuracy
- Presence of bias or inappropriate expressions
- Descriptions that could cause misunderstandings

If there are problems, please provide specific revision instructions.
If no problems, please respond with "Approved".

Please set your quality confirmation results to {{quality_check}}.

## Final Output
Only if {{quality_check}} is "Approved", save the final article to article_output.md.

## Intervention Recording
Record this series of intervention processes to hitl_log.json:
- Structure approval: {{structure_approval}}
- Quality confirmation: {{quality_check}}
- Revision count: {{revision_count}}
```

**Learning Points**:
1. **Staged approval** realizes human intervention at important judgment points
2. **Explicit waiting** controls automated processing and clarifies responsibility
3. **Feedback integration** reflects human insights into system
4. **Record retention** ensures transparency of decision-making process

**Key Learning Points**:
1. **Appropriate intervention frequency** balances efficiency and safety
2. **Clear judgment criteria** reduce human burden and promote quick decisions
3. **Flexible modification function** effectively utilizes human feedback
4. **Responsibility visualization** ensures transparency and accountability of decisions

### 📁 Practical Samples

Detailed practical examples of Human-in-the-Loop:

- **Beginner**: [Creative Blog Article Creation System](./examples/human_in_the_loop/creative_blog_writer.md) - Human-collaborative article creation with strategic intervention points
- **Intermediate**: [Investment Decision Support System](./experiments/investment_decision_support/experiment.md) - Responsibility clarification and staged approval process for high-risk decisions

---

## Pattern 9: Error Handling

### Overview

The Error Handling pattern provides methods for dealing with various types of problems that occur during system execution. It is an essential pattern for building robust agent systems.

**Two Approaches**:
1. **Try-Catch-Finally (Traditional Exception Handling)**: Responding to unexpected runtime errors
2. **Graceful Degradation (Gradual Quality Adjustment)**: Adapting to foreseeable constraints and limitations

By combining these two approaches, robust systems capable of handling various situations can be constructed.

### 9-1: Try-Catch-Finally (Traditional Exception Handling)

Realizes a structure similar to try-catch-finally in programming languages using natural language. Defines explicit recovery processes for unexpected runtime errors such as API call failures, network errors, and tool bugs.

#### Basic Syntax Pattern

```markdown
## Main Task Execution
Try the following process:

Execute primary_task.md.

If it fails (Catch):
Execute backup_task.md.

Finally:
Record the execution result (success or failure) to execution_log.txt.
```

#### Practical Patterns

**1. API Call Redundancy**
```markdown
## Data Retrieval Process
Try the following process:

Retrieve data from the main API and save to {{api_data}}.

If it fails:
Retrieve the same data from the backup API and save to {{api_data}}.

Finally:
Record the retrieval status to {{api_status}} and save to api_log.json.
```

**2. File Operation Safety Assurance**
```markdown
## File Writing Process
Try the following process:

Write {{report_data}} to final_report.md.

If it fails:
Write {{report_data}} to backup_report.md and
display the message "Main file writing failed."

Finally:
Record the writing result to the processing log.
```

**3. External Tool Execution Reliability Improvement**
```markdown
## Multi-tool Verification
Try the following process:

Execute the task using Tool A.

If it fails:
Execute the same task using Tool B.

If that also fails:
Create instructions for manual processing and notify the administrator.

Finally:
Record the execution result and tools used to the execution history.
```

### 9-2: Graceful Degradation (Gradual Quality Adjustment)

A technique that continues to provide valuable results by gradually adjusting quality when ideal operation is difficult, rather than complete failure. It maintains maximum functionality under constrained environments.

#### Basic Concept

Even when the system cannot operate ideally, quality is adjusted gradually in the following priority order:
1. **Ideal Operation**: Complete functionality and quality
2. **Practical Operation**: Maintain main functions, partial limitations
3. **Minimum Operation**: Provide only core value

#### Practical Patterns

**1. Response to Resource Constraints**
```markdown
## Report Generation Process
When sufficient time and resources are available:
- Complete market analysis
- Detailed graph creation
- Comprehensive recommendations

When time is limited:
- Analysis of main indicators only
- Simple graph creation
- Important recommendations only

In emergency situations:
- Summary of most important data only
- Text-based concise reporting
```

**2. Adaptation to Data Quality**
```markdown
## Analysis Accuracy Adjustment
When data is completely available:
Execute high-precision statistical analysis and save to {{detailed_analysis}}.

When some data is missing:
Execute approximate analysis with available data and save to {{approximate_analysis}}.

When data is significantly insufficient:
Execute trend analysis only and save to {{trend_analysis}}, and
record "Detailed analysis could not be executed due to data shortage."
```

**3. Response to Tool Availability**
```markdown
## Gradual Information Collection
When web search tools are available:
Execute comprehensive research including latest information.

When web search is unavailable:
Extract relevant information from existing knowledge base.

When both are difficult:
Provide basic information based on general knowledge and
add the note "Latest information verification recommended."
```

### Error Handling Integration Example

Example of a robust system combining Try-Catch-Finally and Graceful Degradation:

```markdown
## Market Analysis Report Generation System
Try the following process:

Retrieve information from the latest market data API and execute detailed analysis.

If API retrieval fails (Catch):
Switch to analysis using existing data (Graceful Degradation).

If existing data is also insufficient:
Execute outline analysis based on general industry trends (Further Degradation).

Finally:
- Record the analysis level executed
- Specify data sources and reliability levels
- Record improvement suggestions for next execution
```

### Learning Points

**Try-Catch-Finally**:
1. **Explicit Error Response**: Pre-define specific recovery procedures for failures
2. **Ensuring Redundancy**: Improve reliability through multiple execution paths
3. **Situation Recording**: Utilize success/failure information for future improvements
4. **Preparation for Unexpected Failures**: Avoid complete system shutdown

**Graceful Degradation**:
1. **Gradual Quality Adjustment**: Provide valuable results even when not perfect
2. **Adaptation to Constraints**: Optimization under resource or data limitations
3. **User Expectation Management**: Clear explanation of limitations
4. **Continuous Service**: Maintain system value through partial functionality provision

---

## 📜 Disclaimer

Please read the following terms carefully before using this "Claude Code Natural Language Macro Programming Guide." By using this guide, you agree to these terms.

1.  **No Warranties**
    This guide, including all information, sample code, and techniques, is provided on an "as-is" basis without any warranties of any kind, express or implied. The authors do not warrant the accuracy, completeness, usefulness, or fitness for a particular purpose of the content provided.

2.  **Probabilistic Nature of Operation**
    The techniques described in this guide rely heavily on the probabilistic nature of Large Language Models (LLMs). Therefore, there is no guarantee that they will always produce the expected results or behave as described, even when instructions are followed verbatim. Outputs may vary with each execution.

3.  **Limitation of Liability**
    In no event shall the authors or contributors be liable for any damages arising from the use of this guide. This includes, but is not limited to, direct, indirect, incidental, or consequential damages such as data loss, business interruption, or loss of profits.

4.  **Use at Your Own Risk**
    Your use of the techniques and information in this guide is entirely at your own risk. You must exercise extreme caution when using features that can affect your system environment, such as file operations or command execution (e.g., Bash). **Never run these commands in a production environment or on a system containing critical data. Always perform thorough testing in a safe, isolated environment first, and ensure you have adequate backups before proceeding.**

5.  **Security**
    You are solely responsible for implementing security measures when using the techniques in this guide. This includes avoiding execution of untrusted code, properly managing permissions, and being cautious with automated file operations or system commands.

6.  **Third-Party Services**
    This guide refers to features of Claude, a product of Anthropic. The authors of this guide are independent of Anthropic, and this guide is not an official publication. The terms of service and specifications of Claude are subject to change, which may render parts of this guide obsolete.

7.  **Content Modification**
    The content of this guide may be changed or removed without prior notice.

---

# Appendix

## A.1: System Control via Claude Code Slash Commands

When agents perform tasks, they need to be mindful of resource constraints (budget, API call limits, time allowances, computational costs, etc.). Real-world agents do not possess infinite resources, and cost-conscious decision-making under resource constraints is essential for practical systems.

### What are Slash Commands?

**Slash commands** are special commands in Claude Code that begin with "/". They can be executed directly during natural language conversations and enable checking and controlling Claude Code's system state. Unlike traditional command-line operations, they can be executed seamlessly within the flow of dialogue.

#### Main Built-in Commands

Claude Code provides the following built-in slash commands:

- `/help` - Display list and descriptions of available commands
- `/clear` - Reset conversation history and context (memory optimization)
- `/model` - Switch between Claude models (Opus/Sonnet, etc.)
- `/ide` - Check IDE integration status (open files, linter errors, etc.)
- `/init` - Automatically generate CLAUDE.md file
- `/permissions` - Manage tool allowlists


### Key Points

**1. Actual System Information Retrieval**
- Real-time development environment status checking via `/ide`
- Dynamic discovery of available functions via `/help`
- Decision-making based on actual system state

**2. Dynamic Environment Control**
- Timely memory management via `/clear`
- Optimization according to processing characteristics via `/model`
- Dynamic adjustment based on performance requirements

**3. Integration with Conditional Branching**
- Processing branches based on system state
- Determining next actions based on execution results
- Practical workflow automation

The use of slash commands enables practical agent design that leverages Claude Code's system capabilities.

## A.2: Event-Driven Execution and System Integration

Many processes in the real world occur asynchronously. Systems that can immediately respond to external stimuli such as file creation, email reception, and sensor value changes are required to have high responsiveness. Event-Driven execution is a primitive that asynchronously listens for specific events and executes corresponding tasks when detected.

### What is Event-Driven?

**Event-Driven execution** is an execution model that starts tasks asynchronously triggered by external events, in contrast to Sequential Pipeline which is synchronous. Agents monitor events in a waiting state and automatically begin processing when specific conditions are met.

### External Trigger Model

The most practical and robust approach is a hybrid design that delegates event monitoring to existing proven technologies and allows the LLM to focus on post-trigger processing.

#### Main Implementation Technology Examples

**1. Time Triggers with cron**
- Automatic invocation at specified times
- Basic implementation method for scheduled tasks

**2. File Monitoring with watchdog**
- File system monitoring using Python's watchdog library
- Detection of file creation, modification, and deletion events
- Continuous monitoring of specified directories with immediate response

**3. inotify System**
- Linux native file system monitoring functionality
- Efficient event detection at low level

### Integration Patterns

Typical integration example: "Continuously monitor directory `/orders`, and when a new file (e.g., `order123.json`) is created, evaluate `order_processing.md` with that file path as an argument" by running a resident script.

### Key Points

**1. Asynchronous Processing Implementation**
- Immediate response to external events
- Parallel monitoring of multiple events
- Improved system-wide responsiveness

**2. Flexibility in Technology Selection**
- Choice of monitoring technology according to requirements
- Easy integration with existing systems
- Adaptability to operational environments

**3. Integration with Macro Files**
- Separation of event information and processing logic
- Dynamic modification of processing content
- Construction of reusable processing patterns

Event-Driven execution enables the construction of agent systems with high responsiveness for real-time systems and business automation.

## A.3: Risk Mitigation Strategies for Mission-Critical Environments

### Background and Challenge Recognition

Natural Language Macro Programming is expected to be utilized across diverse fields due to its intuitiveness and high explainability. However, uncertainties derived from the probabilistic behavioral characteristics of LLMs (Large Language Models) can pose significant risks in specific environments.

**Challenges from Probabilistic Uncertainty**:
- Difficulty in guaranteeing 100% operational reliability in principle
- Possibility of unexpected interpretations or execution results
- Discrepancy with reliability requirements in mission-critical decisions
- Application constraints in fields with strict legal responsibility and safety requirements

**Purpose of This Section**:
To achieve safe and responsible utilization of natural language macro programming through a three-layer defense strategy (proactive design prevention, runtime error handling, auditing and continuous improvement) to approach the reliability levels required by traditional deterministic systems.

### Layer 1: Proactive Design Measures (Proactive Design)

Incorporate risk reduction mechanisms in advance during the workflow design stage.

#### 1. Strategic Placement of Human-in-the-Loop (HITL)

**Approval Gate Design at Critical Points**:

```markdown
## Approval Process for Critical Decisions
Please review the following processing content:
{{proposed_action}}

This process includes irreversible changes.
Please respond with "Approved" or "Revision Required".
Will not proceed to next step without approval.

Save approval result to {{human_approval}}.

## Safety Control through Conditional Branching
Only when {{human_approval}} is "Approved":
Execute critical_operation.md

Otherwise:
Stop processing and transition to revision pending state.
```

**Implementation Points**:
- Must be placed immediately before irreversible operations (file deletion, external API calls, financial transactions, etc.)
- Utilize "Approval Waiting Pattern" from "Human-in-the-Loop" pattern
- Predefine clear approval and rejection criteria

#### 2. Graceful Degradation Design

Design that continues to provide limited but valuable service when ideal conditions are not available, rather than immediately stopping the system.

```markdown
## Staged Alternative Processing for API Connections
Try the following process:
Retrieve latest data from external API and save to {{latest_data}}

If it fails (Catch):
Retrieve latest available data from local cache and save to {{cached_data}}
Set warning "Note: Data is from {{cache_date}}" to {{warning}}

Finally:
Continue analysis using {{latest_data}} or {{cached_data}}
Include {{warning}} in results if quality degradation warning exists
```

#### 3. Execution Permission Minimization

Minimize permissions granted to the system and implement strict access control for functions involving risks.

```markdown
## Permission Control Implementation Example
/permissions Allow file reading and text generation only

When dangerous command execution is required:
"This operation requires system administrator privileges.
Request manual execution by administrator."
Pause processing and wait for human intervention
```

### Layer 2: Runtime Error Handling

Prevent the system from falling into catastrophic states when unexpected errors occur.

#### 1. Redundancy through Try-Catch-Finally

```markdown
## Robust External Integration Processing
Try the following process:
Retrieve important data from main API

If it fails (Catch):
Retrieve similar data from backup API
Record that source is different in {{data_source_warning}}

If backup also fails (Catch):
Search existing database for available alternative data
Set "Data freshness is limited" to {{limitation_note}}

Finally:
Clearly record retrieved data and its limitations
Report quality level along with processing results
```

#### 2. State Persistence and Recovery Mechanisms

Address the risk of process interruption, especially for long-running tasks.

```markdown
## Design for Interruptible Long-term Processing
Save progress to progress_state.json at each stage of long-term tasks:

Upon Step 1 completion:
{"completed_steps": ["data_collection"], "current_step": "analysis", "timestamp": "2025-01-15T10:30:00Z"}

Upon Step 2 completion:
{"completed_steps": ["data_collection", "analysis"], "current_step": "report_generation", "timestamp": "2025-01-15T11:45:00Z"}

## Recovery Processing
Check progress_state.json and resume processing from last completed step
Record "Processing resumed from {{timestamp}}" in log
```

### Layer 3: Auditing and Continuous Improvement

Record and analyze system behavior to reduce future risks.

#### 1. Log Recording Examples

```markdown
## Create Audit Log for All Processing
At execution start:
{"timestamp": "2025-01-15T09:00:00Z", "action": "process_start", "user_input": "{{original_request}}", "system_state": "{{initial_state}}"}

During Human-in-the-Loop intervention:
{"timestamp": "2025-01-15T09:15:00Z", "action": "human_intervention", "decision": "{{human_decision}}", "rationale": "{{human_rationale}}", "context": "{{decision_context}}"}

When error occurs:
{"timestamp": "2025-01-15T09:30:00Z", "action": "error_occurred", "error_type": "{{error_type}}", "error_message": "{{error_details}}", "recovery_action": "{{recovery_method}}"}

Persist all logs to audit_log.json
```

#### 2. Utilizing Learning from Experience

```markdown
## Converting Failure Patterns to Learning Data
Update learning database when errors occur:

Record in failure_patterns.json:
{
  "error_type": "API_timeout",
  "context": "high_traffic_period",
  "failed_action": "external_data_fetch",
  "successful_recovery": "switch_to_cached_data",
  "lesson_learned": "Prioritize cached data from the start during high traffic periods"
}

In similar situations next time:
Check past failure patterns and proactively use cached data
"Selected safe alternative based on past learning"
```

Understanding the probabilistic characteristics of natural language macro programming and implementing appropriate risk mitigation measures enables safe and responsible utilization across diverse fields.