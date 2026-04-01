# Lab 8 — Report

Paste your checkpoint evidence below. Add screenshots as image files in the repo and reference them with `![description](path)`.

## Task 1A — Bare agent

**Question 1: "What is the agentic loop?"**

The **agentic loop** is the fundamental cycle that autonomous AI agents follow to accomplish tasks. It's the core reason agents can act independently rather than just responding to prompts.

### The Four Stages

1. **Perceive**: The agent receives input (user message, sensor data, tool results) and builds a representation of the current situation

2. **Plan**: Based on its goal and current understanding, the agent decides what to do next

3. **Act**: The agent executes an action (calling a tool, running code, sending a message, etc.)

4. **Observe**: The agent receives feedback from the action (results, errors, new information)

5. **Reflect**: The agent evaluates progress, updates its understanding, and decides whether to continue, adjust the plan, or terminate

### Why It Matters

This loop enables:
- **Autonomy**: Agents can work without constant human guidance
- **Adaptability**: Agents can adjust when things don't go as expected
- **Multi-step reasoning**: Complex tasks get broken into manageable steps
- **Self-correction**: Agents can detect and fix their own mistakes

### Variations

Different frameworks use slightly different formulations:
- **ReAct (Reason + Act)**: Interleaves reasoning traces with actions
- **Reflexion**: Adds explicit self-reflection to improve future attempts
- **Tree of Thoughts**: Explores multiple reasoning paths before acting

The agentic loop is what distinguishes autonomous agents from simple chatbots—instead of just responding to prompts, agents actively pursue goals through iterative cycles of reasoning and action.

---

**Question 2: "What labs are available in our LMS?"**

Based on my exploration of the workspace, here are the **available labs** in your LMS:

### Current Lab
**Lab 8** — AI Agentic Framework with Nanobot

### Previous Labs
- **Lab 1** — Documentation available in wiki
- **Lab 2** — Backend service setup
- **Lab 3** — Backend API implementation
- **Lab 4** — Testing and frontend
- **Lab 5** — Data pipeline and analytics
- **Lab 6** — Build Your Own Agent
- **Lab 7** — Telegram Bot with Manual LLM Tool-Calling Loop

### Lab 8 Task Overview

| Task | Type | Description |
|------|------|-------------|
| Task 1 | Required | Set Up the Agent (install nanobot, configure MCP server, skills, channels) |
| Task 2 | Required | Details in lab/tasks/required/task-2.md |
| Task 3 | Required | Details in lab/tasks/required/task-3.md |
| Task 4 | Required | Details in lab/tasks/required/task-4.md |
| Task 5 | Required | Details in lab/tasks/required/task-5.md |
| Task 1 | Optional | Extension task |

The LMS system includes:
- **LMS API** — FastAPI backend for managing learning data
- **LMS Frontend** — React client for displaying items and dashboard charts
- **Nanobot Integration** — AI agent framework with skills, memory, cron scheduling, and multiple channels (Telegram, WebSocket, etc.)

## Task 1B — Agent with LMS tools

**Question 1: "What labs are available?"**

Here are the available labs:

1. **Lab 01** – Products, Architecture & Roles
2. **Lab 02** — Run, Fix, and Deploy a Backend Service
3. **Lab 03** — Backend API: Explore, Debug, Implement, Deploy
4. **Lab 04** — Testing, Front-end, and AI Agents
5. **Lab 05** — Data Pipeline and Analytics Dashboard
6. **Lab 06** — Build Your Own Agent
7. **Lab 07** — Build a Client with an AI Coding Agent
8. **lab-08**

Would you like more details about any specific lab, such as completion rates, pass rates, or submission timelines?

---

**Question 2: "Is the LMS backend healthy?"**

Yes, the LMS backend is healthy. It currently has 56 items in the system.

---

**Note:** The agent now returns **real backend data** via MCP tools. Before MCP was configured (in Task 1A), the agent could only explore local files. Now it calls `lms_labs`, `lms_health`, and other tools to fetch live data from the LMS API.

## Task 1C — Skill prompt

**Question: "Show me the scores"** (without specifying a lab)

**Agent response:**

I'll check the available labs and get the score data for you.

There are 8 labs available. Which lab would you like to see the scores for? Here are the options:

1. **Lab 01** – Products, Architecture & Roles
2. **Lab 02** — Run, Fix, and Deploy a Backend Service
3. **Lab 03** — Backend API: Explore, Debug, Implement, Deploy
4. **Lab 04** — Testing, Front-end, and AI Agents
5. **Lab 05** — Data Pipeline and Analytics Dashboard
6. **Lab 06** — Build Your Own Agent
7. **Lab 07** — Build a Client with an AI Coding Agent
8. **lab-08**

Or would you like me to show scores for all labs?

---

**Analysis:**

The skill prompt successfully teaches the agent to:
1. **Detect missing parameters**: When "scores" is requested without a lab, the agent doesn't guess
2. **Call `lms_labs` first**: The agent fetches the list of available labs
3. **Present choices clearly**: Lists all 8 labs with their full titles
4. **Ask for clarification**: Prompts the user to choose a specific lab

This behavior matches the strategy defined in `workspace/skills/lms/SKILL.md`:
> "If the user asks for scores, pass rates, completion, groups, timeline, or top learners without naming a lab, call `lms_labs` first. If multiple labs are available, ask the user to choose one."

## Task 2A — Deployed agent

**Nanobot gateway startup logs:**

```
nanobot-1  | 🐈 Starting nanobot gateway version 0.1.4.post5 on port 18790...
nanobot-1  | ✓ Channels enabled: webchat
nanobot-1  | ✓ Heartbeat: every 1800s
nanobot-1  | ✓ Channels enabled: webchat
nanobot-1  | Starting webchat channel...
nanobot-1  | MCP server 'lms': connected, 9 tools registered
nanobot-1  | Agent loop started
```

**Services running:**
- nanobot gateway on port 18790
- WebChat channel enabled for WebSocket connections
- MCP LMS server connected with 9 tools (lms_health, lms_labs, lms_learners, lms_pass_rates, lms_timeline, lms_groups, lms_top_learners, lms_completion_rate, lms_sync_pipeline)

## Task 2B — Web client

**Flutter web client deployed at:** `http://<vm-ip>:42002/flutter`

**WebSocket endpoint:** `ws://localhost:42002/ws/chat?access_key=NANOBOT_ACCESS_KEY`

**Nanobot logs showing webchat channel:**
```
nanobot-1  | ✓ Channels enabled: webchat
nanobot-1  | Starting webchat channel...
nanobot-1  | Outbound dispatcher started
nanobot-1  | MCP server 'lms': connected, 9 tools registered
nanobot-1  | Agent loop started
```

**Caddy routing:**
- `/flutter*` → Flutter web client (static files from Docker volume)
- `/ws/chat` → WebSocket reverse proxy to nanobot:8765

**Access key:** Protected by `NANOBOT_ACCESS_KEY` environment variable

**Test conversation:**

```bash
$ echo '{"content":"What labs are available?"}' | websocat "ws://localhost:42002/ws/chat?access_key=мой-пароль-для-нанобота"
```

**Actual agent response received via WebSocket:**
```json
{
  "type": "text",
  "content": "Here are the available labs:\n\n1. **Lab 01** – Products, Architecture & Roles\n2. **Lab 02** — Run, Fix, and Deploy a Backend Service\n3. **Lab 03** — Backend API: Explore, Debug, Implement, Deploy\n4. **Lab 04** — Testing, Front-end, and AI Agents\n5. **Lab 05** — Data Pipeline and Analytics Dashboard\n6. **Lab 06** — Build Your Own Agent\n7. **Lab 07** — Build a Client with an AI Coding Agent\n8. **Lab 08** — lab-08\n\nWould you like to see details about a specific lab, such as pass rates, completion rates, submission timeline, group performance, or top learners?",
  "format": "markdown"
}
```

**Rendered response:**
> Here are the available labs:
> 
> 1. **Lab 01** – Products, Architecture & Roles
> 2. **Lab 02** — Run, Fix, and Deploy a Backend Service
> 3. **Lab 03** — Backend API: Explore, Debug, Implement, Deploy
> 4. **Lab 04** — Testing, Front-end, and AI Agents
> 5. **Lab 05** — Data Pipeline and Analytics Dashboard
> 6. **Lab 06** — Build Your Own Agent
> 7. **Lab 07** — Build a Client with an AI Coding Agent
> 8. **Lab 08** — lab-08
> 
> Would you like to see details about a specific lab, such as pass rates, completion rates, submission timeline, group performance, or top learners?

**Verification:**
- Flutter serves main.dart.js at /flutter ✓
- WebSocket endpoint accepts connections at /ws/chat ✓
- Nanobot gateway running with webchat channel enabled ✓

## Task 3A — Structured logging

<!-- Paste happy-path and error-path log excerpts, VictoriaLogs query screenshot -->

## Task 3B — Traces

<!-- Screenshots: healthy trace span hierarchy, error trace -->

## Task 3C — Observability MCP tools

<!-- Paste agent responses to "any errors in the last hour?" under normal and failure conditions -->

## Task 4A — Multi-step investigation

<!-- Paste the agent's response to "What went wrong?" showing chained log + trace investigation -->

## Task 4B — Proactive health check

<!-- Screenshot or transcript of the proactive health report that appears in the Flutter chat -->

## Task 4C — Bug fix and recovery

<!-- 1. Root cause identified
     2. Code fix (diff or description)
     3. Post-fix response to "What went wrong?" showing the real underlying failure
     4. Healthy follow-up report or transcript after recovery -->
