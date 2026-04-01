#!/usr/bin/env python3
"""MCP server for observability tools."""
import asyncio
import json
import os
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
import httpx

VICTORIALOGS_URL = os.environ.get("VICTORIALOGS_URL", "http://localhost:9428")
VICTORIATRACES_URL = os.environ.get("VICTORIATRACES_URL", "http://localhost:10428")

server = Server("mcp-obs")

@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="logs_search",
            description="Search VictoriaLogs by LogsQL query. Returns matching log entries.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "LogsQL query (e.g., '_time:10m severity:ERROR')"},
                    "limit": {"type": "integer", "description": "Max results", "default": 10}
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="logs_error_count",
            description="Count errors per service in a time window.",
            inputSchema={
                "type": "object",
                "properties": {
                    "time_window": {"type": "string", "description": "Time window (e.g., '10m', '1h')", "default": "10m"},
                    "service": {"type": "string", "description": "Service name filter (optional)"}
                }
            }
        ),
        Tool(
            name="traces_list",
            description="List recent traces for a service from VictoriaTraces.",
            inputSchema={
                "type": "object",
                "properties": {
                    "service": {"type": "string", "description": "Service name"},
                    "limit": {"type": "integer", "description": "Max traces", "default": 5}
                },
                "required": ["service"]
            }
        ),
        Tool(
            name="traces_get",
            description="Get a specific trace by ID with full span hierarchy.",
            inputSchema={
                "type": "object",
                "properties": {
                    "trace_id": {"type": "string", "description": "Trace ID (hex string)"}
                },
                "required": ["trace_id"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    async with httpx.AsyncClient(timeout=30.0) as client:
        if name == "logs_search":
            query = arguments.get("query", "")
            limit = arguments.get("limit", 10)
            url = f"{VICTORIALOGS_URL}/select/logsql/query"
            params = {"query": query, "limit": str(limit)}
            resp = await client.get(url, params=params)
            resp.raise_for_status()
            logs = resp.json() if resp.text else []
            return [TextContent(type="text", text=json.dumps(logs, indent=2)[:4000])]
        
        elif name == "logs_error_count":
            time_window = arguments.get("time_window", "10m")
            service = arguments.get("service", "")
            query = f"_time:{time_window} severity:ERROR"
            if service:
                query += f' service.name:"{service}"'
            url = f"{VICTORIALOGS_URL}/select/logsql/query"
            params = {"query": query, "limit": "1000"}
            resp = await client.get(url, params=params)
            resp.raise_for_status()
            logs = resp.json() if resp.text else []
            # Count by service
            counts = {}
            for entry in logs if isinstance(logs, list) else []:
                svc = entry.get("service.name", "unknown") if isinstance(entry, dict) else "unknown"
                counts[svc] = counts.get(svc, 0) + 1
            return [TextContent(type="text", text=json.dumps(counts, indent=2))]
        
        elif name == "traces_list":
            service = arguments.get("service", "")
            limit = arguments.get("limit", 5)
            url = f"{VICTORIATRACES_URL}/select/jaeger/api/traces"
            params = {"service": service, "limit": str(limit)}
            resp = await client.get(url, params=params)
            resp.raise_for_status()
            data = resp.json()
            traces = data.get("data", []) if isinstance(data, dict) else []
            summary = [{"traceID": t.get("traceID"), "spans": len(t.get("spans", []))} for t in traces[:5]]
            return [TextContent(type="text", text=json.dumps(summary, indent=2))]
        
        elif name == "traces_get":
            trace_id = arguments.get("trace_id", "")
            url = f"{VICTORIATRACES_URL}/select/jaeger/api/traces/{trace_id}"
            resp = await client.get(url)
            resp.raise_for_status()
            data = resp.json()
            return [TextContent(type="text", text=json.dumps(data, indent=2)[:4000])]
        
        else:
            raise ValueError(f"Unknown tool: {name}")

def main():
    asyncio.run(_run_server())

async def _run_server():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())

if __name__ == "__main__":
    main()
