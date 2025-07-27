# Natural Language Macro Test

This file tests the simplified syntax of Chroma RAG system integrated natural language macro programming.

## Test Scenario: Python Web Development Project

### 1. Initialization
Clear all variables

### 2. Variable Setup
Save Python Web API Project to {{project_name}}

Save intermediate to {{skill_level}}

Save API optimization techniques to {{research_topic}}

### 3. Knowledge Base Construction
Save this content to knowledge base:
"In Python Web API development, the FastAPI framework achieves both high performance and development efficiency. Modern API development is possible through automatic API specification generation, type hint utilization, and asynchronous processing support. Full-fledged web services can be built in combination with PostgreSQL."

Save this content to knowledge base:
"For API response time optimization, database query optimization, cache strategies, and asynchronous processing utilization are effective. In particular, session management and query result caching using Redis can be expected to improve performance by more than 50%."

### 4. Knowledge Search Test (Simple Syntax)
{{knowledge:FastAPI}}

{{knowledge:{{project_name}}}}

{{knowledge:{{research_topic}}}}

### 5. Experience Learning Test
Save this success example as experience:
"In Python API development, built a full-fledged REST API in 2 weeks using FastAPI + PostgreSQL + Docker configuration. Achieved both quality and speed through automatic test introduction, improving team development efficiency by 40%."

Record this learning:
"For small team API development, early Docker containerization and automatic test introduction are key to improving development efficiency."

### 6. Experience Search Test (Simple Syntax)
{{memory:Python API development}}

{{memory:{{project_name}}}}

{{memory:new Web development project}}

### 7. Conditional Branching and Integrated Utilization
If {{skill_level}} is intermediate, suggest efficiency-focused development methods; if beginner, suggest learning-focused approaches

## Expected Results

### Simple Syntax Operation Verification
- `{{knowledge:query}}` → Knowledge search is executed
- `{{memory:task}}` → Experience search is executed  
- `{{knowledge:{{variable}}}}` → Knowledge search with variable value (nested syntax)
- `{{memory:{{variable}}}}` → Experience search with variable value (nested syntax)

### Integrated Operation
- Integration of SQLite variables and Chroma vector database
- Combination of conditional branching and knowledge utilization
- Appropriate search results through semantic similarity

---

**Usage**: Execute the above instructions in order with Claude Code. You can confirm that the new simple syntax operates correctly.