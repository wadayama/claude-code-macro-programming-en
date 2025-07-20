# Data Visualization Demo - Natural Language Macro Programming

This demo demonstrates SQLite-based variable management collaboration between natural language macro programming and Python tools as a proof of concept for A.4 Python Tool Integration.

## Execution Steps

### Step 0: Clear Variables

First, clear all variables to start with a clean state.

Clear all variables

### Step 1: Random Data Generation

First, set the parameters for random number generation.

Save "12" to {{random_count}}

Save "2.5" to {{random_min}}

Save "15.0" to {{random_max}}

Generate random numbers.

Execute random_generator.py

### Step 2: Visualization Parameter Setup

Save "Custom Random Data Analysis" to {{chart_title}}

Save "Sample Number" to {{x_label}}

Save "Measured Score" to {{y_label}}

Save "custom_analysis.png" to {{output_filename}}

### Step 3: Data Visualization Execution

Execute data_visualizer.py

### Step 4: Results Confirmation

Retrieve {{output_file}}