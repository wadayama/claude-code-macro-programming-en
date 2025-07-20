#!/usr/bin/env python3
"""Integrated watcher for both SQLite variables and Chroma vector database.

This tool provides unified monitoring of the complete natural language macro
system state, including both variable storage and vector knowledge/experience.
"""

import argparse
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Set

from variable_db import VariableDB
from simple_chroma_rag import SimpleChromaRAG


class Colors:
    """ANSI color codes for terminal output."""
    
    GREEN = "\033[92m"    # New items
    YELLOW = "\033[93m"   # Modified items
    RED = "\033[91m"      # Deleted items
    BLUE = "\033[94m"     # Headers
    CYAN = "\033[96m"     # Timestamps/Variables
    PURPLE = "\033[95m"   # Knowledge items
    ORANGE = "\033[33m"   # Experience items
    RESET = "\033[0m"     # Reset color
    BOLD = "\033[1m"      # Bold text


class IntegratedWatcher:
    """Monitor both SQLite variables and Chroma vector database."""
    
    def __init__(self, variable_db_path: str = "variables.db", 
                 chroma_db_path: str = "./chroma_db", use_colors: bool = True):
        """Initialize the integrated watcher.
        
        Parameters
        ----------
        variable_db_path : str
            Path to the SQLite variables database
        chroma_db_path : str
            Path to the Chroma database directory
        use_colors : bool
            Whether to use colored output
        """
        self.variable_db = VariableDB(variable_db_path)
        self.chroma_rag = SimpleChromaRAG(chroma_db_path)
        self.use_colors = use_colors and sys.stdout.isatty()
        
        # State tracking
        self.last_variables: Dict[str, str] = {}
        self.last_knowledge_ids: Set[str] = set()
        self.last_experience_ids: Set[str] = set()
        
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
    
    def _get_chroma_items(self, collection_name: str) -> Dict:
        """Get items from Chroma collection."""
        try:
            if collection_name == "knowledge_base":
                collection = self.chroma_rag.knowledge_collection
            else:
                collection = self.chroma_rag.experience_collection
            
            results = collection.get()
            items = {}
            if results['ids']:
                for i, doc_id in enumerate(results['ids']):
                    items[doc_id] = {
                        'document': results['documents'][i],
                        'metadata': results['metadatas'][i] if results['metadatas'] else {}
                    }
            return items
        except Exception:
            return {}
    
    def display_system_status(self) -> None:
        """Display complete system status."""
        self._print_header(f"Natural Language Macro System Status - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # SQLite Variables
        variables = self.variable_db.list_variables()
        print(f"\n{self._colorize('📊 SQLite Variables:', Colors.BOLD)}")
        print(f"   Count: {self._colorize(str(len(variables)), Colors.CYAN)}")
        
        if variables:
            for name, value in list(variables.items())[:3]:  # Show first 3
                value_preview = value[:40] + "..." if len(value) > 40 else value
                print(f"   {{{{ {self._colorize(name, Colors.CYAN)} }}}} = {value_preview}")
            if len(variables) > 3:
                print(f"   ... and {len(variables) - 3} more")
        
        # Chroma Vector Database
        chroma_stats = self.chroma_rag.get_stats()
        print(f"\n{self._colorize('🧠 Chroma Vector Database:', Colors.BOLD)}")
        print(f"   Knowledge: {self._colorize(str(chroma_stats['knowledge_count']), Colors.PURPLE)}")
        print(f"   Experience: {self._colorize(str(chroma_stats['experience_count']), Colors.ORANGE)}")
        print(f"   Total Vector Items: {self._colorize(str(chroma_stats['knowledge_count'] + chroma_stats['experience_count']), Colors.BOLD)}")
        
        # Show recent additions
        knowledge_items = self._get_chroma_items("knowledge_base")
        if knowledge_items:
            print(f"\n{self._colorize('📚 Recent Knowledge:', Colors.PURPLE)}")
            for i, (doc_id, item) in enumerate(list(knowledge_items.items())[-2:], 1):
                source = item['metadata'].get('source', 'unknown')
                content_preview = item['document'][:50] + "..." if len(item['document']) > 50 else item['document']
                print(f"   {i}. [{doc_id[:8]}...] from {source}")
                print(f"      {content_preview}")
        
        experience_items = self._get_chroma_items("experience_base")
        if experience_items:
            print(f"\n{self._colorize('💡 Recent Experience:', Colors.ORANGE)}")
            for i, (doc_id, item) in enumerate(list(experience_items.items())[-2:], 1):
                success = item['metadata'].get('success', True)
                status = self._colorize("SUCCESS", Colors.GREEN) if success else self._colorize("FAILURE", Colors.RED)
                content_preview = item['document'][:50] + "..." if len(item['document']) > 50 else item['document']
                print(f"   {i}. [{doc_id[:8]}...] ({status})")
                print(f"      {content_preview}")
    
    def watch_continuous(self, interval: float = 2.0) -> None:
        """Watch both systems continuously for changes."""
        self._print_header("Integrated Natural Language Macro System Monitoring")
        print(f"Update interval: {interval}s (Press Ctrl+C to stop)\n")
        
        # Initialize state
        self.last_variables = self.variable_db.list_variables()
        
        knowledge_items = self._get_chroma_items("knowledge_base")
        experience_items = self._get_chroma_items("experience_base")
        self.last_knowledge_ids = set(knowledge_items.keys())
        self.last_experience_ids = set(experience_items.keys())
        
        print(f"{self._get_timestamp()} Initial state: "
              f"{self._colorize(f'{len(self.last_variables)} variables', Colors.CYAN)}, "
              f"{self._colorize(f'{len(self.last_knowledge_ids)} knowledge', Colors.PURPLE)}, "
              f"{self._colorize(f'{len(self.last_experience_ids)} experience', Colors.ORANGE)}")
        
        try:
            while True:
                time.sleep(interval)
                self._check_all_changes()
                
        except KeyboardInterrupt:
            print(f"\n\n{self._colorize('Integrated monitoring stopped.', Colors.BLUE)}")
    
    def _check_all_changes(self) -> None:
        """Check for changes in both systems."""
        timestamp = self._get_timestamp()
        changes_detected = False
        
        # Check variable changes
        current_variables = self.variable_db.list_variables()
        
        # New variables
        new_vars = set(current_variables.keys()) - set(self.last_variables.keys())
        for name in new_vars:
            changes_detected = True
            value_preview = current_variables[name][:40] + "..." if len(current_variables[name]) > 40 else current_variables[name]
            print(f"{timestamp} {self._colorize('NEW VARIABLE', Colors.GREEN)}: "
                  f"{{{{ {self._colorize(name, Colors.CYAN)} }}}} = \"{value_preview}\"")
        
        # Deleted variables
        deleted_vars = set(self.last_variables.keys()) - set(current_variables.keys())
        for name in deleted_vars:
            changes_detected = True
            print(f"{timestamp} {self._colorize('DELETED VARIABLE', Colors.RED)}: "
                  f"{{{{ {self._colorize(name, Colors.CYAN)} }}}}")
        
        # Modified variables
        common_vars = set(self.last_variables.keys()) & set(current_variables.keys())
        for name in common_vars:
            if self.last_variables[name] != current_variables[name]:
                changes_detected = True
                new_value_preview = current_variables[name][:40] + "..." if len(current_variables[name]) > 40 else current_variables[name]
                print(f"{timestamp} {self._colorize('MODIFIED VARIABLE', Colors.YELLOW)}: "
                      f"{{{{ {self._colorize(name, Colors.CYAN)} }}}} = \"{new_value_preview}\"")
        
        # Check Chroma changes
        knowledge_items = self._get_chroma_items("knowledge_base")
        experience_items = self._get_chroma_items("experience_base")
        
        current_knowledge_ids = set(knowledge_items.keys())
        current_experience_ids = set(experience_items.keys())
        
        # New knowledge
        new_knowledge = current_knowledge_ids - self.last_knowledge_ids
        for doc_id in new_knowledge:
            changes_detected = True
            item = knowledge_items[doc_id]
            source = item['metadata'].get('source', 'unknown')
            content_preview = item['document'][:50] + "..." if len(item['document']) > 50 else item['document']
            
            print(f"{timestamp} {self._colorize('NEW KNOWLEDGE', Colors.GREEN)}: "
                  f"{self._colorize(f'[{doc_id[:8]}...]', Colors.PURPLE)} from {source}")
            print(f"         {content_preview}")
        
        # New experience
        new_experience = current_experience_ids - self.last_experience_ids
        for doc_id in new_experience:
            changes_detected = True
            item = experience_items[doc_id]
            success = item['metadata'].get('success', True)
            status_text = "SUCCESS" if success else "FAILURE"
            status_color = Colors.GREEN if success else Colors.RED
            content_preview = item['document'][:50] + "..." if len(item['document']) > 50 else item['document']
            
            print(f"{timestamp} {self._colorize('NEW EXPERIENCE', Colors.ORANGE)}: "
                  f"{self._colorize(f'[{doc_id[:8]}...]', Colors.ORANGE)} ({self._colorize(status_text, status_color)})")
            print(f"         {content_preview}")
        
        # Update state
        self.last_variables = current_variables.copy()
        self.last_knowledge_ids = current_knowledge_ids
        self.last_experience_ids = current_experience_ids
        
        if changes_detected:
            print(f"         System state: "
                  f"{self._colorize(f'{len(current_variables)} vars', Colors.CYAN)}, "
                  f"{self._colorize(f'{len(current_knowledge_ids)} knowledge', Colors.PURPLE)}, "
                  f"{self._colorize(f'{len(current_experience_ids)} experience', Colors.ORANGE)}")
    
    def test_search_integration(self, query: str) -> None:
        """Test integrated search across variables and vector database."""
        self._print_header(f"Integrated Search Test: '{query}'")
        
        # Search in variables
        variables = self.variable_db.list_variables()
        matching_vars = {name: value for name, value in variables.items() 
                        if query.lower() in name.lower() or query.lower() in value.lower()}
        
        if matching_vars:
            print(f"\n{self._colorize('🔍 Matching Variables:', Colors.CYAN)}")
            for name, value in matching_vars.items():
                value_preview = value[:60] + "..." if len(value) > 60 else value
                print(f"   {{{{ {self._colorize(name, Colors.CYAN)} }}}} = {value_preview}")
        
        # Search in Chroma
        print(f"\n{self._colorize('🧠 Vector Search Results:', Colors.PURPLE)}")
        knowledge_results = self.chroma_rag.search_knowledge(query, n_results=2)
        
        for i, result in enumerate(knowledge_results, 1):
            source = result['metadata'].get('source', 'unknown')
            distance = result.get('distance', 'unknown')
            print(f"\n   {i}. Knowledge (distance: {distance:.4f}, source: {source})")
            print(f"      {result['document'][:80]}{'...' if len(result['document']) > 80 else ''}")
        
        experience_results = self.chroma_rag.search_similar_experience(query, success_only=True, n_results=2)
        
        for i, result in enumerate(experience_results, 1):
            distance = result.get('distance', 'unknown')
            print(f"\n   {i}. Experience (distance: {distance:.4f})")
            print(f"      {result['experience'][:80]}{'...' if len(result['experience']) > 80 else ''}")


def main():
    """Main entry point for the integrated watcher."""
    parser = argparse.ArgumentParser(
        description="Watch both SQLite variables and Chroma vector database",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --status                        # Show system status
  %(prog)s --watch --interval 1.0         # Watch continuously (1s interval)
  %(prog)s --search "Python API"          # Test integrated search
        """
    )
    
    parser.add_argument(
        "--variable-db",
        default="variables.db",
        help="SQLite variables database file (default: variables.db)"
    )
    
    parser.add_argument(
        "--chroma-db", 
        default="./chroma_db",
        help="Chroma database directory (default: ./chroma_db)"
    )
    
    parser.add_argument(
        "--status", "-s",
        action="store_true",
        help="Show system status"
    )
    
    parser.add_argument(
        "--watch", "-w",
        action="store_true",
        help="Monitor both systems continuously"
    )
    
    parser.add_argument(
        "--interval", "-i",
        type=float,
        default=2.0,
        help="Update interval in seconds (default: 2.0)"
    )
    
    parser.add_argument(
        "--search",
        metavar="QUERY",
        help="Test integrated search functionality"
    )
    
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable colored output"
    )
    
    args = parser.parse_args()
    
    # Initialize watcher
    watcher = IntegratedWatcher(
        args.variable_db, 
        args.chroma_db, 
        use_colors=not args.no_color
    )
    
    try:
        if args.search:
            watcher.test_search_integration(args.search)
        elif args.watch:
            watcher.watch_continuous(args.interval)
        else:
            # Default: show status
            watcher.display_system_status()
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()