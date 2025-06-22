# Presentation Structure Advisor

**Pattern 7 Practical Example**: Automatic presentation structure generation responding to individual requirements using knowledge base

## Overview

System that databases professional knowledge of presentation design and automatically generates optimal presentation structures based on user's individual requirements (audience, time, purpose).

**Main Value**: 
- Utilizing veteran presenter's "tacit knowledge" as "explicit knowledge"
- Beginners can acquire professional-level structures in short time
- Automatic adaptation to individual requirements

## Usage

1. **Knowledge Loading**: Load presentation design framework
2. **Requirement Input**: Specify theme, audience, time, purpose
3. **Structure Generation**: Select and apply optimal patterns from knowledge base
4. **Output Verification**: Acquire specific presentation structure proposals

---

## Step 1: Knowledge Base Loading

Display "=== Presentation Design Knowledge Loading ===".

Load presentation_framework.md and set to {{presentation_knowledge}}.

Display "Presentation design framework loaded".

Verify the following main elements from {{presentation_knowledge}}:
- Types of audience-specific approaches
- Types of structure patterns
- Time-based structure guides
- Slide design principles

---

## Step 2: Requirement Collection

Display "=== Presentation Requirements Confirmation ===".

Please answer the following questions:

**Question 1**: What is the theme of your presentation?
(Examples: New product proposal, project report, technical explanation, etc.)

Set your answer to {{presentation_theme}}.

**Question 2**: What type is your audience?
A) Executives/Decision makers
B) Technical experts
C) General employees
D) External customers
E) Mixed audience

Set your answer to {{audience_type}}.

**Question 3**: How much time do you have for the presentation?
A) 5 minutes (lightning talk)
B) 15 minutes (brief presentation)
C) 30 minutes (standard presentation)
D) 60 minutes (detailed presentation)

Set your answer to {{presentation_time}}.

**Question 4**: What is the main purpose?
A) Persuasion (seeking approval/decision)
B) Information sharing (reporting/explaining)
C) Education (training/teaching)
D) Inspiration (motivation/vision sharing)

Set your answer to {{presentation_purpose}}.

Display "Requirement collection completed".

---

## Step 3: Knowledge Base Analysis and Pattern Selection

Display "=== Knowledge Base Analysis ===".

Based on {{presentation_knowledge}}, analyze the optimal approach for the combination of {{audience_type}}, {{presentation_time}}, and {{presentation_purpose}}.

From the presentation framework, extract:

### Audience-Specific Approach
Based on {{audience_type}}, determine:
- Appropriate level of detail
- Preferred communication style
- Key persuasion factors
- Optimal visual design approach

### Time-Based Structure Pattern
Based on {{presentation_time}}, select:
- Number of main sections
- Time allocation per section
- Appropriate depth of content
- Recommended slide count

### Purpose-Driven Content Strategy
Based on {{presentation_purpose}}, determine:
- Opening strategy
- Main message delivery method
- Evidence and support materials
- Closing and call-to-action approach

Save the analysis results to {{strategy_analysis}}.

---

## Step 4: Customized Structure Generation

Display "=== Customized Presentation Structure Generation ===".

Using {{strategy_analysis}} and {{presentation_knowledge}}, generate a specific presentation structure for {{presentation_theme}}.

Create the following comprehensive structure:

### 1. Overall Structure Framework
- Opening section (duration and key elements)
- Main body sections (number, topics, duration)
- Closing section (duration and key elements)

### 2. Detailed Section Breakdown
For each section, specify:
- Main message/objective
- Key content points
- Recommended slides
- Timing and transitions

### 3. Slide-by-Slide Outline
Provide concrete slide titles and main content for:
- Title slide
- Agenda/overview slide
- Main content slides
- Summary/conclusion slide
- Q&A preparation

### 4. Delivery Recommendations
Based on audience type and purpose:
- Speaking style suggestions
- Visual aid recommendations
- Interaction strategies
- Potential questions preparation

Save the complete structure to {{final_structure}}.

---

## Step 5: Output and Validation

Display "=== Generated Presentation Structure ===".

Present {{final_structure}} in a clear, actionable format.

### Quality Validation
Verify the generated structure against knowledge base criteria:
- **Audience Appropriateness**: Does it match {{audience_type}} preferences?
- **Time Feasibility**: Can it be delivered within {{presentation_time}}?
- **Purpose Alignment**: Does it effectively serve {{presentation_purpose}}?
- **Theme Coverage**: Does it comprehensively address {{presentation_theme}}?

### Customization Notes
Highlight specific adaptations made for this presentation:
- Unique elements for this audience type
- Time-specific optimizations
- Purpose-driven content choices
- Theme-specific recommendations

---

## Step 6: Additional Resources and Examples

Based on the generated structure, provide:

### Sample Content Examples
- Opening statement examples
- Transition phrase suggestions
- Closing statement options

### Visual Design Recommendations
- Slide layout suggestions
- Color scheme recommendations
- Font and typography guidelines

### Backup Strategies
- Content to cut if time runs short
- Additional content if time allows
- Alternative explanations for technical concepts

Display "Presentation structure generation completed with knowledge base guidance".

---

## Learning Points

### Pattern 7 Implementation
1. **Knowledge Base Loading**: Static professional knowledge from external file
2. **Requirement Analysis**: Dynamic adaptation to user-specific needs
3. **Pattern Matching**: Selection of optimal approaches from knowledge repository
4. **Customized Generation**: Application of knowledge patterns to specific cases

### Knowledge Base Value
- **Expertise Democratization**: Professional knowledge accessible to beginners
- **Consistency**: Reliable quality across different users and situations
- **Efficiency**: Rapid generation of high-quality structures
- **Scalability**: Knowledge base can be expanded and refined over time

### Integration Benefits
- **Sequential Pipeline**: Systematic progression from requirements to final output
- **Conditional Execution**: Different strategies based on audience and purpose types
- **Modular Design**: Reusable knowledge components for various presentation scenarios

---

**Knowledge Base Pattern Characteristics**:
1. **Static Knowledge Repository**: Curated professional expertise stored in accessible format
2. **Dynamic Application**: Knowledge adapted to specific requirements and contexts
3. **Pattern Recognition**: System identifies optimal approaches from knowledge patterns
4. **Quality Assurance**: Professional-grade outputs even from non-expert users
5. **Scalable Expertise**: Knowledge base grows and improves over time

This example demonstrates how Pattern 7 enables democratization of professional expertise through structured knowledge bases that can be dynamically applied to individual requirements, producing consistently high-quality, customized solutions.