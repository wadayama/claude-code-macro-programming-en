#!/usr/bin/env python3
"""
Haiku Generator Python Orchestrator
Practical example of A.15 Python Orchestration-Based Hybrid Approach
"""

import subprocess
import concurrent.futures
from variable_db import save_variable, VariableDB


def run_macro(macro_file):
    """Execute macro file"""
    with open(macro_file, 'r', encoding='utf-8') as f:
        subprocess.run(["claude", "-p", "--dangerously-skip-permissions"], stdin=f)


def create_agent_macro(agent_id):
    """Generate agent-specific macro"""
    import os
    
    # Create agents/ folder if it doesn't exist
    os.makedirs('agents', exist_ok=True)
    
    with open('agent_template.md', 'r', encoding='utf-8') as f:
        template = f.read()
    
    content = template.replace('{{AGENT_ID}}', str(agent_id))
    filename = f'agents/agent_{agent_id}.md'
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filename


def run_agent(agent_id):
    """Execute agent"""
    macro_file = create_agent_macro(agent_id)
    run_macro(macro_file)
    return agent_id


def main():
    print("=== Haiku Generation Multi-Agent System Started ===")
    
    # Initialization
    import os
    import glob
    
    # Clear variables
    count = VariableDB().clear_all()
    print(f"🔄 Cleared {count} variables")
    
    # Clear files in agents/ folder
    for file in glob.glob('agents/agent_*.md'):
        os.remove(file)
    print("🔄 Cleared agents/ folder")
    
    # Configuration
    agent_count = 3

    save_variable('agent_count', str(agent_count))
    
    # Theme generation
    run_macro('generate_themes.md')
    
    # Parallel haiku generation
    with concurrent.futures.ThreadPoolExecutor() as executor:
        list(executor.map(run_agent, range(1, agent_count + 1)))
    
    # Evaluation
    run_macro('evaluate_haiku.md')
    
    print("=== Haiku Generation Multi-Agent System Completed ===")


if __name__ == "__main__":
    main()