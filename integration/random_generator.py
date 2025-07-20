#!/usr/bin/env python3
"""Simple random number generator for natural language macro programming."""

import random
from variable_db import get_variable, save_variable


def main():
    """Generate random numbers and save to variables."""
    # Get parameters from variables
    count = int(get_variable("random_count") or "10")
    min_val = float(get_variable("random_min") or "1.0")
    max_val = float(get_variable("random_max") or "10.0")
    
    # Generate random numbers
    numbers = [round(random.uniform(min_val, max_val), 1) for _ in range(count)]
    data_str = ",".join(map(str, numbers))
    
    # Save result to variables
    save_variable("data_values", data_str)
    
    print(f"Generated {count} random numbers: {data_str}")


if __name__ == "__main__":
    main()