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

## 🎯 10 Design Patterns

The core of natural language macro programming consists of 10 design patterns, systematically organized into **4 Basic Patterns** and **6 Advanced Patterns**.

### 📋 Basic 4 Patterns - [macro.md](./macro.md)

- **[Pattern 1: Sequential Pipeline](./macro.md#pattern-1-sequential-pipeline)** - Basic execution pattern that processes tasks sequentially, passing results from one stage to the next
- **[Pattern 2: Parallel Processing](./macro.md#pattern-2-parallel-processing)** - Parallel execution pattern that runs multiple tasks simultaneously for efficient processing
- **[Pattern 3: Conditional Execution](./macro.md#pattern-3-conditional-execution)** - Conditional branching pattern that selects different processing paths based on situations
- **[Pattern 4: Loop & Modular Programming](./macro.md#pattern-4-loop--modular-programming)** - Efficient repetitive control through TODO-list based iteration and Few-shot Pattern Loop

### 🚀 Advanced 6 Patterns - [macro.md](./macro.md)

- **[Pattern 5: Problem Solving & Recursion](./macro.md#pattern-5-problem-solving--recursion)** - Recursive approach that breaks down complex problems step by step and solves them through TODO management
- **[Pattern 6: Learning from Experience](./macro.md#pattern-6-learning-from-experience)** - Experience learning pattern that learns from past execution results and generates improvement suggestions
- **[Pattern 7: Environment Sensing, Knowledge-base & Environment Model](./macro.md#pattern-7-environment-sensing-knowledge-base-and-environment-model)** - Acquires external environment information, builds knowledge systems, and executes adaptive processing according to situations
- **[Pattern 8: Human-in-the-Loop](./macro.md#pattern-8-human-in-the-loop-hitl)** - Collaborative execution pattern that incorporates human judgment at appropriate timings
- **[Pattern 9: Error Handling](./macro.md#pattern-9-error-handling)** - Robustness improvement pattern that predicts errors and executes appropriate recovery processing
- **[Pattern 10: Debug & Tracing](./macro.md#pattern-10-debug--tracing)** - Development support pattern that visualizes execution status and assists in problem identification and resolution

### 🔧 Pattern Utilization and Integration

**Structure**: Combine Pattern 1-4 (Basic Patterns) and Pattern 5-10 (Advanced Patterns), along with Appendix (Specialized Technologies) to build practical systems.

**Integration Effects**: By combining multiple patterns, collaborative systems like the **A.4 Haiku Generation Multi-Agent** can be constructed.

### 📖 Appendix (Advanced Technologies) - [Appendix.md](./Appendix.md)

- **[A.1: Event-Driven Execution](./Appendix.md#a1-event-driven-execution)** - Asynchronous processing and real-time response systems
- **[A.2: Four-Layer Defense Strategy](./Appendix.md#a2-four-layer-defense-strategy)** - Four-layer defense strategies for reliable operations
- **[A.3: Python Tool Integration](./Appendix.md#a3-python-tool-integration)** - Python ecosystem utilization via SQLite variable management integration
- **[A.4: Multi-Agent System Design](./Appendix.md#a4-multi-agent-system-design)** - Collaborative agent systems with shared blackboard model (includes haiku generation multi-agent implementation example)
- **[A.5: Audit Log System](./Appendix.md#a5-audit-log-system)** - Transparency and accountability tracking via SQLite variable management extension
- **[A.6: LLM-based Pre-execution Inspection](./Appendix.md#a6-llm-based-pre-execution-inspection)** - LLM-powered pre-execution static analysis for security and quality assurance
- **[A.7: Metaprogramming](./Appendix.md#a7-metaprogramming)** - Self-adaptive systems through dynamic macro generation, verification, evaluation, and improvement
- **[A.8: Ensemble Execution and Consensus Formation](./Appendix.md#a8-ensemble-execution-and-consensus-formation)** - Statistical countermeasures for probabilistic behavior
- **[A.9: Type Safety and Schema Management](./Appendix.md#a9-type-safety-and-schema-management)** - Gradual type safety enhancement and schema-based systematic data management
- **[A.10: LLM-based Post-execution Evaluation](./Appendix.md#a10-llm-based-post-execution-evaluation)** - Quality, creativity, and logic evaluation for probabilistic systems
- **[A.11: Variable Management Persistence and Scaling](./Appendix.md#a11-variable-management-persistence-and-scaling-database-utilization)** - Robust state management via databases
- **[A.12: Vector Database and RAG Utilization](./Appendix.md#a12-vector-database-and-rag-utilization)** - Dynamic knowledge systems through knowledge bases and experience learning
- **[A.13: Goal-Oriented Architecture and Autonomous Planning](./Appendix.md#a13-goal-oriented-architecture-and-autonomous-planning)** - Complete autonomous systems via 4-stage flow and PDCA cycle
- **[A.14: Python Orchestration-Based Hybrid Approach](./Appendix.md#a14-python-orchestration-based-hybrid-approach)** - High-speed, cost-efficient systems via Python + natural language macros
- **[A.15: SQLite-Based Variable Management](./Appendix.md#a15-sqlite-based-variable-management)** - Robust variable management system with SQLite database, enhanced performance
- **[A.16: LLM Agent Collaborative Macro Auto-Generation](./Appendix.md#a16-llm-agent-collaborative-macro-auto-generation)** - Automatic conversion methods from declarative specifications to procedural macros with design pattern utilization

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