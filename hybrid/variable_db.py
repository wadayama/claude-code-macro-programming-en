"""SQLite-based variable management system for natural language macro programming.

This module provides a replacement for variables.json file management
used in CLAUDE.md natural language macro syntax. Variables are stored
in a SQLite database for better performance and reliability.
"""

import sqlite3
import time
import random
from pathlib import Path


class VariableDB:
    """SQLite-based variable storage manager.

    This class provides the core functionality to replace variables.json
    with SQLite database operations for the natural language macro system.
    """

    def __init__(self, db_path: str | Path = "variables.db", timeout: float = 30.0):
        """Initialize the variable database.

        Parameters
        ----------
        db_path : str or Path, optional
            Path to the SQLite database file, by default "variables.db"
        timeout : float, optional
            Database connection timeout in seconds, by default 30.0
        """
        self.db_path = Path(db_path)
        self.timeout = timeout
        self._init_database()

    def _init_database(self) -> None:
        """Initialize the database schema and optimize for multi-process access."""
        with sqlite3.connect(self.db_path, timeout=self.timeout) as conn:
            # Enable WAL mode for better concurrency
            conn.execute("PRAGMA journal_mode=WAL")
            
            # Optimize for multi-process access
            conn.execute("PRAGMA synchronous=NORMAL")  # Balance safety/performance
            conn.execute("PRAGMA cache_size=10000")    # Increase cache for performance
            conn.execute("PRAGMA temp_store=memory")   # Use memory for temp storage
            
            conn.execute("""
                CREATE TABLE IF NOT EXISTS variables (
                    name TEXT PRIMARY KEY,
                    value TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # Create trigger to update timestamp on value changes
            conn.execute("""
                CREATE TRIGGER IF NOT EXISTS update_timestamp 
                AFTER UPDATE ON variables
                BEGIN
                    UPDATE variables 
                    SET updated_at = CURRENT_TIMESTAMP 
                    WHERE name = NEW.name;
                END
            """)
            conn.commit()

    def _execute_with_retry(self, operation, max_retries: int = 3):
        """Execute database operation with retry logic for concurrent access.
        
        Parameters
        ----------
        operation : callable
            Database operation to execute
        max_retries : int, optional
            Maximum number of retry attempts, by default 3
            
        Returns
        -------
        Any
            Result of the operation
            
        Raises
        ------
        sqlite3.OperationalError
            If operation fails after all retries
        """
        for attempt in range(max_retries):
            try:
                return operation()
            except sqlite3.OperationalError as e:
                error_msg = str(e).lower()
                if ("database is locked" in error_msg or "database is busy" in error_msg) and attempt < max_retries - 1:
                    # Exponential backoff with jitter
                    wait_time = random.uniform(0.05, 0.15) * (2 ** attempt)
                    time.sleep(wait_time)
                    continue
                # Re-raise if not a locking issue or final attempt
                raise
    
    def save_variable(self, name: str, value: str) -> None:
        """Save or update a variable in the database.

        This method replaces the JSON file save operation from CLAUDE.md.
        When a user requests "{{variable_name}}にVALUEを保存してください",
        this method handles the storage.

        Parameters
        ----------
        name : str
            Variable name (without the {{}} brackets)
        value : str
            Variable value to store
        """
        def _save_operation():
            with sqlite3.connect(self.db_path, timeout=self.timeout) as conn:
                conn.execute(
                    """
                    INSERT OR REPLACE INTO variables (name, value, updated_at)
                    VALUES (?, ?, CURRENT_TIMESTAMP)
                """,
                    (name, value),
                )
                conn.commit()
        
        self._execute_with_retry(_save_operation)

    def get_variable(self, name: str) -> str:
        """Retrieve a variable value from the database.

        This method replaces the JSON file read operation from CLAUDE.md.
        When a user requests "{{variable_name}}を取得してください",
        this method handles the retrieval.

        Parameters
        ----------
        name : str
            Variable name (without the {{}} brackets)

        Returns
        -------
        str
            Variable value, or empty string if not found
        """
        def _get_operation():
            with sqlite3.connect(self.db_path, timeout=self.timeout) as conn:
                cursor = conn.execute("SELECT value FROM variables WHERE name = ?", (name,))
                result = cursor.fetchone()
                return result[0] if result else ""
        
        return self._execute_with_retry(_get_operation)

    def list_variables(self) -> dict[str, str]:
        """List all variables in the database.

        Returns
        -------
        Dict[str, str]
            Dictionary mapping variable names to their values
        """
        def _list_operation():
            with sqlite3.connect(self.db_path, timeout=self.timeout) as conn:
                cursor = conn.execute("SELECT name, value FROM variables ORDER BY name")
                return dict(cursor.fetchall())
        
        return self._execute_with_retry(_list_operation)

    def delete_variable(self, name: str) -> bool:
        """Delete a variable from the database.

        Parameters
        ----------
        name : str
            Variable name to delete

        Returns
        -------
        bool
            True if variable was deleted, False if it didn't exist
        """
        def _delete_operation():
            with sqlite3.connect(self.db_path, timeout=self.timeout) as conn:
                cursor = conn.execute("DELETE FROM variables WHERE name = ?", (name,))
                conn.commit()
                return cursor.rowcount > 0
        
        return self._execute_with_retry(_delete_operation)

    def clear_all(self) -> int:
        """Clear all variables from the database.

        Returns
        -------
        int
            Number of variables that were deleted
        """
        def _clear_operation():
            with sqlite3.connect(self.db_path, timeout=self.timeout) as conn:
                cursor = conn.execute("DELETE FROM variables")
                conn.commit()
                return cursor.rowcount
        
        return self._execute_with_retry(_clear_operation)

    def get_variable_info(self, name: str) -> dict[str, str] | None:
        """Get detailed information about a variable.

        Parameters
        ----------
        name : str
            Variable name

        Returns
        -------
        Optional[Dict[str, str]]
            Dictionary with name, value, created_at, updated_at, or None if not found
        """
        def _info_operation():
            with sqlite3.connect(self.db_path, timeout=self.timeout) as conn:
                cursor = conn.execute(
                    """
                    SELECT name, value, created_at, updated_at 
                    FROM variables WHERE name = ?
                """,
                    (name,),
                )
                result = cursor.fetchone()
                if result:
                    return {
                        "name": result[0],
                        "value": result[1],
                        "created_at": result[2],
                        "updated_at": result[3],
                    }
                return None
        
        return self._execute_with_retry(_info_operation)


# Convenience functions for direct use
_default_db = VariableDB()


def save_variable(name: str, value: str) -> None:
    """Save a variable using the default database instance."""
    _default_db.save_variable(name, value)


def get_variable(name: str) -> str:
    """Get a variable using the default database instance."""
    return _default_db.get_variable(name)


def list_variables() -> dict[str, str]:
    """List all variables using the default database instance."""
    return _default_db.list_variables()


def delete_variable(name: str) -> bool:
    """Delete a variable using the default database instance."""
    return _default_db.delete_variable(name)
