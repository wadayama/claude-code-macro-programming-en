#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
English Haiku Data Analysis Tool
Reads haiku data from variables.json, performs detailed analysis, and saves results
Python Tool Integration experimental tool for English version
"""

import json
import re
from collections import Counter
from pathlib import Path

def count_syllables(word):
    """Count syllables in an English word using vowel group approach"""
    word = word.lower().strip()
    if not word:
        return 0
    
    # Remove non-alphabetic characters
    word = re.sub(r'[^a-z]', '', word)
    if not word:
        return 0
    
    vowels = "aeiouy"
    syllable_count = 0
    previous_was_vowel = False
    
    for i, char in enumerate(word):
        is_vowel = char in vowels
        if is_vowel and not previous_was_vowel:
            syllable_count += 1
        previous_was_vowel = is_vowel
    
    # Handle silent 'e' at the end
    if word.endswith('e') and syllable_count > 1:
        syllable_count -= 1
    
    # Ensure at least 1 syllable per word
    return max(1, syllable_count)

def analyze_haiku_structure(haiku):
    """Analyze haiku structure for English 5-7-5 syllable pattern"""
    lines = haiku.strip().split('\n')
    if len(lines) >= 3:
        line1_syllables = sum(count_syllables(word) for word in lines[0].split())
        line2_syllables = sum(count_syllables(word) for word in lines[1].split())
        line3_syllables = sum(count_syllables(word) for word in lines[2].split())
        
        total_syllables = line1_syllables + line2_syllables + line3_syllables
        structure_score = abs(5 - line1_syllables) + abs(7 - line2_syllables) + abs(5 - line3_syllables)
        
        return {
            "total_lines": len(lines),
            "line1_syllables": line1_syllables,
            "line2_syllables": line2_syllables,
            "line3_syllables": line3_syllables,
            "total_syllables": total_syllables,
            "structure_score": structure_score,
            "is_traditional_pattern": structure_score <= 2
        }
    else:
        # Single line or non-standard format
        all_words = ' '.join(lines).split()
        total_syllables = sum(count_syllables(word) for word in all_words)
        return {
            "total_lines": len(lines),
            "total_syllables": total_syllables,
            "structure_score": 100,  # Poor structure
            "is_traditional_pattern": False
        }

def analyze_vocabulary(text):
    """Analyze vocabulary characteristics"""
    # Extract words (remove punctuation)
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    
    # Categorize vocabulary
    nature_words = ['wind', 'star', 'moon', 'flower', 'cloud', 'rain', 'snow', 'sky', 'sea', 'mountain', 
                   'sun', 'tree', 'leaf', 'bird', 'water', 'earth', 'light', 'shadow', 'dawn', 'dusk']
    emotion_words = ['dream', 'love', 'sad', 'joy', 'anger', 'peace', 'hope', 'fear', 'wonder', 'sorrow',
                    'bliss', 'tears', 'smile', 'heart', 'soul', 'spirit', 'memory', 'longing']
    tech_words = ['circuit', 'digital', 'data', 'code', 'machine', 'robot', 'electric', 'computer',
                 'screen', 'signal', 'wire', 'system', 'network', 'virtual', 'pixel']
    
    nature_count = sum(1 for word in words if word in nature_words)
    emotion_count = sum(1 for word in words if word in emotion_words)
    tech_count = sum(1 for word in words if word in tech_words)
    
    return {
        "total_words": len(words),
        "unique_words": len(set(words)),
        "word_list": words,
        "nature_words": nature_count,
        "emotion_words": emotion_count,
        "tech_words": tech_count,
        "vocabulary_diversity": len(set(words)) / len(words) if words else 0
    }

def analyze_creativity(haiku):
    """Analyze creativity and poetic techniques"""
    text = haiku.lower()
    
    # Detect creative techniques
    creativity_indicators = {
        "personification": ["whispers", "dances", "sings", "weeps", "laughs", "dreams", "sleeps"],
        "metaphor": ["becomes", "turns into", "transforms", "melts into", "flows like"],
        "sensory_imagery": ["glows", "shimmers", "echoes", "fragrance", "taste", "touch", "sound"],
        "abstract_concepts": ["time", "space", "infinity", "eternity", "existence", "essence", "spirit"],
        "alliteration": []  # Will be detected separately
    }
    
    detected_techniques = {}
    for technique, patterns in creativity_indicators.items():
        if technique != "alliteration":
            count = sum(1 for pattern in patterns if pattern in text)
            if count > 0:
                detected_techniques[technique] = count
    
    # Detect alliteration (simplified)
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    alliteration_count = 0
    for i in range(len(words) - 1):
        if words[i][0] == words[i+1][0]:
            alliteration_count += 1
    
    if alliteration_count > 0:
        detected_techniques["alliteration"] = alliteration_count
    
    # Check for comparative language
    has_simile = any(phrase in text for phrase in ["like", "as if", "seems", "appears"])
    
    return {
        "creativity_score": len(detected_techniques),
        "detected_techniques": detected_techniques,
        "has_simile": has_simile,
        "alliteration_instances": alliteration_count
    }

def main():
    """Main processing function"""
    try:
        # Read variables.json
        variables_path = Path("variables.json")
        if not variables_path.exists():
            result = {
                "error": "variables.json not found",
                "status": "failed"
            }
        else:
            with open(variables_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Extract haiku data
            haikus = {}
            for i in range(1, 5):
                key = f"haiku_{i}"
                if key in data:
                    haikus[key] = data[key]
            
            themes = data.get("themes", "")
            best_selection = data.get("best_selection", "")
            
            # Analyze each haiku
            haiku_analyses = {}
            for key, haiku in haikus.items():
                analysis = {
                    "text": haiku,
                    "structure": analyze_haiku_structure(haiku),
                    "vocabulary": analyze_vocabulary(haiku),
                    "creativity": analyze_creativity(haiku)
                }
                haiku_analyses[key] = analysis
            
            # Calculate overall statistics
            total_syllables = sum(h["structure"]["total_syllables"] for h in haiku_analyses.values())
            avg_creativity = sum(h["creativity"]["creativity_score"] for h in haiku_analyses.values()) / len(haiku_analyses) if haiku_analyses else 0
            traditional_count = sum(1 for h in haiku_analyses.values() if h["structure"].get("is_traditional_pattern", False))
            
            # Create analysis result
            result = {
                "analysis_timestamp": "2025-06-30",
                "total_haikus_analyzed": len(haiku_analyses),
                "themes_analyzed": themes,
                "individual_analyses": haiku_analyses,
                "overall_statistics": {
                    "total_syllable_count": total_syllables,
                    "average_creativity_score": round(avg_creativity, 2),
                    "traditional_pattern_count": traditional_count,
                    "most_creative_haiku": max(haiku_analyses.keys(), key=lambda k: haiku_analyses[k]["creativity"]["creativity_score"]) if haiku_analyses else None,
                    "best_structure_haiku": min(haiku_analyses.keys(), key=lambda k: haiku_analyses[k]["structure"]["structure_score"]) if haiku_analyses else None
                },
                "recommendations": {
                    "strengths": [],
                    "areas_for_improvement": []
                },
                "status": "completed"
            }
            
            # Generate recommendations
            if avg_creativity > 2:
                result["recommendations"]["strengths"].append("Excellent use of creative techniques and poetic devices")
            
            if traditional_count == len(haiku_analyses):
                result["recommendations"]["strengths"].append("Perfect adherence to traditional 5-7-5 syllable structure")
            elif traditional_count < len(haiku_analyses) / 2:
                result["recommendations"]["areas_for_improvement"].append("Consider refining syllable structure for traditional haiku format")
            
            vocab_diversity_avg = sum(h["vocabulary"]["vocabulary_diversity"] for h in haiku_analyses.values()) / len(haiku_analyses) if haiku_analyses else 0
            if vocab_diversity_avg > 0.9:
                result["recommendations"]["strengths"].append("Excellent vocabulary diversity and word choice")
        
        # Write results back to variables.json
        data["analysis_report"] = result
        
        with open(variables_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print("Haiku analysis completed. Results saved to analysis_report in variables.json.")
        print(f"Analyzed: {result['total_haikus_analyzed']} haiku(s)")
        print(f"Average creativity score: {result['overall_statistics']['average_creativity_score']}")
        
    except Exception as e:
        error_result = {
            "error": str(e),
            "status": "failed",
            "analysis_timestamp": "2025-06-30"
        }
        
        # Record error information in variables.json
        try:
            with open("variables.json", 'r', encoding='utf-8') as f:
                data = json.load(f)
            data["analysis_report"] = error_result
            with open("variables.json", 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except:
            pass
        
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()