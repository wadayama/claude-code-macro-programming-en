# Claude Code Natural Language Macro Programming Guide

> 🌏 **日本語版も利用可能**: [Japanese documentation is available here](https://github.com/wadayama/claude-code-macro-programming) (日本語ドキュメントはこちら)

A guide to building agent systems using **Claude Code** as a natural language interpreter.

## ⚡ Quick Start

Try variable storage and reference:

**Store in variable**:
```
"Create 3 haiku poems about spring and save to {{haiku}}"
```

**Reference variable**:
```
"Select the most beautiful one from {{haiku}} and refine it"
```

Execute these directly in Claude Code to experience natural language macro programming.
(Note: CLAUDE.md macro definition is required)

## 🎯 Overview

## 🎯 10 Design Patterns

The core of natural language macro programming consists of 10 design patterns, systematically organized into **4 Basic Patterns** and **6 Advanced Patterns**.

### 📋 Basic 4 Patterns

#### Pattern 1: Sequential Pipeline
Basic execution pattern that processes tasks sequentially, passing results from one stage to the next

#### Pattern 2: Parallel Processing
Parallel execution pattern that runs multiple tasks simultaneously for efficient processing

#### Pattern 3: Conditional Execution
Conditional branching pattern that selects different processing paths based on situations

#### Pattern 4: Loop & Modular Programming
Efficient repetitive control through TODO-list based iteration and Few-shot Pattern Loop

### 🚀 Advanced 6 Patterns

#### Pattern 5: Problem Solving & Recursion
Recursive approach that breaks down complex problems step by step and solves them through TODO management

#### Pattern 6: Learning from Experience
Experience learning pattern that learns from past execution results and generates improvement suggestions

#### Pattern 7: Environment Sensing, Knowledge-base & Environment Model
Acquires external environment information, builds knowledge systems, and executes adaptive processing according to situations

#### Pattern 8: Human-in-the-Loop
Collaborative execution pattern that incorporates human judgment at appropriate timings

#### Pattern 9: Error Handling
Robustness improvement pattern that predicts errors and executes appropriate recovery processing

#### Pattern 10: Debug & Tracing
Development support pattern that visualizes execution status and assists in problem identification and resolution

### 🔧 Pattern Utilization and Integration

**Structure**: Combine Pattern 1-4 (Basic Patterns) and Pattern 5-10 (Advanced Patterns), along with Appendix (Specialized Technologies) to build practical systems.

**Integration Effects**: By combining multiple patterns, collaborative systems like the **A.5 Haiku Generation Multi-Agent** can be constructed.

**Appendix: Advanced Technical Elements and Practical Implementation**
- A.1: System Control and Resource Management
- A.2: Event-Driven Execution
- A.3: Four-Layer Defense Strategy
- A.4: Python Tool Integration
- A.5: Multi-Agent System Design (shared blackboard model, haiku generation multi-agent implementation example)
- A.6: Audit Log System (transparency and accountability tracking)
- A.7: LLM-based Pre-execution Inspection (LLM-powered pre-execution static analysis for security)
- A.8: Metaprogramming (dynamic macro generation, verification, evaluation, and improvement)
- A.9: Ensemble Execution and Consensus Formation (statistical countermeasures for probabilistic behavior)
- A.10: Type Safety and Schema Management (gradual type safety enhancement and schema-based systematic data management)
- A.11: LLM-based Post-execution Evaluation (quality, creativity, and logic evaluation for probabilistic systems)
- A.12: Variable Management Persistence and Scaling (robust state management via databases)
- A.13: Vector Database and RAG Utilization (dynamic knowledge systems through knowledge bases and experience learning)
- A.14: Goal-Oriented Architecture and Autonomous Planning (complete autonomous systems via 4-stage flow and PDCA cycle)
- A.15: Python Orchestration-Based Hybrid Approach (high-speed, cost-efficient systems via Python orchestration + natural language macros)
- A.16: SQLite-Based Variable Management (gradual migration from variables.json to SQLite, enhanced robustness)

## 📚 Main Contents

- **[macro.md](./macro.md)** - Main guide (10 design patterns + appendix references)
- **[Appendix.md](./Appendix.md)** - Appendix (advanced technical elements and methodologies)
- **[examples/](./examples/)** - Pattern-specific example collection
- **[multi-haiku/](./multi-haiku/)** - Multi-agent haiku generation system (SQLite-based implementation example)
- **[SQLite/](./SQLite/)** - SQLite-based variable management system implementation code and tools
- **[haiku_direct.md](./haiku_direct.md)** - Practical example (haiku generation system)
- **[CLAUDE.md](./CLAUDE.md)** - Macro definition file
- **[debugger.md](./debugger.md)** - Debug mode specification

## 📧 Contact

- **Technical questions, bug reports**: [GitHub Issues](../../issues)
- **Academic inquiries**: wadayama@nitech.ac.jp

## 🛡️ License

MIT License - see [LICENSE](./LICENSE) for details.

## 👥 Authors

- **Tadashi Wadayama** - Project design and documentation

---

**Last Updated**: 2025-07-05  
**Author**: Tadashi Wadayama (with assistance from Claude Code)  
**License**: MIT License (2025)