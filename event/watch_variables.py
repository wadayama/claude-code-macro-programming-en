#!/usr/bin/env python3
"""Variable watcher for debugging SQLite variable management system.

This tool helps debug CLAUDE.md natural language macro execution by
monitoring variable changes in real-time.
"""

import argparse
import json
import sqlite3
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional, Set

from variable_db import VariableDB


class Colors:
    """ANSI color codes for terminal output."""
    
    GREEN = "\033[92m"    # New variables
    YELLOW = "\033[93m"   # Modified variables
    RED = "\033[91m"      # Deleted variables
    BLUE = "\033[94m"     # Headers
    CYAN = "\033[96m"     # Timestamps
    RESET = "\033[0m"     # Reset color
    BOLD = "\033[1m"      # Bold text


class VariableWatcher:
    """Monitor SQLite variable database for changes."""
    
    def __init__(self, db_path: str = "variables.db", use_colors: bool = True):
        """Initialize the variable watcher.
        
        Parameters
        ----------
        db_path : str
            Path to the SQLite database file
        use_colors : bool
            Whether to use colored output
        """
        self.db_path = Path(db_path)
        self.db = VariableDB(db_path)
        self.use_colors = use_colors and sys.stdout.isatty()
        self.last_variables: Dict[str, str] = {}
        self.watch_specific: Optional[str] = None
        
    def _colorize(self, text: str, color: str) -> str:
        """Apply color to text if colors are enabled."""
        if self.use_colors:
            return f"{color}{text}{Colors.RESET}"
        return text
    
    def _get_timestamp(self) -> str:
        """Get formatted timestamp."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        return self._colorize(f"[{timestamp}]", Colors.CYAN)
    
    def _print_header(self, title: str) -> None:
        """Print a colored header."""
        header = f"\n{self._colorize('=' * 50, Colors.BLUE)}"
        title_colored = self._colorize(f" {title} ", Colors.BOLD + Colors.BLUE)
        print(f"{header}\n{title_colored}\n{header}")
    
    def display_variables_table(self, variables: Dict[str, str]) -> None:
        """Display variables in a formatted table."""
        if not variables:
            print(self._colorize("No variables found.", Colors.YELLOW))
            return
        
        # Calculate column widths
        max_name_len = max(len(name) for name in variables.keys())
        max_value_len = max(len(str(value)) for value in variables.values())
        name_width = max(12, max_name_len + 2)
        value_width = max(15, min(max_value_len + 2, 50))  # Limit value width
        
        # Print header
        header = f"{'Variable Name':<{name_width}} | {'Value':<{value_width}} | Updated"
        separator = "-" * len(header)
        print(self._colorize(header, Colors.BOLD))
        print(self._colorize(separator, Colors.BLUE))
        
        # Print variables
        for name, value in sorted(variables.items()):
            # Truncate long values
            display_value = value if len(value) <= 47 else value[:44] + "..."
            
            # Get variable info for timestamp
            info = self.db.get_variable_info(name)
            updated = info["updated_at"] if info else "Unknown"
            
            # Format variable name with proper spacing
            var_display = f"{{{{ {name} }}}}"
            spacing = " " * max(0, name_width - len(var_display))
            print(f"{var_display}{spacing} | {display_value:<{value_width}} | {updated}")
    
    def display_variables_json(self, variables: Dict[str, str]) -> None:
        """Display variables in JSON format."""
        output = {
            "timestamp": datetime.now().isoformat(),
            "variables": variables,
            "count": len(variables)
        }
        print(json.dumps(output, indent=2, ensure_ascii=False))
    
    def display_variables_simple(self, variables: Dict[str, str]) -> None:
        """Display variables in simple format."""
        for name, value in sorted(variables.items()):
            print(f"{{{{ {name} }}}} = {value}")
    
    def watch_once(self, format_type: str = "table") -> None:
        """Display all variables once."""
        self._print_header(f"Variables Snapshot - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        variables = self.db.list_variables()
        
        if format_type == "json":
            self.display_variables_json(variables)
        elif format_type == "simple":
            self.display_variables_simple(variables)
        else:  # table
            self.display_variables_table(variables)
        
        print(f"\nTotal variables: {len(variables)}")
    
    def watch_specific_variable(self, var_name: str, interval: float = 1.0) -> None:
        """Watch a specific variable for changes."""
        self._print_header(f"Watching Variable: {{{{ {var_name} }}}}")
        print(f"Update interval: {interval}s (Press Ctrl+C to stop)\n")
        
        last_value = None
        last_info = None
        
        try:
            while True:
                current_value = self.db.get_variable(var_name)
                current_info = self.db.get_variable_info(var_name)
                
                if current_value != last_value or (current_info and current_info != last_info):
                    timestamp = self._get_timestamp()
                    
                    if last_value is None:
                        # First time or variable was created
                        if current_value:
                            status = self._colorize("CREATED", Colors.GREEN)
                            print(f"{timestamp} {status}: {{{{ {var_name} }}}} = \"{current_value}\"")
                        else:
                            status = self._colorize("NOT_FOUND", Colors.YELLOW)
                            print(f"{timestamp} {status}: {{{{ {var_name} }}}} (variable does not exist)")
                    elif not current_value and last_value:
                        # Variable was deleted
                        status = self._colorize("DELETED", Colors.RED)
                        print(f"{timestamp} {status}: {{{{ {var_name} }}}} (was: \"{last_value}\")")
                    elif current_value != last_value:
                        # Variable was modified
                        status = self._colorize("MODIFIED", Colors.YELLOW)
                        print(f"{timestamp} {status}: {{{{ {var_name} }}}} = \"{current_value}\" (was: \"{last_value}\")")
                    
                    if current_info:
                        updated_time = self._colorize(current_info["updated_at"], Colors.CYAN)
                        print(f"         Last updated: {updated_time}")
                    
                    last_value = current_value
                    last_info = current_info
                
                time.sleep(interval)
                
        except KeyboardInterrupt:
            print(f"\n\n{self._colorize('Monitoring stopped.', Colors.BLUE)}")
    
    def watch_continuous(self, interval: float = 1.0, format_type: str = "table") -> None:
        """Watch all variables continuously for changes."""
        self._print_header("Continuous Variable Monitoring")
        print(f"Update interval: {interval}s (Press Ctrl+C to stop)\n")
        
        # Initialize with current state
        self.last_variables = self.db.list_variables()
        if self.last_variables:
            print(f"{self._get_timestamp()} Initial state ({len(self.last_variables)} variables):")
            if format_type == "table":
                self.display_variables_table(self.last_variables)
            elif format_type == "json":
                self.display_variables_json(self.last_variables)
            else:
                self.display_variables_simple(self.last_variables)
        
        try:
            while True:
                time.sleep(interval)
                current_variables = self.db.list_variables()
                
                if current_variables != self.last_variables:
                    self._show_changes(self.last_variables, current_variables)
                    self.last_variables = current_variables.copy()
                    
        except KeyboardInterrupt:
            print(f"\n\n{self._colorize('Monitoring stopped.', Colors.BLUE)}")
    
    def _show_changes(self, old_vars: Dict[str, str], new_vars: Dict[str, str]) -> None:
        """Show changes between variable states."""
        timestamp = self._get_timestamp()
        
        # Find new variables
        new_names = set(new_vars.keys()) - set(old_vars.keys())
        for name in new_names:
            status = self._colorize("NEW", Colors.GREEN)
            print(f"{timestamp} {status}: {{{{ {name} }}}} = \"{new_vars[name]}\"")
        
        # Find deleted variables
        deleted_names = set(old_vars.keys()) - set(new_vars.keys())
        for name in deleted_names:
            status = self._colorize("DELETED", Colors.RED)
            print(f"{timestamp} {status}: {{{{ {name} }}}} (was: \"{old_vars[name]}\")")
        
        # Find modified variables
        common_names = set(old_vars.keys()) & set(new_vars.keys())
        for name in common_names:
            if old_vars[name] != new_vars[name]:
                status = self._colorize("MODIFIED", Colors.YELLOW)
                print(f"{timestamp} {status}: {{{{ {name} }}}} = \"{new_vars[name]}\" (was: \"{old_vars[name]}\")") 
    
    def show_statistics(self) -> None:
        """Show database statistics."""
        self._print_header("Variable Database Statistics")
        
        variables = self.db.list_variables()
        
        print(f"Database file: {self.db_path}")
        print(f"Total variables: {len(variables)}")
        
        if variables:
            # Variable name statistics
            name_lengths = [len(name) for name in variables.keys()]
            value_lengths = [len(value) for value in variables.values()]
            
            print(f"\nVariable names:")
            print(f"  Shortest: {min(name_lengths)} characters")
            print(f"  Longest: {max(name_lengths)} characters")
            print(f"  Average: {sum(name_lengths)/len(name_lengths):.1f} characters")
            
            print(f"\nVariable values:")
            print(f"  Shortest: {min(value_lengths)} characters")
            print(f"  Longest: {max(value_lengths)} characters")
            print(f"  Average: {sum(value_lengths)/len(value_lengths):.1f} characters")
            
            # Show recent variables
            print(f"\nRecent variables (with timestamps):")
            recent_vars = []
            for name in variables.keys():
                info = self.db.get_variable_info(name)
                if info:
                    recent_vars.append((name, info["updated_at"]))
            
            recent_vars.sort(key=lambda x: x[1], reverse=True)
            for name, updated in recent_vars[:5]:
                print(f"  {{{{ {name} }}}} - {updated}")


def main():
    """Main entry point for the variable watcher."""
    parser = argparse.ArgumentParser(
        description="Watch SQLite variable database for changes",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --once                          # Show all variables once
  %(prog)s --continuous --interval 0.5     # Watch continuously (0.5s interval)
  %(prog)s --watch user_name --continuous  # Watch specific variable
  %(prog)s --format json --once            # Output in JSON format
  %(prog)s --stats                         # Show database statistics
        """
    )
    
    parser.add_argument(
        "--db", "-d", 
        default="variables.db",
        help="SQLite database file path (default: variables.db)"
    )
    
    parser.add_argument(
        "--once", 
        action="store_true",
        help="Show variables once and exit"
    )
    
    parser.add_argument(
        "--continuous", "-c",
        action="store_true", 
        help="Monitor variables continuously"
    )
    
    parser.add_argument(
        "--watch", "-w",
        metavar="VARIABLE_NAME",
        help="Watch a specific variable"
    )
    
    parser.add_argument(
        "--interval", "-i",
        type=float,
        default=1.0,
        help="Update interval in seconds (default: 1.0)"
    )
    
    parser.add_argument(
        "--format", "-f",
        choices=["table", "json", "simple"],
        default="table",
        help="Output format (default: table)"
    )
    
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable colored output"
    )
    
    parser.add_argument(
        "--stats", "-s",
        action="store_true",
        help="Show database statistics"
    )
    
    args = parser.parse_args()
    
    # Check if database exists
    if not Path(args.db).exists():
        print(f"Error: Database file '{args.db}' not found.")
        print("Create some variables first or specify the correct database path.")
        sys.exit(1)
    
    # Initialize watcher
    watcher = VariableWatcher(args.db, use_colors=not args.no_color)
    
    try:
        if args.stats:
            watcher.show_statistics()
        elif args.watch:
            if args.continuous:
                watcher.watch_specific_variable(args.watch, args.interval)
            else:
                # Show current value of specific variable
                value = watcher.db.get_variable(args.watch)
                if value:
                    print(f"{{{{ {args.watch} }}}} = {value}")
                else:
                    print(f"Variable {{{{ {args.watch} }}}} not found.")
        elif args.continuous:
            watcher.watch_continuous(args.interval, args.format)
        elif args.once:
            watcher.watch_once(args.format)
        else:
            # Default: show once in table format
            watcher.watch_once("table")
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()