#!/usr/bin/env python3
"""
Configuration management for MongoDB Variables System

This module provides centralized configuration management for the MongoDB-based
variable storage system, allowing easy customization of connection parameters
and system behavior.
"""

import os
import yaml
from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)


class MongoConfig:
    """
    Configuration manager for MongoDB variables system.
    
    Supports configuration from:
    1. Environment variables
    2. YAML configuration files
    3. Default values
    """
    
    # Default configuration values
    DEFAULT_CONFIG = {
        'mongodb': {
            'connection_string': 'mongodb://localhost:27017/',
            'database_name': 'macro_variables',
            'collection_name': 'variables',
            'connection_timeout_ms': 5000,
            'socket_timeout_ms': 5000,
            'server_selection_timeout_ms': 5000,
        },
        'logging': {
            'level': 'INFO',
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'features': {
            'auto_migrate_from_json': True,
            'backup_on_migration': True,
            'create_indexes': True,
        }
    }
    
    def __init__(self, config_file: Optional[str] = None):
        """
        Initialize configuration.
        
        Args:
            config_file: Path to YAML configuration file (optional)
        """
        self.config = self.DEFAULT_CONFIG.copy()
        
        # Load from file if specified
        if config_file:
            self.load_from_file(config_file)
        
        # Override with environment variables
        self.load_from_env()
    
    def load_from_file(self, config_file: str) -> bool:
        """
        Load configuration from YAML file.
        
        Args:
            config_file: Path to YAML configuration file
            
        Returns:
            bool: True if loaded successfully, False otherwise
        """
        try:
            if not os.path.exists(config_file):
                logger.warning(f"Configuration file {config_file} not found")
                return False
            
            with open(config_file, 'r', encoding='utf-8') as f:
                file_config = yaml.safe_load(f)
            
            if file_config:
                # Deep merge with default config
                self._deep_merge(self.config, file_config)
                logger.info(f"Loaded configuration from {config_file}")
                return True
            
        except yaml.YAMLError as e:
            logger.error(f"Failed to parse YAML config file {config_file}: {e}")
        except Exception as e:
            logger.error(f"Failed to load config file {config_file}: {e}")
        
        return False
    
    def load_from_env(self) -> None:
        """
        Load configuration from environment variables.
        
        Environment variable format:
        MONGO_VARIABLES_<SECTION>_<KEY> = value
        
        Examples:
        MONGO_VARIABLES_MONGODB_CONNECTION_STRING = mongodb://user:pass@host:port/
        MONGO_VARIABLES_MONGODB_DATABASE_NAME = my_variables
        """
        env_prefix = 'MONGO_VARIABLES_'
        
        for key, value in os.environ.items():
            if not key.startswith(env_prefix):
                continue
            
            # Parse environment variable name
            config_key = key[len(env_prefix):].lower()
            parts = config_key.split('_')
            
            if len(parts) >= 2:
                section = parts[0]
                setting = '_'.join(parts[1:])
                
                # Convert value to appropriate type
                converted_value = self._convert_env_value(value)
                
                # Set in config
                if section in self.config:
                    self.config[section][setting] = converted_value
                    logger.debug(f"Set config from env: {section}.{setting} = {converted_value}")
    
    def _convert_env_value(self, value: str) -> Any:
        """
        Convert environment variable string to appropriate Python type.
        
        Args:
            value: String value from environment variable
            
        Returns:
            Converted value (bool, int, or str)
        """
        # Boolean conversion
        if value.lower() in ('true', 'yes', '1', 'on'):
            return True
        elif value.lower() in ('false', 'no', '0', 'off'):
            return False
        
        # Integer conversion
        try:
            return int(value)
        except ValueError:
            pass
        
        # Return as string
        return value
    
    def _deep_merge(self, target: Dict[str, Any], source: Dict[str, Any]) -> None:
        """
        Deep merge source dictionary into target dictionary.
        
        Args:
            target: Target dictionary to merge into
            source: Source dictionary to merge from
        """
        for key, value in source.items():
            if key in target and isinstance(target[key], dict) and isinstance(value, dict):
                self._deep_merge(target[key], value)
            else:
                target[key] = value
    
    def get(self, section: str, key: str, default: Any = None) -> Any:
        """
        Get a configuration value.
        
        Args:
            section: Configuration section name
            key: Configuration key name
            default: Default value if not found
            
        Returns:
            Configuration value or default
        """
        return self.config.get(section, {}).get(key, default)
    
    def get_mongodb_config(self) -> Dict[str, Any]:
        """
        Get MongoDB-specific configuration.
        
        Returns:
            dict: MongoDB configuration section
        """
        return self.config.get('mongodb', {})
    
    def get_connection_string(self) -> str:
        """
        Get MongoDB connection string.
        
        Returns:
            str: MongoDB connection string
        """
        return self.get('mongodb', 'connection_string', 'mongodb://localhost:27017/')
    
    def get_database_name(self) -> str:
        """
        Get database name.
        
        Returns:
            str: Database name
        """
        return self.get('mongodb', 'database_name', 'macro_variables')
    
    def get_collection_name(self) -> str:
        """
        Get collection name.
        
        Returns:
            str: Collection name
        """
        return self.get('mongodb', 'collection_name', 'variables')
    
    def is_auto_migrate_enabled(self) -> bool:
        """
        Check if automatic migration from variables.json is enabled.
        
        Returns:
            bool: True if auto migration is enabled
        """
        return self.get('features', 'auto_migrate_from_json', True)
    
    def is_backup_on_migration_enabled(self) -> bool:
        """
        Check if backup during migration is enabled.
        
        Returns:
            bool: True if backup on migration is enabled
        """
        return self.get('features', 'backup_on_migration', True)
    
    def should_create_indexes(self) -> bool:
        """
        Check if index creation is enabled.
        
        Returns:
            bool: True if indexes should be created
        """
        return self.get('features', 'create_indexes', True)
    
    def setup_logging(self) -> None:
        """
        Setup logging based on configuration.
        """
        log_level = self.get('logging', 'level', 'INFO')
        log_format = self.get('logging', 'format', 
                             '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        # Configure root logger
        logging.basicConfig(
            level=getattr(logging, log_level.upper(), logging.INFO),
            format=log_format,
            force=True
        )
        
        logger.info(f"Logging configured with level: {log_level}")
    
    def validate(self) -> bool:
        """
        Validate configuration values.
        
        Returns:
            bool: True if configuration is valid, False otherwise
        """
        errors = []
        
        # Validate MongoDB connection string
        connection_string = self.get_connection_string()
        if not connection_string.startswith(('mongodb://', 'mongodb+srv://')):
            errors.append(f"Invalid MongoDB connection string: {connection_string}")
        
        # Validate database and collection names
        db_name = self.get_database_name()
        if not db_name or not isinstance(db_name, str):
            errors.append(f"Invalid database name: {db_name}")
        
        collection_name = self.get_collection_name()
        if not collection_name or not isinstance(collection_name, str):
            errors.append(f"Invalid collection name: {collection_name}")
        
        # Validate timeout values
        for timeout_key in ['connection_timeout_ms', 'socket_timeout_ms', 'server_selection_timeout_ms']:
            timeout_value = self.get('mongodb', timeout_key, 5000)
            if not isinstance(timeout_value, int) or timeout_value <= 0:
                errors.append(f"Invalid timeout value for {timeout_key}: {timeout_value}")
        
        if errors:
            logger.error("Configuration validation failed:")
            for error in errors:
                logger.error(f"  - {error}")
            return False
        
        logger.info("Configuration validation passed")
        return True
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Get configuration as dictionary.
        
        Returns:
            dict: Complete configuration
        """
        return self.config.copy()


# Global configuration instance
_config: Optional[MongoConfig] = None


def get_config(config_file: Optional[str] = None) -> MongoConfig:
    """
    Get or create global configuration instance.
    
    Args:
        config_file: Path to configuration file (optional)
        
    Returns:
        MongoConfig: Global configuration instance
    """
    global _config
    
    if _config is None:
        _config = MongoConfig(config_file)
        _config.setup_logging()
        
        if not _config.validate():
            logger.warning("Configuration validation failed, using defaults")
    
    return _config


def create_default_config_file(output_file: str = "config/mongodb.yaml") -> bool:
    """
    Create a default configuration file.
    
    Args:
        output_file: Output file path
        
    Returns:
        bool: True if created successfully, False otherwise
    """
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Write default configuration
        with open(output_file, 'w', encoding='utf-8') as f:
            yaml.dump(MongoConfig.DEFAULT_CONFIG, f, default_flow_style=False, indent=2)
        
        logger.info(f"Created default configuration file: {output_file}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to create configuration file {output_file}: {e}")
        return False