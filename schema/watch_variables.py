#!/usr/bin/env python3
"""Type-aware variable watcher for debugging schema validation system.

This tool helps debug CLAUDE.md natural language macro execution by
monitoring variable changes and their type information in real-time.
"""

import argparse
import json
import sqlite3
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional, Set, Tuple, Any

from variable_db import VariableDB


class Colors:
    """ANSI color codes for terminal output."""
    
    GREEN = "\033[92m"    # Valid/New variables
    YELLOW = "\033[93m"   # Modified variables
    RED = "\033[91m"      # Invalid/Deleted variables
    BLUE = "\033[94m"     # Headers
    CYAN = "\033[96m"     # Timestamps
    MAGENTA = "\033[95m"  # Type information
    RESET = "\033[0m"     # Reset color
    BOLD = "\033[1m"      # Bold text


class TypeAwareVariableWatcher:
    """Monitor SQLite variable database with type information display."""
    
    def __init__(self, db_path: str = "variables.db", use_colors: bool = True):
        """Initialize the type-aware variable watcher.
        
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
        self.last_variables: Dict[str, Tuple[str, Optional[str]]] = {}
        
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
        header = f"\n{self._colorize('=' * 70, Colors.BLUE)}"
        title_colored = self._colorize(f" {title} ", Colors.BOLD + Colors.BLUE)
        print(f"{header}\n{title_colored}\n{header}")
    
    def _get_validation_status(self, name: str, value: str, type_name: Optional[str]) -> str:
        """Get validation status for a variable."""
        if type_name is None:
            return self._colorize("-", Colors.YELLOW)  # No type
        
        try:
            # Try to validate the current value
            self.db._validate_value(value, type_name)
            return self._colorize("✓", Colors.GREEN)  # Valid
        except Exception:
            return self._colorize("✗", Colors.RED)  # Invalid
    
    def display_variables_table(self, variables_with_types: Dict[str, Tuple[str, Optional[str]]]) -> None:
        """Display variables with type information in a formatted table."""
        if not variables_with_types:
            print(self._colorize("No variables found.", Colors.YELLOW))
            return
        
        # Calculate column widths
        max_name_len = max(len(f"{{{{ {name} }}}}") for name in variables_with_types.keys())
        max_value_len = max(len(str(value)) for value, _ in variables_with_types.values())
        max_type_len = max(len(type_name or "(none)") for _, type_name in variables_with_types.values())
        
        name_width = max(15, max_name_len + 2)
        value_width = max(12, min(max_value_len + 2, 40))  # Limit value width
        type_width = max(8, max_type_len + 2)
        
        # Print header
        header = f"{'Variable Name':<{name_width}} | {'Value':<{value_width}} | {'Type':<{type_width}} | Status | Updated"
        separator = "-" * len(header)
        print(self._colorize(header, Colors.BOLD))
        print(self._colorize(separator, Colors.BLUE))
        
        # Print variables
        for name, (value, type_name) in sorted(variables_with_types.items()):
            # Truncate long values
            display_value = value if len(value) <= 37 else value[:34] + "..."
            
            # Format variable name
            var_display = f"{{{{ {name} }}}}"
            
            # Format type name
            type_display = self._colorize(type_name or "(none)", 
                                        Colors.MAGENTA if type_name else Colors.YELLOW)
            
            # Get validation status
            status = self._get_validation_status(name, value, type_name)
            
            # Get variable info for timestamp
            info = self.db.get_variable_info(name)
            updated = info["updated_at"] if info else "Unknown"
            
            # Format row
            print(f"{var_display:<{name_width}} | {display_value:<{value_width}} | {type_display:<{type_width+10}} | {status:<6} | {updated}")
    
    def display_schema_info(self) -> None:
        """Display available schema types and their definitions."""
        print(self._colorize("\nAvailable Schema Types:", Colors.BOLD + Colors.BLUE))
        print(self._colorize("-" * 25, Colors.BLUE))
        
        schema_types = self.db.list_schema_types()
        if not schema_types:
            print(self._colorize("No schema types available.", Colors.YELLOW))
            return
        
        for schema_type in sorted(schema_types):
            schema_info = self.db.get_schema_info(schema_type)
            if schema_info:
                # Format schema definition
                schema_desc = f"{schema_info['type']}"
                if "min" in schema_info or "max" in schema_info:
                    min_val = schema_info.get("min", "∞")
                    max_val = schema_info.get("max", "∞") 
                    schema_desc += f" ({min_val}-{max_val})"
                if "enum" in schema_info:
                    enum_vals = ", ".join(schema_info["enum"])
                    schema_desc += f" [{enum_vals}]"
                
                type_colored = self._colorize(schema_type, Colors.MAGENTA)
                print(f"  {type_colored:<20}: {schema_desc}")
    
    def watch_once(self, show_schemas: bool = False) -> None:
        """Display all variables once with type information."""
        self._print_header(f"Type-Aware Variables Snapshot - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        variables_with_types = self.db.list_variables_with_types()
        self.display_variables_table(variables_with_types)
        
        # Display summary
        total_vars = len(variables_with_types)
        typed_vars = sum(1 for _, type_name in variables_with_types.values() if type_name is not None)
        untyped_vars = total_vars - typed_vars
        
        print(f"\nSummary: {total_vars} total variables")
        print(f"  {self._colorize(f'{typed_vars} typed', Colors.MAGENTA)}")
        print(f"  {self._colorize(f'{untyped_vars} untyped', Colors.YELLOW)}")
        
        if show_schemas:
            self.display_schema_info()
    
    def watch_continuous(self, interval: float = 1.0) -> None:
        """Watch all variables continuously for changes."""
        self._print_header("Continuous Type-Aware Variable Monitoring")
        print(f"Update interval: {interval}s (Press Ctrl+C to stop)\n")
        
        # Initialize with current state
        self.last_variables = self.db.list_variables_with_types()
        if self.last_variables:
            print(f"{self._get_timestamp()} Initial state ({len(self.last_variables)} variables):")
            self.display_variables_table(self.last_variables)
        
        try:
            while True:
                time.sleep(interval)
                current_variables = self.db.list_variables_with_types()
                
                if current_variables != self.last_variables:
                    self._show_changes(self.last_variables, current_variables)
                    self.last_variables = current_variables.copy()
                    
        except KeyboardInterrupt:
            print(f"\n\n{self._colorize('Monitoring stopped.', Colors.BLUE)}")
    
    def _show_changes(self, old_vars: Dict[str, Tuple[str, Optional[str]]], 
                     new_vars: Dict[str, Tuple[str, Optional[str]]]) -> None:
        """Show changes between variable states with type information."""
        timestamp = self._get_timestamp()
        
        # Find new variables
        new_names = set(new_vars.keys()) - set(old_vars.keys())
        for name in new_names:
            value, type_name = new_vars[name]
            type_info = f" ({type_name})" if type_name else " (untyped)"
            status = self._colorize("NEW", Colors.GREEN)
            print(f"{timestamp} {status}: {{{{ {name} }}}} = \"{value}\"{self._colorize(type_info, Colors.MAGENTA)}")
        
        # Find deleted variables
        deleted_names = set(old_vars.keys()) - set(new_vars.keys())
        for name in deleted_names:
            old_value, old_type = old_vars[name]
            type_info = f" ({old_type})" if old_type else " (untyped)"
            status = self._colorize("DELETED", Colors.RED)
            print(f"{timestamp} {status}: {{{{ {name} }}}} (was: \"{old_value}\"{self._colorize(type_info, Colors.MAGENTA)})")
        
        # Find modified variables
        common_names = set(old_vars.keys()) & set(new_vars.keys())
        for name in common_names:
            old_value, old_type = old_vars[name]
            new_value, new_type = new_vars[name]
            
            if (old_value, old_type) != (new_value, new_type):
                status = self._colorize("MODIFIED", Colors.YELLOW)
                
                if old_value != new_value and old_type == new_type:
                    # Value changed, type same
                    type_info = f" ({new_type})" if new_type else " (untyped)"
                    print(f"{timestamp} {status}: {{{{ {name} }}}} = \"{new_value}\" (was: \"{old_value}\"){self._colorize(type_info, Colors.MAGENTA)}")
                elif old_type != new_type:
                    # Type changed (with or without value change)
                    old_type_display = old_type or "untyped"
                    new_type_display = new_type or "untyped"
                    print(f"{timestamp} {status}: {{{{ {name} }}}} = \"{new_value}\" type: {self._colorize(old_type_display, Colors.RED)} → {self._colorize(new_type_display, Colors.GREEN)}")
    
    def validate_all_variables(self) -> None:
        """Show validation status for all typed variables."""
        self._print_header("Variable Validation Report")
        
        validation_results = self.db.validate_all()
        if not validation_results:
            print(self._colorize("No typed variables found.", Colors.YELLOW))
            return
        
        valid_count = sum(1 for result in validation_results.values() if result is True)
        total_count = len(validation_results)
        
        print(f"Validation Summary: {self._colorize(f'{valid_count}/{total_count}', Colors.BOLD)} variables are valid\n")
        
        for var_name, result in validation_results.items():
            if result is True:
                status = self._colorize("✓ VALID", Colors.GREEN)
                print(f"{status}: {{{{ {var_name} }}}}")
            else:
                status = self._colorize("✗ INVALID", Colors.RED)
                print(f"{status}: {{{{ {var_name} }}}} - {result}")
    
    def show_statistics(self) -> None:
        """Show database statistics with type information."""
        self._print_header("Type-Aware Variable Database Statistics")
        
        variables_with_types = self.db.list_variables_with_types()
        
        print(f"Database file: {self.db_path}")
        print(f"Total variables: {len(variables_with_types)}")
        
        if variables_with_types:
            # Type distribution
            typed_vars = [(name, type_name) for name, (_, type_name) in variables_with_types.items() if type_name]
            untyped_vars = [(name, value) for name, (value, type_name) in variables_with_types.items() if not type_name]
            
            print(f"\nType Distribution:")
            print(f"  {self._colorize(f'Typed variables: {len(typed_vars)}', Colors.MAGENTA)}")
            print(f"  {self._colorize(f'Untyped variables: {len(untyped_vars)}', Colors.YELLOW)}")
            
            if typed_vars:
                # Count by type
                type_counts = {}
                for _, type_name in typed_vars:
                    type_counts[type_name] = type_counts.get(type_name, 0) + 1
                
                print(f"\n  Type breakdown:")
                for type_name, count in sorted(type_counts.items()):
                    print(f"    {self._colorize(type_name, Colors.MAGENTA)}: {count}")
            
            # Recent variables
            print(f"\nRecent variables (with type info):")
            recent_vars = []
            for name, (value, type_name) in variables_with_types.items():
                info = self.db.get_variable_info(name)
                if info:
                    type_display = type_name or "untyped"
                    recent_vars.append((name, type_display, info["updated_at"]))
            
            recent_vars.sort(key=lambda x: x[2], reverse=True)
            for name, type_name, updated in recent_vars[:5]:
                type_colored = self._colorize(f"({type_name})", Colors.MAGENTA)
                print(f"  {{{{ {name} }}}} {type_colored} - {updated}")


def main():
    """Main entry point for the type-aware variable watcher."""
    parser = argparse.ArgumentParser(
        description="Watch SQLite variable database with type information",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --once                          # Show all variables with types once
  %(prog)s --continuous --interval 0.5     # Watch continuously (0.5s interval)
  %(prog)s --validate                      # Show validation status for all variables
  %(prog)s --schemas                       # Show available schema types
  %(prog)s --stats                         # Show database statistics with type info
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
        "--interval", "-i",
        type=float,
        default=1.0,
        help="Update interval in seconds (default: 1.0)"
    )
    
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable colored output"
    )
    
    parser.add_argument(
        "--stats", "-s",
        action="store_true",
        help="Show database statistics with type information"
    )
    
    parser.add_argument(
        "--validate", "-v",
        action="store_true",
        help="Show validation status for all typed variables"
    )
    
    parser.add_argument(
        "--schemas",
        action="store_true",
        help="Show available schema types and definitions"
    )
    
    args = parser.parse_args()
    
    # Check if database exists
    if not Path(args.db).exists():
        print(f"Error: Database file '{args.db}' not found.")
        print("Create some variables first or specify the correct database path.")
        sys.exit(1)
    
    # Initialize watcher
    watcher = TypeAwareVariableWatcher(args.db, use_colors=not args.no_color)
    
    try:
        if args.stats:
            watcher.show_statistics()
        elif args.validate:
            watcher.validate_all_variables()
        elif args.schemas:
            watcher.display_schema_info()
        elif args.continuous:
            watcher.watch_continuous(args.interval)
        elif args.once:
            watcher.watch_once(show_schemas=args.schemas)
        else:
            # Default: show once with schema info
            watcher.watch_once(show_schemas=True)
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()