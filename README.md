# Claude Code Natural Language Macro Programming Guide

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

**10 Design Patterns**
- Basic Processing Patterns (Sequential, Parallel, Conditional, Loop)
- Advanced Patterns (Problem Solving, Learning from Experience, Environment Understanding, Human Collaboration, Error Handling, Debug)

**Appendix: Implementation Technologies**
- A.1: System Control via Claude Code Slash Commands
- A.2: Event-Driven Execution
- A.3: Risk Mitigation Strategies for Important Tasks
- A.4: Python Tool Integration
- A.5: Multi-Agent System Design (variables.json blackboard model)
- A.6: Audit Log System (transparency and accountability tracking)
- A.7: LLM-based Verification System (LLM-powered pre-execution static analysis for security)
- A.8: Metaprogramming (dynamic macro generation, verification, evaluation, and improvement)
- A.9: Ensemble Execution and Consensus Formation (statistical countermeasures for probabilistic behavior)
- A.10: Type Safety and Schema Management (gradual type safety enhancement and schema-based systematic data management)

**Practical Applications**
- Haiku generation, blog creation, investment decision support systems
- Business automation methodologies

## 📚 Main Contents

- **[macro.md](./macro.md)** - Main guide (10 design patterns + appendix references)
- **[Appendix.md](./Appendix.md)** - Appendix (advanced system integration and risk management)
- **[examples/](./examples/)** - Pattern-specific example collection
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

**Last Updated**: 2025-07-04  
**Author**: Tadashi Wadayama (with assistance from Claude Code)  
**License**: MIT License (2025)