# Lab 8 — Report

## Task 1A — Bare agent

**Terminal session: cli:task1a-loop**

```
$ uv run nanobot agent --logs --session cli:task1a-loop -c ./config.json -m "What is the agentic loop?"

nanobot
The agentic loop is the fundamental cycle that autonomous AI agents follow to accomplish tasks.

The Four Stages:
1. Perceive: The agent receives input and builds a representation of the current situation
2. Plan: Based on its goal, the agent decides what to do next
3. Act: The agent executes an action (calling a tool, running code, sending a message)
4. Observe: The agent receives feedback from the action
5. Reflect: The agent evaluates progress and decides whether to continue or adjust

Why It Matters:
- Autonomy: Agents can work without constant human guidance
- Adaptability: Agents can adjust when things dont go as expected
- Multi-step reasoning: Complex tasks get broken into manageable steps
- Self-correction: Agents can detect and fix their own mistakes
```

---

**Terminal session: cli:task1a-labs**

```
$ uv run nanobot agent --logs --session cli:task1a-labs -c ./config.json -m "What labs are available in our LMS?"

nanobot
Based on my exploration of the workspace, here are the available labs:

Current Lab: Lab 8 — AI Agentic Framework with Nanobot

Previous Labs:
- Lab 1 — Documentation available in wiki
- Lab 2 — Backend service setup
- Lab 3 — Backend API implementation
- Lab 4 — Testing and frontend
- Lab 5 — Data pipeline and analytics
- Lab 6 — Build Your Own Agent
- Lab 7 — Telegram Bot with Manual LLM Tool-Calling Loop
```

## Task 1B — Agent with LMS tools

**Terminal session: cli:task1b-labs**

```
$ uv run nanobot agent --logs --session cli:task1b-labs -c ./config.json -m "What labs are available?"

2026-04-01 18:20:15.534 | INFO | nanobot.agent.tools.mcp:connect_mcp_servers:246 - MCP server lms: connected, 9 tools registered
2026-04-01 18:20:30.113 | INFO | nanobot.agent.loop:_prepare_tools:253 - Tool call: mcp_lms_lms_labs({})

nanobot
Here are the available labs:

1. Lab 01 – Products, Architecture & Roles
2. Lab 02 — Run, Fix, and Deploy a Backend Service
3. Lab 03 — Backend API: Explore, Debug, Implement, Deploy
4. Lab 04 — Testing, Front-end, and AI Agents
5. Lab 05 — Data Pipeline and Analytics Dashboard
6. Lab 06 — Build Your Own Agent
7. Lab 07 — Build a Client with an AI Coding Agent
8. lab-08

Would you like more details about any specific lab?
```

---

**Terminal session: cli:task1b-health**

```
$ uv run nanobot agent --logs --session cli:task1b-health -c ./config.json -m "Is the LMS backend healthy?"

2026-04-01 18:21:00.387 | INFO | nanobot.agent.loop:_prepare_tools:253 - Tool call: mcp_lms_lms_health({})

nanobot
Yes, the LMS backend is healthy. It currently has 56 items in the system.
```

## Task 1C — Skill prompt

**Terminal session: cli:task1c**

```
$ uv run nanobot agent --logs --session cli:task1c -c ./config.json -m "Show me the scores"

2026-04-01 18:22:47.076 | INFO | nanobot.agent.tools.mcp:connect_mcp_servers:246 - MCP server lms: connected, 9 tools registered
2026-04-01 18:23:03.589 | INFO | nanobot.agent.loop:_prepare_tools:253 - Tool call: mcp_lms_lms_labs({})

nanobot
Ill check the available labs and get the score data for you.

There are 8 labs available. Which lab would you like to see the scores for? Here are the options:

1. Lab 01 – Products, Architecture & Roles
2. Lab 02 — Run, Fix, and Deploy a Backend Service
3. Lab 03 — Backend API: Explore, Debug, Implement, Deploy
4. Lab 04 — Testing, Front-end, and AI Agents
5. Lab 05 — Data Pipeline and Analytics Dashboard
6. Lab 06 — Build Your Own Agent
7. Lab 07 — Build a Client with an AI Coding Agent
8. lab-08

Or would you like me to show scores for all labs?
```

**Analysis:** The skill prompt teaches the agent to call lms_labs first when lab is not specified, then ask the user to choose.
