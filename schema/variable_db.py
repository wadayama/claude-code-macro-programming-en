"""SQLite-based variable management system with simple schema validation.

This module provides schema validation for natural language macro programming.
It demonstrates core concepts of type safety in a simple, understandable way.
"""

import sqlite3
import time
import random
import json
from pathlib import Path
from typing import Any, Union


class SchemaValidationError(Exception):
    """Exception raised when schema validation fails."""
    pass


class VariableDB:
    """SQLite-based variable storage with integrated schema validation.

    This class demonstrates unified variable storage with optional type safety:
    - save_variable(name, value) → Basic storage without validation
    - save_variable(name, value, type_name) → Type-safe storage with validation
    - Built-in types: integer, number, string, boolean
    - Constrained types: age (0-150), percentage (0-100), status (enum)
    """

    def __init__(self, db_path: str | Path = "variables.db", timeout: float = 30.0):
        """Initialize the variable database with schema support.

        Parameters
        ----------
        db_path : str or Path, optional
            Path to the SQLite database file, by default "variables.db"
        timeout : float, optional
            Database connection timeout in seconds, by default 30.0
        """
        self.db_path = Path(db_path)
        self.timeout = timeout
        self._init_schemas()
        self._init_database()

    def _init_schemas(self) -> None:
        """Initialize schema definitions from external JSON file."""
        schema_file = Path("test_schema.json")
        
        if schema_file.exists():
            try:
                with open(schema_file, 'r', encoding='utf-8') as f:
                    schema_data = json.load(f)
                    
                # Extract schemas from JSON structure
                if "schemas" in schema_data:
                    self.schemas = {}
                    for name, schema_def in schema_data["schemas"].items():
                        # Convert JSON Schema format to internal format
                        converted_schema = self._convert_json_schema(schema_def)
                        self.schemas[name] = converted_schema
                else:
                    raise ValueError("JSON file must have 'schemas' key")
                    
                print(f"Loaded {len(self.schemas)} schemas from {schema_file}")
                
            except (json.JSONDecodeError, FileNotFoundError, ValueError) as e:
                print(f"Warning: Could not load schema file {schema_file}: {e}")
                print("Using fallback internal schema definitions")
                self._init_fallback_schemas()
        else:
            print(f"Schema file {schema_file} not found, using fallback internal definitions")
            self._init_fallback_schemas()
    
    def _convert_json_schema(self, json_schema: dict) -> dict:
        """Convert JSON Schema format to internal schema format."""
        converted = {"type": json_schema["type"]}
        
        # Handle range constraints
        if "minimum" in json_schema:
            converted["min"] = json_schema["minimum"]
        if "maximum" in json_schema:
            converted["max"] = json_schema["maximum"]
            
        # Handle enumeration constraints
        if "enum" in json_schema:
            converted["enum"] = json_schema["enum"]
            
        return converted
    
    def _init_fallback_schemas(self) -> None:
        """Initialize fallback schema definitions (used when external file fails)."""
        self.schemas = {
            # Basic types
            "integer": {"type": "integer"},
            "number": {"type": "number"},
            "string": {"type": "string"},
            "boolean": {"type": "boolean"},
            
            # Range-constrained types (for demonstration)
            "age": {"type": "integer", "min": 0, "max": 150},
            "percentage": {"type": "number", "min": 0, "max": 100},
            
            # Enumeration type (for demonstration)
            "status": {"type": "string", "enum": ["pending", "completed", "failed"]}
        }

    def _init_database(self) -> None:
        """Initialize the database schema."""
        with sqlite3.connect(self.db_path, timeout=self.timeout) as conn:
            # Enable WAL mode for better concurrency
            conn.execute("PRAGMA journal_mode=WAL")
            conn.execute("PRAGMA synchronous=NORMAL")
            conn.execute("PRAGMA cache_size=10000")
            conn.execute("PRAGMA temp_store=memory")
            
            # Variables table
            conn.execute("""
                CREATE TABLE IF NOT EXISTS variables (
                    name TEXT PRIMARY KEY,
                    value TEXT NOT NULL,
                    type_name TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # Update trigger
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
        """Execute database operation with retry logic."""
        for attempt in range(max_retries):
            try:
                return operation()
            except sqlite3.OperationalError as e:
                error_msg = str(e).lower()
                if ("database is locked" in error_msg or "database is busy" in error_msg) and attempt < max_retries - 1:
                    wait_time = random.uniform(0.05, 0.15) * (2 ** attempt)
                    time.sleep(wait_time)
                    continue
                raise

    def _validate_value(self, value: str, type_name: str) -> Any:
        """Validate value against schema and return converted value.
        
        Parameters
        ----------
        value : str
            String value to validate
        type_name : str
            Type name to validate against
            
        Returns
        -------
        Any
            Converted and validated value
            
        Raises
        ------
        SchemaValidationError
            If validation fails
        """
        if type_name not in self.schemas:
            raise SchemaValidationError(f"Unknown type: {type_name}")
        
        schema = self.schemas[type_name]
        schema_type = schema["type"]
        
        try:
            # Type conversion
            if schema_type == "integer":
                converted_value = int(value)
            elif schema_type == "number":
                converted_value = float(value)
            elif schema_type == "boolean":
                if value.lower() in ["true", "1", "yes"]:
                    converted_value = True
                elif value.lower() in ["false", "0", "no"]:
                    converted_value = False
                else:
                    raise ValueError(f"Invalid boolean value: {value}")
            else:  # string
                converted_value = str(value)
                
        except ValueError as e:
            raise SchemaValidationError(f"Type conversion failed for {type_name}: {e}")
        
        # Range validation
        if "min" in schema or "max" in schema:
            if schema_type not in ["integer", "number"]:
                raise SchemaValidationError(f"Range constraints only apply to numbers, not {schema_type}")
            
            if "min" in schema and converted_value < schema["min"]:
                raise SchemaValidationError(
                    f"Value {converted_value} is below minimum {schema['min']} for type {type_name}"
                )
            if "max" in schema and converted_value > schema["max"]:
                raise SchemaValidationError(
                    f"Value {converted_value} is above maximum {schema['max']} for type {type_name}"
                )
        
        # Enumeration validation
        if "enum" in schema:
            if converted_value not in schema["enum"]:
                raise SchemaValidationError(
                    f"Value '{converted_value}' not in allowed values {schema['enum']} for type {type_name}"
                )
        
        return converted_value

    def save_variable(self, name: str, value: str, type_name: str = None) -> None:
        """Save a variable with optional schema validation.

        This unified method demonstrates both basic and type-safe variable storage.
        
        Parameters
        ----------
        name : str
            Variable name (without the {{}} brackets)
        value : str
            Variable value to store (as string)
        type_name : str, optional
            Type name for validation. If None, saves without validation.
            
        Raises
        ------
        SchemaValidationError
            If type_name is provided and validation fails
        """
        # Type validation if type_name is specified
        if type_name is not None:
            validated_value = self._validate_value(value, type_name)
            
            # Convert back to string for storage
            if isinstance(validated_value, bool):
                value_str = "true" if validated_value else "false"
            else:
                value_str = str(validated_value)
        else:
            # No validation, store as-is
            value_str = value
        
        def _save_operation():
            with sqlite3.connect(self.db_path, timeout=self.timeout) as conn:
                conn.execute(
                    """
                    INSERT OR REPLACE INTO variables (name, value, type_name, updated_at)
                    VALUES (?, ?, ?, CURRENT_TIMESTAMP)
                    """,
                    (name, value_str, type_name),
                )
                conn.commit()
        
        self._execute_with_retry(_save_operation)

    def get_variable(self, name: str) -> str:
        """Retrieve a variable value as string (backward compatibility).

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

    def get_variable_typed(self, name: str) -> tuple[Any, str | None]:
        """Retrieve a variable with type conversion and type information.
        
        This demonstrates how typed retrieval works.

        Parameters
        ----------
        name : str
            Variable name

        Returns
        -------
        tuple[Any, str | None]
            (converted_value, type_name) or (string_value, None) if no type
        """
        def _get_operation():
            with sqlite3.connect(self.db_path, timeout=self.timeout) as conn:
                cursor = conn.execute(
                    "SELECT value, type_name FROM variables WHERE name = ?", 
                    (name,)
                )
                result = cursor.fetchone()
                if not result:
                    return "", None
                
                value, type_name = result
                if type_name is None:
                    return value, None
                
                # Convert value back to proper type
                try:
                    converted_value = self._validate_value(value, type_name)
                    return converted_value, type_name
                except SchemaValidationError:
                    # If validation fails, return as string with error indication
                    return f"[VALIDATION_ERROR] {value}", type_name
        
        return self._execute_with_retry(_get_operation)

    def list_variables(self) -> dict[str, str]:
        """List all variables as strings (backward compatibility).

        Returns
        -------
        dict[str, str]
            Dictionary mapping variable names to their string values
        """
        def _list_operation():
            with sqlite3.connect(self.db_path, timeout=self.timeout) as conn:
                cursor = conn.execute("SELECT name, value FROM variables ORDER BY name")
                return dict(cursor.fetchall())
        
        return self._execute_with_retry(_list_operation)

    def list_variables_with_types(self) -> dict[str, tuple[str, str | None]]:
        """List all variables with their type information.

        Returns
        -------
        dict[str, tuple[str, str | None]]
            Dictionary mapping variable names to (value, type_name)
        """
        def _list_operation():
            with sqlite3.connect(self.db_path, timeout=self.timeout) as conn:
                cursor = conn.execute("SELECT name, value, type_name FROM variables ORDER BY name")
                return {name: (value, type_name) for name, value, type_name in cursor.fetchall()}
        
        return self._execute_with_retry(_list_operation)

    def validate_all(self) -> dict[str, bool | str]:
        """Validate all typed variables against their schemas.
        
        This demonstrates comprehensive validation checking.

        Returns
        -------
        dict[str, bool | str]
            Dictionary with variable names as keys and validation results as values.
            True if valid, error message string if invalid.
        """
        results = {}
        variables_with_types = self.list_variables_with_types()
        
        for name, (value, type_name) in variables_with_types.items():
            if type_name is None:
                continue  # Skip untyped variables
            
            try:
                self._validate_value(value, type_name)
                results[name] = True
            except SchemaValidationError as e:
                results[name] = str(e)
        
        return results

    def get_schema_info(self, type_name: str) -> dict | None:
        """Get information about a schema type.

        Parameters
        ----------
        type_name : str
            Name of the type

        Returns
        -------
        dict | None
            Schema definition or None if not found
        """
        return self.schemas.get(type_name)

    def list_schema_types(self) -> list[str]:
        """List all available schema types.

        Returns
        -------
        list[str]
            List of available type names
        """
        return list(self.schemas.keys())

    # Keep existing methods for backward compatibility
    def delete_variable(self, name: str) -> bool:
        """Delete a variable from the database."""
        def _delete_operation():
            with sqlite3.connect(self.db_path, timeout=self.timeout) as conn:
                cursor = conn.execute("DELETE FROM variables WHERE name = ?", (name,))
                conn.commit()
                return cursor.rowcount > 0
        
        return self._execute_with_retry(_delete_operation)

    def clear_all(self) -> int:
        """Clear all variables from the database."""
        def _clear_operation():
            with sqlite3.connect(self.db_path, timeout=self.timeout) as conn:
                cursor = conn.execute("DELETE FROM variables")
                conn.commit()
                return cursor.rowcount
        
        return self._execute_with_retry(_clear_operation)

    def get_variable_info(self, name: str) -> dict[str, str] | None:
        """Get detailed information about a variable."""
        def _info_operation():
            with sqlite3.connect(self.db_path, timeout=self.timeout) as conn:
                cursor = conn.execute(
                    """
                    SELECT name, value, type_name, created_at, updated_at 
                    FROM variables WHERE name = ?
                    """,
                    (name,),
                )
                result = cursor.fetchone()
                if result:
                    return {
                        "name": result[0],
                        "value": result[1],
                        "type_name": result[2] or "untyped",
                        "created_at": result[3],
                        "updated_at": result[4],
                    }
                return None
        
        return self._execute_with_retry(_info_operation)


# Convenience functions for direct use
_default_db = VariableDB()


def save_variable(name: str, value: str, type_name: str = None) -> None:
    """Save a variable using the default database instance.
    
    Parameters
    ----------
    name : str
        Variable name
    value : str  
        Variable value
    type_name : str, optional
        Type name for validation. If None, saves without validation.
    """
    _default_db.save_variable(name, value, type_name)


def get_variable(name: str) -> str:
    """Get a variable using the default database instance."""
    return _default_db.get_variable(name)


def get_variable_typed(name: str) -> tuple[Any, str | None]:
    """Get a typed variable using the default database instance."""
    return _default_db.get_variable_typed(name)


def list_variables() -> dict[str, str]:
    """List all variables using the default database instance."""
    return _default_db.list_variables()


def validate_all() -> dict[str, bool | str]:
    """Validate all variables using the default database instance."""
    return _default_db.validate_all()


def delete_variable(name: str) -> bool:
    """Delete a variable using the default database instance."""
    return _default_db.delete_variable(name)