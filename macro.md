# Claude Code Natural Language Macro Programming Guide

**Claude Code** is a specialized coding environment that extends Anthropic's AI assistant Claude ([Official Documentation](https://docs.anthropic.com/en/docs/claude-code)). It integrates powerful tool suites including file operations, Bash execution, and web search, supporting a wide range of tasks from programming to document creation. This guide presents methods for utilizing Claude Code not merely as a coding tool, but as an agent execution environment programmable through natural language.

## 🤖 Core Concept: Agent Programming Using Claude Code as Interpreter

This guide presents a **Natural Language Macro Programming** approach that treats **Claude Code as a natural language interpreter for realizing agent programming**.

While conventional programming requires computers to interpret programming languages with specific syntax, natural language macro programming enables:

- **Natural language and Markdown notation** as program descriptions
- **Claude Code** functioning as an interpreter that parses and executes these descriptions
- **Advanced control structures** (Task tool, TODO tool, variable management, conditional branching, parallel execution) realized through natural language
- **Agent systems** for automating and optimizing complex tasks

Even people without programming experience can design agent behaviors using intuitive natural language and have Claude Code execute them.

## ⚠️ Probabilistic Behavior Characteristics

The natural language macro programming techniques presented in this guide are based on the probabilistic operational characteristics of Large Language Models (LLMs):

- **High-probability operations**: Variable management (`{{variable_name}}`), external module execution (`filename.md execution`), etc., operate with very high probability as expected
- **Non-deterministic nature**: 100% deterministic operation cannot be expected due to LLM characteristics
- **Practical reliability**: Operates at a level with sufficient reliability for actual use
- **Graceful degradation**: Continues to provide partial value even when ideal operation is difficult

## 🎯 Learning Objectives

1. **Fundamental Concepts of Natural Language Macro Programming**
   - Information management and result passing
   - Implementation of conditional branching and multitask processing

2. **8 Design Patterns**
   - Sequential Pipeline
   - Parallel Processing
   - Conditional Execution
   - Loop & Modular Programming
   - Problem Solving & Recursion
   - Learning from Experience
   - Environment sensing, Knowledge-base and Environment model
   - Human-in-the-Loop

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

This research proposes a novel methodology called "Claude Code Natural Language Macro Programming," consisting of the following elements:

1. **Establishment of Systematic Design Patterns**
   - Construction of a graduated learning system through 8 design patterns
   - Design methodologies comprehensively covering from basic processing to advanced human collaboration
   - Development of reusable and extensible pattern libraries

2. **Natural Language Structured Description Methods**
   - Intuitive task description methods independent of programming syntax
   - Utilization of Markdown notation with high affinity to human cognitive processes
   - Description rules considering the balance between ambiguity control and structuring

3. **Graduated Learning Model Design**
   - Systematic progression from basic patterns (sequential, parallel, conditional) to advanced patterns (learning, environment understanding, human collaboration)
   - Educational approach integrating theoretical learning with practical application
   - Demonstration of versatility through application examples in diverse fields

### Shared Documentation in Collaboration with Claude Code

By including this document in the context, you can provide specific instructions such as: "For sales data, execute parallel analysis along 3 axes (regional, product, time series) using the Parallel Processing pattern, integrate results into {{analysis_result}}, and execute report creation through Sequential Pipeline." This enables specifying design patterns when having Claude Code create prompts, utilizing design patterns as a common language in human-AI collaboration.

### Significance and Future Prospects

The approach proposed in this research provides practical solutions to important challenges in AI technology social implementation—removing barriers to utilization due to technical complexity. Furthermore, it is expected to provide methodological foundations for future human-AI collaborative system design as a concrete implementation method for human-centered design in responsible AI development.

---

## 📋 Representative Syntax of Claude Code Natural Language Macro Programming

```markdown
- Conditional branching: Natural language conditional instructions ("if...", "depending on...", etc.)
- `{{variable_name}}`: Variable reference
- Variable storage: "Please save ... to {{variable_name}}"
- Persistent storage: "Please save {{variable_name}} to filename.json for persistence"
- File loading: "Please load filename.json and set to {{variable_name}}"
- External module execution: "Please execute filename.md"
- File search: "Please search for files containing 'keyword'"
- Parallel execution: "Please execute the following tasks in parallel:"
- Loop processing: "Please repeat the following process until [condition]:"
```

## 🔧 Basic Variable Management

Claude Code can manage variables through natural language instructions, enabling information passing between different processing steps.

### Variable Operations

```markdown
## Data Analysis Pipeline
Please analyze the sales data and save the results to {{analysis_result}}.

Based on {{analysis_result}}, create a summary report and save it to {{final_report}}.

Please save {{final_report}} to report.json for permanent storage.
```

### Control Structures

Conditional branching can be described flexibly in natural language:

```markdown
## Data Processing
If {{analysis_result}} shows positive growth, create an expansion plan.
If it shows negative growth, create a risk mitigation strategy.
Depending on the market situation, adjust the approach accordingly.
```

### Module Execution

Modular design is possible by calling external module files:

```markdown
## Data Processing Pipeline
1. Please execute data_collection.md
2. Please execute analysis.md  
3. Please execute report_generation.md
```

---

[Note: This is the beginning of the English translation. The complete guide contains detailed explanations of all 8 design patterns with examples. The full translation is being developed progressively.]

## 🚀 Next Steps

For the complete guide with all 8 design patterns and detailed examples, please refer to the progressive translation updates. Each pattern includes:

- Theoretical foundations
- Practical implementation examples
- Advanced use cases
- Integration with other patterns

## 📖 Pattern Overview

1. **Sequential Pipeline**: Step-by-step task processing with clear dependencies
2. **Parallel Processing**: Concurrent execution of independent tasks
3. **Conditional Execution**: Decision-based branching and adaptive behavior
4. **Loop & Modular Programming**: Iterative processes and reusable components
5. **Problem Solving & Recursion**: Complex problem decomposition strategies
6. **Learning from Experience**: Knowledge accumulation and continuous improvement
7. **Environment Sensing**: Context-aware processing and adaptive responses
8. **Human-in-the-Loop**: Human-AI collaborative design patterns

---

*This English version is under active development. For the complete Japanese version, please refer to the original repository.*