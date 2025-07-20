#!/usr/bin/env python3
"""Simple data visualization tool for natural language macro programming."""

import matplotlib.pyplot as plt
from variable_db import get_variable, save_variable


def main():
    """Create visualization from variable data."""
    # Get data and parameters from variables
    data_str = get_variable("data_values")
    title = get_variable("chart_title") or "Data Visualization"
    x_label = get_variable("x_label") or "Index"
    y_label = get_variable("y_label") or "Value"
    output_file = get_variable("output_filename") or "chart.png"
    
    # Parse comma-separated data
    data = [float(x.strip()) for x in data_str.split(",")]
    
    # Create line plot
    plt.figure(figsize=(10, 6))
    plt.plot(data, marker='o')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    
    # Save plot
    plt.savefig(output_file)
    plt.close()
    
    # Save result to variables
    save_variable("output_file", output_file)
    
    print(f"Chart saved as {output_file}")


if __name__ == "__main__":
    main()