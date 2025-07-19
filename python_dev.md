# Python Development Guidelines for Scientific Computing

## 1. Introduction

### 1.1. Purpose of This Guideline
This document provides development guidelines to enhance the quality and efficiency of scientific computing conducted in this project. We prioritize the three pillars of **Correctness**, **Readability**, and **Reproducibility**.

### 1.2. Basic Principles
* **Accuracy > Speed**: In scientific computing, the accuracy of results takes priority over computational speed.
* **For future self and others**: Code is not only written once but will be read multiple times afterward.
* **Always reproducible by anyone**: We aim for a state where the same experiment can be immediately reproduced in the same environment even 10 years later.
---

## 2. Development Environment Setup and Management

**A consistent development environment is the first step toward reproducibility. We use `uv` to build and manage independent environments for each project.**

### 2.1. Virtual Environment
Execute the following command in the project root directory to create a virtual environment.
```bash
# Create virtual environment
uv venv

### 2.2. Package Management
Unify package management with `uv` and avoid concurrent use with `pip` or `conda`. Dependencies are centrally managed in `pyproject.toml`. To ensure reproducibility, specify the Python version required by the project in pyproject.toml.

* **Adding packages**:
    ```bash
    # Add packages required for execution
    uv add numpy pandas
    
    # Add packages required only during development (testing, formatters, etc.)
    uv add -d pytest ruff-lsp
    ```
* **Environment synchronization**:
    With `pyproject.toml` and `uv.lock` files, anyone can reproduce the same environment with the following command.
    ```bash
    uv sync --frozen
    ```
* **Tool execution**:
    Execute created code and installed tools using `uv run`.
    ```bash
    uv run pytest
    uv run ruff format .
    ```
---

## 3. Code Quality Standards

### 3.1. Quality Assurance through Static Analysis
**Before human review, maximize the use of automated tool checking.**

* **Formatting**: Use `ruff format` to unify code style.
* **Linting**: Use `ruff check` to detect potential bugs and deprecated practices.
* **Type checking**:
    * Add **Type Hints** to code whenever possible.
    * Use `pyright` to statically verify type hint consistency.
    
**※ We recommend consolidating these tool settings in `pyproject.toml` and sharing them across the team.**

### 3.2. Ensuring Accuracy through Testing
**We make it a principle to write tests for all functions containing logic, not just "important functions".**

* **Test framework**: Use `pytest`.
* **Testing principles**:
    * **Small and focused**: Each test function verifies only one thing.
    * **Boundary values**: Prepare test cases for not only normal cases but also abnormal cases and boundary values.
    * **Isolation of side effects**: Design processing that includes "side effects" such as random number generation, current time acquisition, and file I/O to be separated from the core logic. This makes testing the logic portion easier.

### 3.3. Improving Readability
* **Documentation strings (Docstrings)**:
    * All public modules, functions, classes, and methods must include Docstrings.
    * **We recommend NumPy style.** This clarifies arguments, return values, and processing content.
    * **Write Docstrings in English.** We standardize English writing considering international collaboration and future use.
* **Comments**: Use comments to explain "why" that code is necessary and the intent of complex logic. Comments explaining "what" that can be understood by looking at the code are unnecessary.
    * **Write comments in English as well.** We assume team development and use in international environments.
* **Naming conventions**: **Follow PEP 8 and use clear variable and function names.**
    * **Use English for variable and function names.** Avoid romaji naming and use appropriate English words.

### 3.4. Internationalization and Usability
* **Program output language**:
    * **Write console output, log messages, and error messages in English.**
    * Program execution results and progress displays should also use English as standard.
    * Naming: variable names, function names, class names (※ romaji notation is not allowed)
* **Graphs and plots**:
    * **Write axis labels, titles, and legends in English.**
    * Charts created with matplotlib etc. should also use English notation as standard, considering international use.
* **File output**:
    * Unify CSV headers, PDF titles, etc. in English.

### 3.5. Function Design Principles

### 3.5.1. Breaking Down into Small Functions
From the perspective of maintainability and readability, keep individual functions as small as possible.
* Single Responsibility Principle: One function should have only one responsibility
* Function length: Generally aim for within 20-30 lines, designed to fit on screen
* Decomposition of complex processing: Break down complex algorithms into functions by meaningful units

#### Bad: Long and complex function
```
def analyze_data(data_path: str) -> dict:
    """Analyze data from file (too complex)."""
    # Data loading (10 lines)
    # Data preprocessing (15 lines)
    # Statistical calculation (20 lines)
    # Visualization (15 lines)
    # Result saving (10 lines)
    pass  # Total 70 lines of complex processing
```
#### Good: Broken down into small functions
```
def load_data(data_path: str) -> pd.DataFrame:
    """Load data from specified path."""
    return pd.read_csv(data_path)

def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    """Clean and preprocess the input data."""
    # Preprocessing logic
    return cleaned_data

def calculate_statistics(data: pd.DataFrame) -> dict:
    """Calculate basic statistical measures."""
    # Statistical calculation logic
    return statistics

def create_visualization(data: pd.DataFrame, stats: dict) -> plt.Figure:
    """Create visualization plots."""
    # Visualization logic
    return figure

def save_results(stats: dict, figure: plt.Figure, output_dir: Path) -> None:
    """Save analysis results to files."""
    # Saving logic
    pass

def analyze_data(data_path: str, output_dir: Path) -> dict:
    """Analyze data with clear workflow."""
    data = load_data(data_path)
    cleaned_data = preprocess_data(data)
    stats = calculate_statistics(cleaned_data)
    figure = create_visualization(cleaned_data, stats)
    save_results(stats, figure, output_dir)
    return stats

```
### 3.5.2 Referential Transparency and Side Effect Separation
Clearly separate computation logic (pure functions) from I/O processing (functions with side effects).
#### Characteristics of pure functions with referential transparency
* Same output for same input: Function execution results depend only on inputs
* No side effects: Do not perform global variable changes, file operations, network communications, etc.
* Easy to test: Clear relationship between input and output, no mocking required

### 3.5.3. Function Design Best Practices

* Function names start with verbs: calculate_, process_, validate_, etc.
* Argument order: Important arguments first, optional arguments later
* Default arguments: Do not use mutable objects (lists, dictionaries) as default values
* Type hint utilization: Clarify input/output types to make function contracts clear

### 3.5.4 Minimize Use of Global Variables

To increase referentially transparent parts, minimize the use of global variables.
Global variables make function behavior unpredictable, make testing difficult, and can cause race conditions during parallel processing.
However, global variables for physical constants or immutable constants within programs may be used to improve code readability.

## 4. Setting Calculation Parameters

Rather than hard-coding calculation parameters (e.g., learning rate, iteration count) within code, reading them from configuration files in YAML or TOML format as a convention will further improve reproducibility by allowing experimental conditions to be managed without changing code.

## 5. Data Loading and Saving

### 5.1. Data Loading

### 5.2. Data Saving

### 5.3. Data Preprocessing
