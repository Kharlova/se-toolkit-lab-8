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

## Strategy

### When the user asks about errors or issues:

1. First, check error count: Use logs_error_count with the relevant time window (default 10m) and service name (e.g., Learning Management Service for LMS backend).

2. If errors exist, search logs: Use logs_search with a query like _time:10m severity:ERROR service.name:Learning Management Service to get details.

3. Extract trace_id: From the log results, look for trace_id field in error entries.

4. Fetch the trace: Use traces_get with the trace_id to see the full request flow and identify where the failure occurred.

5. Summarize findings: Provide a concise summary:
   - How many errors occurred
   - What service was affected
   - What the error was (e.g., connection refused, database query failed)
   - Which trace shows the failure

### Example queries:

- For LMS backend errors in last 10 minutes:
  - logs_error_count with time_window=10m, service=Learning Management Service
  - logs_search with query=_time:10m service.name:Learning Management Service severity:ERROR

- For tracing a specific request:
  - Extract trace_id from logs
  - traces_get with that trace_id

### Response format:

Keep responses concise. Do not dump raw JSON. Summarize:
- Found X errors in the last 10 minutes for service Y.
- The most recent error was: [error message]
- Trace [ID] shows the failure occurred at [span/service].

### Important:

- Always narrow the time window to recent data (e.g., _time:10m) to avoid historical noise.
- Focus on the specific service the user asks about (e.g., Learning Management Service for LMS backend).
- If no errors are found, say so clearly: No errors found in the last 10 minutes for [service].
