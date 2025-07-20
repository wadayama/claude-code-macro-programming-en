"""SQLite-based audit logging system for natural language macro programming.

This module extends the variable management system with comprehensive audit logging
capabilities, recording all variable changes, decisions, and reasoning processes
for transparency and accountability in AI-driven systems.
"""

import json
import sqlite3
import time
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Union

from variable_db import VariableDB


class EventType(Enum):
    """Enumeration of audit log event types."""
    
    VARIABLE_CREATE = "variable_create"
    VARIABLE_UPDATE = "variable_update"
    VARIABLE_DELETE = "variable_delete"
    DECISION_MADE = "decision_made"
    REASONING_LOGGED = "reasoning_logged"
    MACRO_START = "macro_start"
    MACRO_END = "macro_end"
    ERROR_OCCURRED = "error_occurred"
    USER_INPUT = "user_input"
    SYSTEM_ACTION = "system_action"


class AuditLogger(VariableDB):
    """Extended variable database with comprehensive audit logging capabilities.
    
    This class extends VariableDB to provide audit trail functionality,
    recording all operations, decisions, and reasoning processes for
    natural language macro programming systems.
    """

    def __init__(self, db_path: str | Path = "variables.db", timeout: float = 30.0):
        """Initialize the audit logging system.

        Parameters
        ----------
        db_path : str or Path, optional
            Path to the SQLite database file, by default "variables.db"
        timeout : float, optional
            Database connection timeout in seconds, by default 30.0
        """
        super().__init__(db_path, timeout)
        self._init_audit_tables()

    def _init_audit_tables(self) -> None:
        """Initialize audit logging tables in the database."""
        with sqlite3.connect(self.db_path, timeout=self.timeout) as conn:
            # Enable foreign key constraints
            conn.execute("PRAGMA foreign_keys=ON")
            
            # Create audit_logs table
            conn.execute("""
                CREATE TABLE IF NOT EXISTS audit_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    event_type TEXT NOT NULL,
                    variable_name TEXT,
                    old_value TEXT,
                    new_value TEXT,
                    reasoning TEXT,
                    source TEXT DEFAULT 'system',
                    session_id TEXT,
                    metadata TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # Create index for efficient querying
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_audit_timestamp 
                ON audit_logs(timestamp)
            """)
            
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_audit_variable 
                ON audit_logs(variable_name)
            """)
            
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_audit_event_type 
                ON audit_logs(event_type)
            """)

            conn.commit()

    def log_event(
        self,
        event_type: Union[EventType, str],
        variable_name: Optional[str] = None,
        old_value: Optional[str] = None,
        new_value: Optional[str] = None,
        reasoning: Optional[str] = None,
        source: str = "system",
        session_id: Optional[str] = None,
        metadata: Optional[Dict] = None
    ) -> int:
        """Log an audit event to the database.

        Parameters
        ----------
        event_type : EventType or str
            Type of event being logged
        variable_name : str, optional
            Name of the variable involved (if applicable)
        old_value : str, optional
            Previous value of the variable
        new_value : str, optional
            New value of the variable
        reasoning : str, optional
            Explanation or reasoning for the action/decision
        source : str, optional
            Source of the event (system, human, llm), by default "system"
        session_id : str, optional
            Session identifier for grouping related events
        metadata : dict, optional
            Additional metadata as JSON

        Returns
        -------
        int
            ID of the created audit log entry

        Raises
        ------
        sqlite3.OperationalError
            If database operation fails
        """
        def _log_operation():
            with sqlite3.connect(self.db_path, timeout=self.timeout) as conn:
                event_type_str = event_type.value if isinstance(event_type, EventType) else event_type
                metadata_json = json.dumps(metadata) if metadata else None
                
                cursor = conn.execute("""
                    INSERT INTO audit_logs (
                        event_type, variable_name, old_value, new_value,
                        reasoning, source, session_id, metadata
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    event_type_str, variable_name, old_value, new_value,
                    reasoning, source, session_id, metadata_json
                ))
                conn.commit()
                return cursor.lastrowid

        return self._execute_with_retry(_log_operation)

    def save_variable(self, name: str, value: str) -> None:
        """Save or update a variable with audit logging.

        This method overrides the parent class to add audit logging
        for all variable operations.

        Parameters
        ----------
        name : str
            Variable name (without the {{}} brackets)
        value : str
            Variable value to store
        """
        # Get old value for audit trail
        old_value = self.get_variable(name)
        
        # Determine event type
        event_type = EventType.VARIABLE_UPDATE if old_value else EventType.VARIABLE_CREATE
        
        # Save the variable using parent method
        super().save_variable(name, value)
        
        # Log the operation
        self.log_event(
            event_type=event_type,
            variable_name=name,
            old_value=old_value if old_value else None,
            new_value=value,
            source="macro"
        )

    def delete_variable(self, name: str) -> bool:
        """Delete a variable with audit logging.

        Parameters
        ----------
        name : str
            Variable name to delete

        Returns
        -------
        bool
            True if variable was deleted, False if it didn't exist
        """
        # Get old value for audit trail
        old_value = self.get_variable(name)
        
        # Delete using parent method
        deleted = super().delete_variable(name)
        
        # Log the operation if deletion occurred
        if deleted:
            self.log_event(
                event_type=EventType.VARIABLE_DELETE,
                variable_name=name,
                old_value=old_value,
                source="macro"
            )
        
        return deleted

    def log_decision(
        self,
        decision: str,
        reasoning: str,
        affected_variables: Optional[List[str]] = None,
        confidence: Optional[float] = None,
        session_id: Optional[str] = None
    ) -> int:
        """Log a decision made during macro execution.

        Parameters
        ----------
        decision : str
            Description of the decision made
        reasoning : str
            Explanation of why this decision was made
        affected_variables : list of str, optional
            Variables that influenced or were affected by this decision
        confidence : float, optional
            Confidence level of the decision (0.0 to 1.0)
        session_id : str, optional
            Session identifier for grouping related decisions

        Returns
        -------
        int
            ID of the created audit log entry
        """
        metadata = {}
        if affected_variables:
            metadata["affected_variables"] = affected_variables
        if confidence is not None:
            metadata["confidence"] = confidence
        
        return self.log_event(
            event_type=EventType.DECISION_MADE,
            new_value=decision,
            reasoning=reasoning,
            source="llm",
            session_id=session_id,
            metadata=metadata if metadata else None
        )

    def log_reasoning(
        self,
        context: str,
        reasoning: str,
        result: Optional[str] = None,
        session_id: Optional[str] = None
    ) -> int:
        """Log reasoning process during macro execution.

        Parameters
        ----------
        context : str
            Context or situation where reasoning was applied
        reasoning : str
            The reasoning process or explanation
        result : str, optional
            Outcome or result of the reasoning
        session_id : str, optional
            Session identifier for grouping related reasoning

        Returns
        -------
        int
            ID of the created audit log entry
        """
        return self.log_event(
            event_type=EventType.REASONING_LOGGED,
            old_value=context,
            new_value=result,
            reasoning=reasoning,
            source="llm",
            session_id=session_id
        )

    def get_audit_logs(
        self,
        limit: Optional[int] = None,
        event_type: Optional[Union[EventType, str]] = None,
        variable_name: Optional[str] = None,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        session_id: Optional[str] = None
    ) -> List[Dict]:
        """Retrieve audit logs with optional filtering.

        Parameters
        ----------
        limit : int, optional
            Maximum number of logs to retrieve
        event_type : EventType or str, optional
            Filter by specific event type
        variable_name : str, optional
            Filter by variable name
        start_time : datetime, optional
            Filter logs after this timestamp
        end_time : datetime, optional
            Filter logs before this timestamp
        session_id : str, optional
            Filter by session identifier

        Returns
        -------
        list of dict
            List of audit log entries matching the criteria
        """
        def _get_logs_operation():
            with sqlite3.connect(self.db_path, timeout=self.timeout) as conn:
                # Build query with filters
                query = "SELECT * FROM audit_logs WHERE 1=1"
                params = []
                
                if event_type:
                    event_type_str = event_type.value if isinstance(event_type, EventType) else event_type
                    query += " AND event_type = ?"
                    params.append(event_type_str)
                
                if variable_name:
                    query += " AND variable_name = ?"
                    params.append(variable_name)
                
                if start_time:
                    query += " AND timestamp >= ?"
                    params.append(start_time.isoformat())
                
                if end_time:
                    query += " AND timestamp <= ?"
                    params.append(end_time.isoformat())
                
                if session_id:
                    query += " AND session_id = ?"
                    params.append(session_id)
                
                query += " ORDER BY timestamp DESC"
                
                if limit:
                    query += " LIMIT ?"
                    params.append(limit)
                
                cursor = conn.execute(query, params)
                columns = [description[0] for description in cursor.description]
                
                logs = []
                for row in cursor.fetchall():
                    log_dict = dict(zip(columns, row))
                    # Parse metadata JSON if present
                    if log_dict.get('metadata'):
                        try:
                            log_dict['metadata'] = json.loads(log_dict['metadata'])
                        except json.JSONDecodeError:
                            log_dict['metadata'] = None
                    logs.append(log_dict)
                
                return logs

        return self._execute_with_retry(_get_logs_operation)

    def clear_audit_logs(self, older_than_days: Optional[int] = None) -> int:
        """Clear audit logs with optional time-based filtering.

        Parameters
        ----------
        older_than_days : int, optional
            Only delete logs older than this many days

        Returns
        -------
        int
            Number of logs that were deleted
        """
        def _clear_operation():
            with sqlite3.connect(self.db_path, timeout=self.timeout) as conn:
                if older_than_days:
                    cutoff_time = datetime.now().timestamp() - (older_than_days * 24 * 3600)
                    cutoff_datetime = datetime.fromtimestamp(cutoff_time).isoformat()
                    cursor = conn.execute(
                        "DELETE FROM audit_logs WHERE timestamp < ?",
                        (cutoff_datetime,)
                    )
                else:
                    cursor = conn.execute("DELETE FROM audit_logs")
                
                conn.commit()
                return cursor.rowcount

        return self._execute_with_retry(_clear_operation)


# Convenience functions for direct use with audit logging
_default_audit_db = AuditLogger()


def save_variable(name: str, value: str) -> None:
    """Save a variable using the default audit logging database instance."""
    _default_audit_db.save_variable(name, value)


def get_variable(name: str) -> str:
    """Get a variable using the default audit logging database instance."""
    return _default_audit_db.get_variable(name)


def log_decision(
    decision: str,
    reasoning: str,
    affected_variables: Optional[List[str]] = None,
    confidence: Optional[float] = None,
    session_id: Optional[str] = None
) -> int:
    """Log a decision using the default audit logging database instance."""
    return _default_audit_db.log_decision(
        decision, reasoning, affected_variables, confidence, session_id
    )


def log_reasoning(
    context: str,
    reasoning: str,
    result: Optional[str] = None,
    session_id: Optional[str] = None
) -> int:
    """Log reasoning using the default audit logging database instance."""
    return _default_audit_db.log_reasoning(context, reasoning, result, session_id)