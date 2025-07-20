#!/usr/bin/env python3
"""Audit log viewer for monitoring and analyzing natural language macro execution.

This tool provides comprehensive audit trail visualization for the natural language
macro programming system, enabling transparency, debugging, and compliance monitoring.
"""

import argparse
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional

from audit_logger import AuditLogger, EventType


class Colors:
    """ANSI color codes for terminal output."""
    
    GREEN = "\033[92m"      # Variable create events
    YELLOW = "\033[93m"     # Variable update events  
    RED = "\033[91m"        # Variable delete events
    BLUE = "\033[94m"       # Decision events
    CYAN = "\033[96m"       # Reasoning events
    MAGENTA = "\033[95m"    # System events
    WHITE = "\033[97m"      # Headers
    RESET = "\033[0m"       # Reset color
    BOLD = "\033[1m"        # Bold text
    DIM = "\033[2m"         # Dim text


class AuditViewer:
    """Comprehensive audit log viewer and analyzer."""
    
    def __init__(self, db_path: str = "variables.db", use_colors: bool = True):
        """Initialize the audit log viewer.
        
        Parameters
        ----------
        db_path : str
            Path to the SQLite database file
        use_colors : bool
            Whether to use colored output
        """
        self.db_path = Path(db_path)
        self.audit_db = AuditLogger(db_path)
        self.use_colors = use_colors and sys.stdout.isatty()
        
        # Color mapping for different event types
        self.event_colors = {
            EventType.VARIABLE_CREATE: Colors.GREEN,
            EventType.VARIABLE_UPDATE: Colors.YELLOW,
            EventType.VARIABLE_DELETE: Colors.RED,
            EventType.DECISION_MADE: Colors.BLUE,
            EventType.REASONING_LOGGED: Colors.CYAN,
            EventType.MACRO_START: Colors.MAGENTA,
            EventType.MACRO_END: Colors.MAGENTA,
            EventType.ERROR_OCCURRED: Colors.RED,
            EventType.USER_INPUT: Colors.WHITE,
            EventType.SYSTEM_ACTION: Colors.MAGENTA,
        }
    
    def _colorize(self, text: str, color: str) -> str:
        """Apply color to text if colors are enabled."""
        if self.use_colors:
            return f"{color}{text}{Colors.RESET}"
        return text
    
    def _format_timestamp(self, timestamp_str: str) -> str:
        """Format timestamp for display."""
        try:
            dt = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
            formatted = dt.strftime("%Y-%m-%d %H:%M:%S")
            return self._colorize(formatted, Colors.DIM)
        except ValueError:
            return self._colorize(timestamp_str, Colors.DIM)
    
    def _format_event_type(self, event_type: str) -> str:
        """Format event type with appropriate color."""
        try:
            event_enum = EventType(event_type)
            color = self.event_colors.get(event_enum, Colors.WHITE)
        except ValueError:
            color = Colors.WHITE
        
        return self._colorize(f"[{event_type.upper()}]", color)
    
    def _print_header(self, title: str) -> None:
        """Print a colored header."""
        separator = self._colorize("=" * 60, Colors.BLUE)
        title_colored = self._colorize(f" {title} ", Colors.BOLD + Colors.WHITE)
        print(f"\n{separator}")
        print(title_colored)
        print(separator)
    
    def display_logs_table(self, logs: List[Dict], max_reasoning_length: int = 50) -> None:
        """Display audit logs in a formatted table.
        
        Parameters
        ----------
        logs : list of dict
            List of audit log entries
        max_reasoning_length : int, optional
            Maximum length for reasoning text display, by default 50
        """
        if not logs:
            print(self._colorize("No audit logs found.", Colors.YELLOW))
            return
        
        print(f"\nTotal logs: {len(logs)}")
        print()
        
        # Print each log entry
        for log in logs:
            timestamp = self._format_timestamp(log['timestamp'])
            event_type = self._format_event_type(log['event_type'])
            
            print(f"{timestamp} {event_type}")
            
            # Variable information
            if log.get('variable_name'):
                var_name = self._colorize(f"{{{{ {log['variable_name']} }}}}", Colors.BOLD)
                print(f"  Variable: {var_name}")
                
                if log.get('old_value') and log.get('new_value'):
                    old_val = log['old_value'][:30] + "..." if len(log['old_value']) > 30 else log['old_value']
                    new_val = log['new_value'][:30] + "..." if len(log['new_value']) > 30 else log['new_value']
                    print(f"  Changed: {old_val} → {new_val}")
                elif log.get('new_value'):
                    new_val = log['new_value'][:30] + "..." if len(log['new_value']) > 30 else log['new_value']
                    print(f"  Value: {new_val}")
                elif log.get('old_value'):
                    old_val = log['old_value'][:30] + "..." if len(log['old_value']) > 30 else log['old_value']
                    print(f"  Deleted: {old_val}")
            
            # Decision/reasoning content
            elif log.get('new_value') and log['event_type'] in ['decision_made', 'reasoning_logged']:
                content = log['new_value'][:50] + "..." if len(log['new_value']) > 50 else log['new_value']
                print(f"  Content: {content}")
            
            # Reasoning information
            if log.get('reasoning'):
                reasoning = log['reasoning']
                if len(reasoning) > max_reasoning_length:
                    reasoning = reasoning[:max_reasoning_length] + "..."
                reasoning_colored = self._colorize(reasoning, Colors.CYAN)
                print(f"  Reasoning: {reasoning_colored}")
            
            # Source and metadata
            source_info = []
            if log.get('source'):
                source_info.append(f"Source: {log['source']}")
            if log.get('session_id'):
                source_info.append(f"Session: {log['session_id']}")
            if source_info:
                print(f"  {' | '.join(source_info)}")
            
            # Metadata
            if log.get('metadata'):
                try:
                    if isinstance(log['metadata'], str):
                        metadata = json.loads(log['metadata'])
                    else:
                        metadata = log['metadata']
                    
                    if metadata:
                        meta_str = ", ".join([f"{k}: {v}" for k, v in metadata.items()])
                        meta_colored = self._colorize(meta_str, Colors.DIM)
                        print(f"  Metadata: {meta_colored}")
                except (json.JSONDecodeError, TypeError):
                    pass
            
            print()
    
    def display_logs_json(self, logs: List[Dict]) -> None:
        """Display audit logs in JSON format.
        
        Parameters
        ----------
        logs : list of dict
            List of audit log entries
        """
        output = {
            "timestamp": datetime.now().isoformat(),
            "total_logs": len(logs),
            "logs": logs
        }
        print(json.dumps(output, indent=2, ensure_ascii=False))
    
    def display_logs_summary(self, logs: List[Dict]) -> None:
        """Display summary statistics of audit logs.
        
        Parameters
        ----------
        logs : list of dict
            List of audit log entries
        """
        if not logs:
            print(self._colorize("No audit logs found.", Colors.YELLOW))
            return
        
        # Event type statistics
        event_counts = {}
        variable_activity = {}
        sources = set()
        sessions = set()
        
        for log in logs:
            # Count event types
            event_type = log['event_type']
            event_counts[event_type] = event_counts.get(event_type, 0) + 1
            
            # Track variable activity
            if log.get('variable_name'):
                var_name = log['variable_name']
                variable_activity[var_name] = variable_activity.get(var_name, 0) + 1
            
            # Track sources and sessions
            if log.get('source'):
                sources.add(log['source'])
            if log.get('session_id'):
                sessions.add(log['session_id'])
        
        print(f"Total logs: {len(logs)}")
        print()
        
        # Event type breakdown
        print(self._colorize("Event Types:", Colors.BOLD))
        for event_type, count in sorted(event_counts.items()):
            color = self.event_colors.get(EventType(event_type) if event_type in [e.value for e in EventType] else None, Colors.WHITE)
            event_colored = self._colorize(event_type, color)
            print(f"  {event_colored}: {count}")
        print()
        
        # Most active variables
        if variable_activity:
            print(self._colorize("Most Active Variables:", Colors.BOLD))
            sorted_vars = sorted(variable_activity.items(), key=lambda x: x[1], reverse=True)
            for var_name, count in sorted_vars[:10]:
                var_colored = self._colorize(f"{{{{ {var_name} }}}}", Colors.BOLD)
                print(f"  {var_colored}: {count} operations")
            print()
        
        # Sources
        if sources:
            print(self._colorize(f"Sources: {', '.join(sorted(sources))}", Colors.DIM))
        
        # Sessions
        if sessions:
            session_count = len(sessions)
            print(self._colorize(f"Sessions: {session_count}", Colors.DIM))
        
        # Time range
        if len(logs) > 1:
            first_time = logs[-1]['timestamp']  # logs are ordered by timestamp DESC
            last_time = logs[0]['timestamp']
            print(self._colorize(f"Time range: {first_time} to {last_time}", Colors.DIM))
    
    def show_variable_history(self, variable_name: str, limit: Optional[int] = None) -> None:
        """Show complete history for a specific variable.
        
        Parameters
        ----------
        variable_name : str
            Name of the variable to track
        limit : int, optional
            Maximum number of entries to show
        """
        self._print_header(f"Variable History: {{{{ {variable_name} }}}}")
        
        logs = self.audit_db.get_audit_logs(
            variable_name=variable_name,
            limit=limit
        )
        
        if not logs:
            print(self._colorize(f"No history found for variable {{{{ {variable_name} }}}}.", Colors.YELLOW))
            return
        
        # Show in chronological order (reverse the DESC order from DB)
        logs.reverse()
        
        current_value = None
        for i, log in enumerate(logs):
            timestamp = self._format_timestamp(log['timestamp'])
            event_type = self._format_event_type(log['event_type'])
            
            print(f"{i+1:2d}. {timestamp} {event_type}")
            
            if log['event_type'] == EventType.VARIABLE_CREATE.value:
                current_value = log['new_value']
                print(f"    Created with value: {self._colorize(current_value, Colors.GREEN)}")
            
            elif log['event_type'] == EventType.VARIABLE_UPDATE.value:
                old_val = log['old_value']
                new_val = log['new_value']
                current_value = new_val
                print(f"    Updated: {old_val} → {self._colorize(new_val, Colors.YELLOW)}")
            
            elif log['event_type'] == EventType.VARIABLE_DELETE.value:
                print(f"    Deleted (was: {self._colorize(log['old_value'], Colors.RED)})")
                current_value = None
            
            if log.get('reasoning'):
                reasoning_colored = self._colorize(log['reasoning'], Colors.CYAN)
                print(f"    Reasoning: {reasoning_colored}")
            
            print()
        
        # Show current status
        try:
            actual_current = self.audit_db.get_variable(variable_name)
            if actual_current:
                status_color = Colors.GREEN
                status = f"EXISTS (value: {actual_current})"
            else:
                status_color = Colors.RED
                status = "DOES NOT EXIST"
        except Exception:
            status_color = Colors.YELLOW
            status = "UNKNOWN"
        
        print(self._colorize(f"Current status: {status}", status_color))
    
    def show_decision_trail(self, limit: Optional[int] = None, session_id: Optional[str] = None) -> None:
        """Show decision and reasoning trail.
        
        Parameters
        ----------
        limit : int, optional
            Maximum number of entries to show
        session_id : str, optional
            Filter by specific session
        """
        self._print_header("Decision and Reasoning Trail")
        
        # Get decision and reasoning logs
        decision_logs = self.audit_db.get_audit_logs(
            event_type=EventType.DECISION_MADE,
            limit=limit,
            session_id=session_id
        )
        
        reasoning_logs = self.audit_db.get_audit_logs(
            event_type=EventType.REASONING_LOGGED,
            limit=limit,
            session_id=session_id
        )
        
        # Combine and sort by timestamp
        all_logs = decision_logs + reasoning_logs
        all_logs.sort(key=lambda x: x['timestamp'], reverse=True)
        
        if not all_logs:
            print(self._colorize("No decision or reasoning logs found.", Colors.YELLOW))
            return
        
        for log in all_logs:
            timestamp = self._format_timestamp(log['timestamp'])
            
            if log['event_type'] == EventType.DECISION_MADE.value:
                event_label = self._colorize("[DECISION]", Colors.BLUE)
                content = log.get('new_value', 'No decision content')
            else:  # reasoning_logged
                event_label = self._colorize("[REASONING]", Colors.CYAN)
                context = log.get('old_value', 'No context')
                result = log.get('new_value', 'No result')
                content = f"Context: {context} → Result: {result}"
            
            print(f"{timestamp} {event_label}")
            print(f"  Content: {content}")
            
            if log.get('reasoning'):
                reasoning_colored = self._colorize(log['reasoning'], Colors.CYAN)
                print(f"  Reasoning: {reasoning_colored}")
            
            # Show metadata if available
            if log.get('metadata'):
                try:
                    metadata = json.loads(log['metadata']) if isinstance(log['metadata'], str) else log['metadata']
                    if metadata:
                        meta_str = ", ".join([f"{k}: {v}" for k, v in metadata.items()])
                        print(f"  Metadata: {self._colorize(meta_str, Colors.DIM)}")
                except (json.JSONDecodeError, TypeError):
                    pass
            
            print()


def main():
    """Main entry point for the audit log viewer."""
    parser = argparse.ArgumentParser(
        description="View and analyze audit logs from natural language macro execution",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --recent 10                    # Show 10 most recent logs
  %(prog)s --variable user_name           # Show history for specific variable
  %(prog)s --decisions --session sess1    # Show decisions from specific session
  %(prog)s --summary --last-hours 24      # Show summary for last 24 hours
  %(prog)s --format json --recent 5       # Output recent logs in JSON
        """
    )
    
    parser.add_argument(
        "--db", "-d",
        default="variables.db",
        help="SQLite database file path (default: variables.db)"
    )
    
    parser.add_argument(
        "--recent", "-r",
        type=int,
        help="Show N most recent audit logs"
    )
    
    parser.add_argument(
        "--variable", "-v",
        help="Show complete history for a specific variable"
    )
    
    parser.add_argument(
        "--decisions",
        action="store_true",
        help="Show decision and reasoning trail"
    )
    
    parser.add_argument(
        "--summary", "-s",
        action="store_true",
        help="Show summary statistics of audit logs"
    )
    
    parser.add_argument(
        "--event-type", "-e",
        help="Filter by event type (e.g., variable_create, decision_made)"
    )
    
    parser.add_argument(
        "--session",
        help="Filter by session ID"
    )
    
    parser.add_argument(
        "--last-hours",
        type=int,
        help="Show logs from last N hours"
    )
    
    parser.add_argument(
        "--last-days",
        type=int,
        help="Show logs from last N days"
    )
    
    parser.add_argument(
        "--format", "-f",
        choices=["table", "json"],
        default="table",
        help="Output format (default: table)"
    )
    
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable colored output"
    )
    
    parser.add_argument(
        "--limit", "-l",
        type=int,
        default=50,
        help="Maximum number of logs to show (default: 50)"
    )
    
    args = parser.parse_args()
    
    # Check if database exists
    if not Path(args.db).exists():
        print(f"Error: Database file '{args.db}' not found.")
        print("Run some natural language macros first to create audit logs.")
        sys.exit(1)
    
    # Initialize viewer
    viewer = AuditViewer(args.db, use_colors=not args.no_color)
    
    try:
        # Determine time filters
        start_time = None
        end_time = None
        
        if args.last_hours:
            start_time = datetime.now() - timedelta(hours=args.last_hours)
        elif args.last_days:
            start_time = datetime.now() - timedelta(days=args.last_days)
        
        # Handle specific actions
        if args.variable:
            viewer.show_variable_history(args.variable, args.limit)
        
        elif args.decisions:
            viewer.show_decision_trail(args.limit, args.session)
        
        elif args.summary:
            logs = viewer.audit_db.get_audit_logs(
                limit=args.limit,
                event_type=args.event_type,
                session_id=args.session,
                start_time=start_time,
                end_time=end_time
            )
            viewer.display_logs_summary(logs)
        
        else:
            # Show general logs
            limit = args.recent if args.recent else args.limit
            logs = viewer.audit_db.get_audit_logs(
                limit=limit,
                event_type=args.event_type,
                session_id=args.session,
                start_time=start_time,
                end_time=end_time
            )
            
            if args.format == "json":
                viewer.display_logs_json(logs)
            else:
                viewer.display_logs_table(logs)
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()