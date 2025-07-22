#!/usr/bin/env python3
"""
MongoDB Variables Management System

This module provides MongoDB-based variable storage for the natural language macro system,
replacing the traditional variables.json file approach with a more robust database solution.

Key Features:
- MongoDB's built-in atomicity and concurrency control
- variables.json compatible interface
- Automatic error handling and fallback mechanisms
- High performance with proper indexing
"""

from pymongo import MongoClient, errors
from pymongo.collection import Collection
from datetime import datetime
import logging
from typing import Optional, Dict, Any
import json
import os

# Configure logging
logger = logging.getLogger(__name__)


class MongoVariables:
    """
    MongoDB-based variable management system for natural language macros.
    
    This class provides a drop-in replacement for variables.json functionality
    while leveraging MongoDB's robust features for better scalability and reliability.
    """
    
    def __init__(self, connection_string: str = "mongodb://localhost:27017/", 
                 database_name: str = "macro_variables",
                 collection_name: str = "variables"):
        """
        Initialize MongoDB variables manager.
        
        Args:
            connection_string: MongoDB connection string
            database_name: Database name for storing variables
            collection_name: Collection name for variable documents
        """
        self.connection_string = connection_string
        self.database_name = database_name
        self.collection_name = collection_name
        self._client: Optional[MongoClient] = None
        self._collection: Optional[Collection] = None
        
        # Initialize connection and setup
        self._connect()
        self._setup_indexes()
    
    def _connect(self) -> bool:
        """
        Establish connection to MongoDB.
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            self._client = MongoClient(
                self.connection_string,
                serverSelectionTimeoutMS=5000,  # 5 second timeout
                connectTimeoutMS=5000,
                socketTimeoutMS=5000
            )
            
            # Test connection
            self._client.admin.command('ping')
            
            # Get database and collection
            db = self._client[self.database_name]
            self._collection = db[self.collection_name]
            
            logger.info(f"Successfully connected to MongoDB: {self.database_name}.{self.collection_name}")
            return True
            
        except errors.ServerSelectionTimeoutError as e:
            logger.error(f"MongoDB connection timeout: {e}")
            return False
        except Exception as e:
            logger.error(f"Failed to connect to MongoDB: {e}")
            return False
    
    def _setup_indexes(self) -> None:
        """
        Setup necessary indexes for optimal performance.
        """
        if self._collection is None:
            return
            
        try:
            # Create unique index on variable name for fast lookups and uniqueness
            self._collection.create_index("name", unique=True)
            logger.debug("Created unique index on 'name' field")
            
        except Exception as e:
            logger.warning(f"Failed to create indexes: {e}")
    
    def get_variable(self, name: str) -> str:
        """
        Retrieve a variable value by name.
        
        Args:
            name: Variable name
            
        Returns:
            str: Variable value, or empty string if not found
        """
        if self._collection is None:
            logger.error("MongoDB collection not available")
            return ""
        
        try:
            # Find the variable document
            doc = self._collection.find_one({"name": name})
            
            if doc:
                value = doc.get("value", "")
                logger.debug(f"Retrieved variable '{name}': {value}")
                return value
            else:
                logger.debug(f"Variable '{name}' not found")
                return ""
                
        except Exception as e:
            logger.error(f"Failed to retrieve variable '{name}': {e}")
            return ""
    
    def set_variable(self, name: str, value: str) -> bool:
        """
        Set a variable value, creating or updating as needed.
        
        Args:
            name: Variable name
            value: Variable value (will be converted to string)
            
        Returns:
            bool: True if operation successful, False otherwise
        """
        if self._collection is None:
            logger.error("MongoDB collection not available")
            return False
        
        # Convert value to string to maintain compatibility with variables.json
        str_value = str(value)
        
        try:
            # Use upsert for atomic create-or-update operation
            current_time = datetime.utcnow()
            
            result = self._collection.find_one_and_update(
                {"name": name},
                {
                    "$set": {
                        "value": str_value,
                        "updated_at": current_time
                    },
                    "$setOnInsert": {
                        "created_at": current_time
                    }
                },
                upsert=True,
                return_document=True
            )
            
            if result:
                logger.info(f"Set variable '{name}' = '{str_value}'")
                return True
            else:
                logger.error(f"Failed to set variable '{name}'")
                return False
                
        except Exception as e:
            logger.error(f"Failed to set variable '{name}': {e}")
            return False
    
    def delete_variable(self, name: str) -> bool:
        """
        Delete a variable.
        
        Args:
            name: Variable name
            
        Returns:
            bool: True if deleted or didn't exist, False on error
        """
        if self._collection is None:
            logger.error("MongoDB collection not available")
            return False
        
        try:
            result = self._collection.delete_one({"name": name})
            
            if result.deleted_count > 0:
                logger.info(f"Deleted variable '{name}'")
            else:
                logger.debug(f"Variable '{name}' not found for deletion")
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to delete variable '{name}': {e}")
            return False
    
    def list_variables(self) -> Dict[str, str]:
        """
        List all variables as a dictionary (variables.json compatible format).
        
        Returns:
            dict: Dictionary of variable name -> value pairs
        """
        if self._collection is None:
            logger.error("MongoDB collection not available")
            return {}
        
        try:
            variables = {}
            
            # Retrieve all variable documents
            cursor = self._collection.find({}, {"name": 1, "value": 1, "_id": 0})
            
            for doc in cursor:
                name = doc.get("name", "")
                value = doc.get("value", "")
                if name:  # Only include valid names
                    variables[name] = value
            
            logger.debug(f"Listed {len(variables)} variables")
            return variables
            
        except Exception as e:
            logger.error(f"Failed to list variables: {e}")
            return {}
    
    def variable_exists(self, name: str) -> bool:
        """
        Check if a variable exists.
        
        Args:
            name: Variable name
            
        Returns:
            bool: True if variable exists, False otherwise
        """
        if self._collection is None:
            return False
        
        try:
            count = self._collection.count_documents({"name": name}, limit=1)
            return count > 0
            
        except Exception as e:
            logger.error(f"Failed to check variable existence '{name}': {e}")
            return False
    
    def get_variable_info(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Get detailed information about a variable.
        
        Args:
            name: Variable name
            
        Returns:
            dict: Variable information including timestamps, or None if not found
        """
        if self._collection is None:
            return None
        
        try:
            doc = self._collection.find_one({"name": name})
            
            if doc:
                # Remove MongoDB internal _id field
                doc.pop("_id", None)
                return doc
            else:
                return None
                
        except Exception as e:
            logger.error(f"Failed to get variable info '{name}': {e}")
            return None
    
    def migrate_from_json(self, json_file_path: str = "variables.json") -> bool:
        """
        Migrate variables from a JSON file to MongoDB.
        
        Args:
            json_file_path: Path to the variables.json file
            
        Returns:
            bool: True if migration successful, False otherwise
        """
        if not os.path.exists(json_file_path):
            logger.info(f"JSON file {json_file_path} not found, no migration needed")
            return True
        
        try:
            with open(json_file_path, 'r', encoding='utf-8') as f:
                variables = json.load(f)
            
            if not isinstance(variables, dict):
                logger.error(f"Invalid JSON format in {json_file_path}")
                return False
            
            # Migrate each variable
            migrated_count = 0
            for name, value in variables.items():
                if self.set_variable(name, str(value)):
                    migrated_count += 1
            
            logger.info(f"Migrated {migrated_count} variables from {json_file_path}")
            return True
            
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON file {json_file_path}: {e}")
            return False
        except Exception as e:
            logger.error(f"Failed to migrate from {json_file_path}: {e}")
            return False
    
    def export_to_json(self, json_file_path: str = "variables_export.json") -> bool:
        """
        Export all variables to a JSON file (variables.json format).
        
        Args:
            json_file_path: Output file path
            
        Returns:
            bool: True if export successful, False otherwise
        """
        try:
            variables = self.list_variables()
            
            with open(json_file_path, 'w', encoding='utf-8') as f:
                json.dump(variables, f, ensure_ascii=False, indent=2)
            
            logger.info(f"Exported {len(variables)} variables to {json_file_path}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to export variables to {json_file_path}: {e}")
            return False
    
    def clear_all_variables(self) -> int:
        """
        Clear all variables from the database.
        
        Returns:
            int: Number of variables deleted, or -1 on error
        """
        if self._collection is None:
            logger.error("MongoDB collection not available")
            return -1
        
        try:
            result = self._collection.delete_many({})
            deleted_count = result.deleted_count
            
            logger.info(f"Cleared {deleted_count} variables from database")
            return deleted_count
            
        except Exception as e:
            logger.error(f"Failed to clear all variables: {e}")
            return -1
    
    def close(self) -> None:
        """
        Close MongoDB connection.
        """
        if self._client:
            self._client.close()
            logger.info("MongoDB connection closed")


# Global instance for easy access
_mongo_variables: Optional[MongoVariables] = None


def get_mongo_variables() -> MongoVariables:
    """
    Get or create global MongoVariables instance.
    
    Returns:
        MongoVariables: Global instance
    """
    global _mongo_variables
    
    if _mongo_variables is None:
        _mongo_variables = MongoVariables()
    
    return _mongo_variables


# Convenience functions for easy integration with CLAUDE.md
def get_variable(name: str) -> str:
    """
    Convenience function to get a variable value.
    
    Args:
        name: Variable name
        
    Returns:
        str: Variable value or empty string if not found
    """
    return get_mongo_variables().get_variable(name)


def set_variable(name: str, value: str) -> bool:
    """
    Convenience function to set a variable value.
    
    Args:
        name: Variable name
        value: Variable value
        
    Returns:
        bool: True if successful, False otherwise
    """
    return get_mongo_variables().set_variable(name, value)


def list_variables() -> Dict[str, str]:
    """
    Convenience function to list all variables.
    
    Returns:
        dict: Dictionary of all variables
    """
    return get_mongo_variables().list_variables()


def delete_variable(name: str) -> bool:
    """
    Convenience function to delete a variable.
    
    Args:
        name: Variable name
        
    Returns:
        bool: True if successful, False otherwise
    """
    return get_mongo_variables().delete_variable(name)


def clear_all_variables() -> int:
    """
    Convenience function to clear all variables.
    
    Returns:
        int: Number of variables deleted, or -1 on error
    """
    return get_mongo_variables().clear_all_variables()