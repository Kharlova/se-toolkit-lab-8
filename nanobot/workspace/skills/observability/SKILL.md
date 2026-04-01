---
name: observability
description: Use observability MCP tools for logs and traces analysis
always: true
---

# Observability Skill

You have access to observability tools via MCP:
- logs_search — search VictoriaLogs by LogsQL query
- logs_error_count — count errors per service in a time window
- traces_list — list recent traces for a service
- traces_get — get a specific trace by ID with full span hierarchy

## Strategy for "What went wrong?" or "Check system health"

When the user asks about errors, failures, or system health:

1. **First, check error count**: Use logs_error_count with a recent time window (default "10m" or "1h" depending on context) and service name (e.g., "Learning Management Service" for LMS backend).

2. **If errors exist, search logs**: Use logs_search with a query like:
   - `_time:10m service.name:"Learning Management Service" severity:ERROR`
   - Extract key details: error message, trace_id, span_id, timestamp

3. **Extract trace_id**: From the log results, look for the trace_id field in error entries.

4. **Fetch the trace**: Use traces_get with the trace_id to see the full request flow and identify where the failure occurred.

5. **Summarize findings concisely**:
   - State how many errors occurred and in what time window
   - Name the affected service
   - Quote the specific error message from logs
   - Describe what the trace shows (which span failed, what operation)
   - Explain the root cause in plain language
   - Do NOT dump raw JSON - synthesize the information

## Example response format

```
Found X errors in the last [time window] for [service name].

**Error details:**
- Time: [timestamp]
- Error: [specific error message from logs]
- Trace ID: [trace_id]

**Trace analysis:**
The trace shows the failure occurred at [span/operation name]. 
The [specific operation] failed with [error type].

**Root cause:**
[Plain language explanation of what went wrong]

**Recommendation:**
[Suggested fix or next step]
```

## Important guidelines

- Always use recent time windows (_time:10m or _time:1h) to avoid historical noise
- Focus on the specific service the user asks about
- Connect log evidence with trace evidence in your explanation
- If no errors are found, say so clearly: "No errors found in the last [time window] for [service]. The system appears healthy."
- When investigating failures, mention BOTH what the logs show AND what the trace reveals
