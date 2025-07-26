Please execute the following process. However, make sure not to timeout during the event waiting loop.

0. Clear all variables.
1. Get the current value of {{kick_condition}}
2. Event waiting loop: If the value is not "ready", get {{kick_condition}} again
3. Repeat step 2 until it becomes "ready"
4. When "ready" is confirmed, proceed to the next process

Save "completed" to {{macro_message}}