#!/usr/bin/env python3
"""A.2: Event-Driven Execution - Concept Proof

Watch 'user_status' variable and execute simple macro when it changes.
"""

import time
import subprocess
from variable_db import get_variable, save_variable, VariableDB

# Watch this specific variable  
WATCH_VARIABLE = "user_status"
MACRO_FILE = "simple_macro.md"

print(f"🚀 Event Handler Starting...")

# (1) Clear all variables
VariableDB().clear_all()

# (2) Set initial value
save_variable(WATCH_VARIABLE, "inactive")
print(f"🔍 Now watching variable: {WATCH_VARIABLE}")
last_value = get_variable(WATCH_VARIABLE)
print(f"📊 Initial value: '{last_value}'")
print("=" * 40)
time.sleep(2.0)
def run_macro():
    """Execute macro using claude command"""
    try:
        with open(MACRO_FILE, 'r', encoding='utf-8') as f:
            subprocess.run(["claude", "-p", "--dangerously-skip-permissions"], 
                         stdin=f, check=True)
    except Exception as e:
        print(f"   ❌ Macro execution failed: {e}")

try:
    while True:
        current_value = get_variable(WATCH_VARIABLE)
        
        if current_value != last_value:
            print("event detected")
            run_macro()
            last_value = current_value
            print("-" * 40)
        
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n🛑 Event monitoring stopped")