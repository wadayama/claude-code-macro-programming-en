"""Simple Chroma-based RAG system for natural language macro programming.

This module provides basic vector database functionality using ChromaDB
for knowledge retrieval and experience learning in natural language macros.
Designed to integrate with the existing variable_db.py system.
"""

import chromadb
from chromadb.config import Settings
from typing import List, Dict, Optional
from pathlib import Path
import uuid
import time


class SimpleChromaRAG:
    """Simple RAG system using ChromaDB for natural language macro integration."""
    
    def __init__(self, persist_directory: str = "./chroma_db"):
        """Initialize the Chroma RAG system.
        
        Parameters
        ----------
        persist_directory : str
            Directory to persist the Chroma database
        """
        self.persist_directory = Path(persist_directory)
        self.persist_directory.mkdir(exist_ok=True)
        
        # Initialize Chroma client with persistence
        self.client = chromadb.PersistentClient(
            path=str(self.persist_directory)
        )
        
        # Create collections for different types of knowledge
        self.knowledge_collection = self.client.get_or_create_collection(
            name="knowledge_base",
            metadata={"description": "General knowledge documents"}
        )
        
        self.experience_collection = self.client.get_or_create_collection(
            name="experience_base", 
            metadata={"description": "Task execution experiences"}
        )
    
    def add_knowledge(self, text: str, source: str = "unknown", metadata: Optional[Dict] = None) -> str:
        """Add knowledge to the knowledge base.
        
        Parameters
        ----------
        text : str
            Knowledge text to store
        source : str
            Source of the knowledge
        metadata : dict, optional
            Additional metadata
            
        Returns
        -------
        str
            ID of the stored knowledge
        """
        doc_id = str(uuid.uuid4())
        doc_metadata = {
            "source": source,
            "timestamp": time.time(),
            **(metadata or {})
        }
        
        self.knowledge_collection.add(
            documents=[text],
            metadatas=[doc_metadata],
            ids=[doc_id]
        )
        
        return doc_id
    
    def search_knowledge(self, query: str, n_results: int = 3) -> List[Dict]:
        """Search for relevant knowledge.
        
        Parameters
        ----------
        query : str
            Search query
        n_results : int
            Number of results to return
            
        Returns
        -------
        List[Dict]
            Search results with documents and metadata
        """
        results = self.knowledge_collection.query(
            query_texts=[query],
            n_results=n_results
        )
        
        # Format results
        formatted_results = []
        for i in range(len(results['documents'][0])):
            formatted_results.append({
                'document': results['documents'][0][i],
                'metadata': results['metadatas'][0][i],
                'distance': results['distances'][0][i] if 'distances' in results else None
            })
        
        return formatted_results
    
    def add_experience(self, task: str, result: str, success: bool = True, metadata: Optional[Dict] = None) -> str:
        """Add task execution experience.
        
        Parameters
        ----------
        task : str
            Task description
        result : str
            Task execution result/outcome
        success : bool
            Whether the task was successful
        metadata : dict, optional
            Additional metadata
            
        Returns
        -------
        str
            ID of the stored experience
        """
        doc_id = str(uuid.uuid4())
        experience_text = f"Task: {task}\nResult: {result}"
        
        doc_metadata = {
            "task_type": "general",
            "success": success,
            "timestamp": time.time(),
            **(metadata or {})
        }
        
        self.experience_collection.add(
            documents=[experience_text],
            metadatas=[doc_metadata], 
            ids=[doc_id]
        )
        
        return doc_id
    
    def search_similar_experience(self, task: str, success_only: bool = True, n_results: int = 3) -> List[Dict]:
        """Search for similar task experiences.
        
        Parameters
        ----------
        task : str
            Current task description
        success_only : bool
            Only return successful experiences
        n_results : int
            Number of results to return
            
        Returns
        -------
        List[Dict]
            Similar experiences with metadata
        """
        # Build where clause for filtering
        where_clause = {}
        if success_only:
            where_clause["success"] = True
        
        results = self.experience_collection.query(
            query_texts=[task],
            n_results=n_results,
            where=where_clause if where_clause else None
        )
        
        # Format results
        formatted_results = []
        for i in range(len(results['documents'][0])):
            formatted_results.append({
                'experience': results['documents'][0][i],
                'metadata': results['metadatas'][0][i],
                'distance': results['distances'][0][i] if 'distances' in results else None
            })
        
        return formatted_results
    
    def get_stats(self) -> Dict:
        """Get database statistics.
        
        Returns
        -------
        Dict
            Database statistics
        """
        return {
            "knowledge_count": self.knowledge_collection.count(),
            "experience_count": self.experience_collection.count(),
            "persist_directory": str(self.persist_directory)
        }


# Convenience functions for natural language macro integration
_default_rag = SimpleChromaRAG()


def search_knowledge_base(query: str, max_results: int = 3) -> str:
    """Search knowledge base and return formatted results.
    
    This function is designed for natural language macro integration.
    Usage: "Search for information related to {{topic}} from the knowledge base"
    """
    results = _default_rag.search_knowledge(query, max_results)
    
    if not results:
        return f"No relevant knowledge found for: {query}"
    
    formatted_output = f"Knowledge search results for '{query}':\n\n"
    for i, result in enumerate(results, 1):
        formatted_output += f"{i}. {result['document']}\n"
        if result['metadata'].get('source'):
            formatted_output += f"   Source: {result['metadata']['source']}\n"
        formatted_output += "\n"
    
    return formatted_output


def save_experience(task: str, outcome: str, success: bool = True) -> str:
    """Save task execution experience.
    
    This function is designed for natural language macro integration.
    Usage: After task completion, save the experience for future reference.
    """
    exp_id = _default_rag.add_experience(task, outcome, success)
    return f"Experience saved with ID: {exp_id}"


def find_similar_experience(current_task: str, max_results: int = 3) -> str:
    """Find similar past experiences.
    
    This function is designed for natural language macro integration.
    Usage: "Search for past successful examples similar to {{current_task}}"
    """
    results = _default_rag.search_similar_experience(current_task, True, max_results)
    
    if not results:
        return f"No similar successful experiences found for: {current_task}"
    
    formatted_output = f"Similar successful experiences for '{current_task}':\n\n"
    for i, result in enumerate(results, 1):
        formatted_output += f"{i}. {result['experience']}\n\n"
    
    return formatted_output


def add_knowledge_from_text(text: str, source: str = "manual_input") -> str:
    """Add knowledge from text input.
    
    This function is designed for natural language macro integration.
    Usage: "Save the content of this document to the knowledge base"
    """
    doc_id = _default_rag.add_knowledge(text, source)
    return f"Knowledge added to database with ID: {doc_id}"