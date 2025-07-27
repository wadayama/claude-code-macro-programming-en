# A.6 Audit Log System Test Macro

A simple test macro for verifying core concepts of the A.6 audit log system.
Tests basic functionality of multiple variable settings, conditional judgments, and decision reasoning recording.

## Execution Steps

### Step 1: Initial Value Setting
Save 10 to {{value}}

### Step 2: Value Update (Multiple Times)
Get {{value}}

Save 20 to {{value}}

Record 'Updated from initial value 10 to 20' with reasoning 'Gradual value change test' to log

### Step 3: Conditional Judgment 1
Get {{value}}

If {{value}} is 15 or higher, save "high" to {{status}}; if less than 15, save "low" to {{status}}

Record 'Judged as {{status}} because {{value}}' with reasoning 'Two-stage judgment based on 15 threshold' to log

### Step 4: Value Re-update
Save 5 to {{value}}

Record reasoning 'For confirming conditional judgment behavior' with result 'Low category test execution' in context 'Changed value from 20 to 5' to log

### Step 5: Conditional Judgment 2 (Re-execution)
Get {{value}}

If {{value}} is 15 or higher, save "high" to {{status}}; if less than 15, save "low" to {{status}}

Record 'Re-judged {{value}} as {{status}}' with reasoning 'Judgment confirmation after value change with same logic' to log

### Step 6: Three-stage Judgment
Get {{value}}

Set {{category}} based on {{value}} value:
- 20 or higher: "A"
- 10 or higher but less than 20: "B"  
- Less than 10: "C"

Record 'Classified into {{category}} category by {{value}}' with reasoning 'Classification logic using three-stage thresholds' to log

### Step 7: Result Display
Get {{value}}, {{status}}, and {{category}} and display the results

## Expected Audit Log Records

1. **Variable Operation Logs (7 records)**:
   - {{value}} CREATE: 10
   - {{value}} UPDATE: 10→20  
   - {{status}} CREATE: high
   - {{value}} UPDATE: 20→5
   - {{status}} UPDATE: high→low
   - {{category}} CREATE: C

2. **Decision Reasoning Logs (4 records)**:
   - Initial value update judgment
   - 1st conditional judgment decision
   - 2nd conditional judgment decision  
   - Three-stage judgment decision

3. **Reasoning Process Logs (1 record)**:
   - Value change reasoning process

## Verification Points

- [ ] Multiple updates of the same variable are correctly recorded
- [ ] Conditional judgment decision reasoning is saved in structured format
- [ ] Variable history allows tracking of change trajectories
- [ ] All logs can be verified with audit_viewer.py
- [ ] Transparency of judgment logic is ensured

This simple structure ensures reliable verification of the audit log system's basic functionality.