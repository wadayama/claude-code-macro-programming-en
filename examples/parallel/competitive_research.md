# Competitive Research System (Parallel Processing - Intermediate)

## Research Target Setting
Save the following 5 companies as major players in the "Cloud Services Market" to {{target_companies}}, and save {{target_companies}} to target_companies.json for persistence:
- Amazon AWS
- Microsoft Azure  
- Google Cloud Platform
- IBM Cloud
- Oracle Cloud

## Parallel Company Analysis
**Execute the following 5 tasks in parallel using the Task tool:**

Analyze each company in {{target_companies}} as follows:

### AWS Analysis
Analyze Amazon AWS's business strategy, technological advantages, market share, and latest services, and save to {{aws_analysis}}.

### Azure Analysis  
Analyze Microsoft Azure's business strategy, enterprise focus, Office365 integration, and growth strategy, and save to {{azure_analysis}}.

### GCP Analysis
Analyze Google Cloud Platform's technological innovation, AI/ML specialized strategy, and data analytics strengths, and save to {{gcp_analysis}}.

### IBM Analysis
Analyze IBM Cloud's hybrid strategy, enterprise solutions, and AI Watson utilization, and save to {{ibm_analysis}}.

### Oracle Analysis
Analyze Oracle Cloud's database strengths, enterprise customer base, and integration strategy, and save to {{oracle_analysis}}.

## Competitive Comparison Matrix Creation
Please compare {{aws_analysis}}, {{azure_analysis}}, {{gcp_analysis}}, {{ibm_analysis}}, and {{oracle_analysis}}, and create a competitive matrix from the following perspectives, saving to {{comparison_matrix}}:
- Market share
- Technological advantages
- Price competitiveness
- Customer satisfaction
- Growth potential

## Strategic Insights Extraction
Based on {{comparison_matrix}}, please analyze the competitive structure in the market and future development forecasts, and save strategic insights to competitive_insights.json for persistence.

---

**Learning Points**:
- Scalable design with 5 parallel tasks
- Individual analysis perspectives tailored to each company's characteristics
- Systematic comparison methods for multiple analysis results
- Strategic insight extraction process
- File persistence for important information storage
- Construction of more complex parallel processing systems

**Advanced Parallel Processing Features**:
1. **Scalability**: Easily expandable from 3 to 5+ parallel tasks
2. **Specialization**: Each task targets company-specific strengths and strategies
3. **Data Persistence**: Critical analysis saved to JSON files for future reference
4. **Multi-stage Integration**: Parallel results → comparison matrix → strategic insights
5. **Business Intelligence**: Converts raw data into actionable strategic intelligence

This intermediate example demonstrates how Parallel Processing can handle complex competitive intelligence gathering with multiple data streams, specialized analysis approaches, and sophisticated integration workflows.