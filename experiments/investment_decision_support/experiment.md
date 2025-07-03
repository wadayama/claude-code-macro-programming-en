# Investment Decision Support System Experiment (HITL Intermediate)

**Experiment Goal**: Verification of responsibility clarification and safety assurance effects of HITL in high-risk investment decisions

**Verification Items**: 
1. Human intervention effects in high-risk decisions
2. Responsibility visualization and transparency
3. Staged risk assessment process
4. Human value in final decisions

---

## Step 1: Investment Case Data Loading

Please load investment_data.json and set it to {{investment_data}}.

Display "Investment case data loaded".

Please confirm the following information from {{investment_data}}:
- Investment case name
- Investment amount
- Expected return
- Major risk factors

---

## Step 2: Basic Analysis Execution

Based on {{investment_data}}, execute the following basic analysis and set to {{basic_analysis}}:

### Financial Analysis
- ROI (Return on Investment) calculation
- Payback period calculation
- Risk-return ratio evaluation

### Market Analysis
- Market size and growth potential evaluation
- Competitive situation analysis
- Market entry difficulty assessment

### Technical Analysis
- Technical advantage evaluation
- Feasibility verification
- Technical risk identification

Display "Basic analysis completed".

---

## Step 3: Investment Strategy Confirmation (Human Intervention Point 1)

Display "=== Investment Strategy Confirmation (Human Decision Required) ===".

Based on {{basic_analysis}} results, please provide your judgment on the following investment strategy:

**Proposed Strategy**: Recommended approach for {{investment_data}} case
- Aggressive Investment: Offensive investment targeting high returns
- Conservative Investment: Stability-oriented investment with controlled risks  
- Staged Investment: Start small and monitor progress
- Investment Decline: No investment due to excessive risks

**Decision Materials**:
- Expected ROI: Extract from {{basic_analysis}}
- Major Risks: Extract from {{basic_analysis}}  
- Market Opportunities: Extract from {{basic_analysis}}

Which strategy do you choose? Please include your reasoning for the selection.

Please set your strategy decision to {{strategy_decision}}.

---

## Step 4: Risk Assessment and Approval (Human Intervention Point 2)

Display "=== Risk Assessment Confirmation (Human Approval Required) ===".

Based on {{strategy_decision}}, please review the following risk assessment results:

### Identified Risk Factors
Based on {{basic_analysis}} and {{strategy_decision}}, analyze major risk factors and set to {{risk_analysis}}:

- **Market Risk**: Impact of market environment changes
- **Technical Risk**: Technical implementation difficulties
- **Competitive Risk**: Impact of competitor actions
- **Financial Risk**: Difficulties in funding and recovery
- **Legal Risk**: Impact of regulatory changes

### Risk Mitigation Measures
Set mitigation measures for each risk to {{risk_mitigation}}.

### Approval Confirmation
Based on {{risk_analysis}} and {{risk_mitigation}}:

Do you approve continuing investment consideration with these risk assessment results?
- "Approved": Risks are within acceptable range, continue investment consideration
- "Revision Required": Risk assessment or mitigation measures need review
- "Abort": Risks are too high, abort investment

Please set your risk approval decision to {{risk_approval}}.

---

## Step 5: Final Investment Decision (Human Intervention Point 3)

Display "=== Final Investment Decision (Human Final Decision) ===".

Only proceed to final investment decision if {{risk_approval}} is "Approved".

### Investment Decision Summary
Please make your final investment decision based on the following comprehensive information:

**Investment Case**: Display case name from {{investment_data}}
**Selected Strategy**: {{strategy_decision}}
**Risk Assessment**: Summary of {{risk_analysis}}
**Expected Effects**: Display expected returns from {{basic_analysis}}

### Final Decision Options
1. **Execute Investment**: Execute investment under proposed conditions
2. **Conditional Investment**: Execute investment with additional conditions
3. **Postpone Investment**: Re-evaluate after further consideration
4. **Cancel Investment**: Do not proceed with investment

**Important**: This decision means investment execution and carries financial responsibility.

Please provide your final decision after careful consideration.
Please provide detailed reasoning for your decision.

Please set your final investment decision to {{final_decision}}.

---

## Step 6: Decision Record Persistence

Please save the following investment decision record to decision_log.json:

```json
{
  "investment_case": "Investment case name",
  "timestamp": "Decision execution date/time",
  "human_decisions": {
    "strategy_phase": {
      "decision": "{{strategy_decision}}",
      "rationale": "Reasoning for strategy selection",
      "responsibility": "Strategic direction determination"
    },
    "risk_phase": {
      "decision": "{{risk_approval}}",
      "risk_factors": "{{risk_analysis}}",
      "mitigation": "{{risk_mitigation}}",
      "responsibility": "Risk assessment validity confirmation"
    },
    "final_phase": {
      "decision": "{{final_decision}}",
      "rationale": "Final decision reasoning",
      "responsibility": "Final investment execution decision"
    }
  },
  "ai_contribution": {
    "basic_analysis": "{{basic_analysis}}",
    "risk_identification": "{{risk_analysis}}",
    "data_processing": "Objective analysis and information organization"
  },
  "accountability": {
    "decision_maker": "Human (specific individual)",
    "ai_role": "Analysis support only, no decision responsibility",
    "audit_trail": "Complete record of all decision processes"
  }
}
```

Display "Investment decision process completed: Achieved transparent decision-making where humans take responsibility for all critical decisions".

---

## Experiment Verification Points

### HITL Effect Confirmation
1. **Responsibility Clarification**: Design where humans clearly take responsibility at each stage
2. **Decision Transparency**: All processes recorded and verifiable later
3. **Risk Mitigation**: Human intervention prevents serious misjudgments
4. **Efficiency**: AI handles analysis while humans focus on decisions

### HITL Value in High-Risk Decisions
- **Strategic Level**: Human determination of investment policies
- **Assessment Level**: Human approval of risk validity  
- **Execution Level**: Human acceptance of final responsibility

Display "Investment decision support HITL experiment completed: Verified appropriate role distribution between humans and AI in high-risk decisions".