# Lab 8 — Report

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

**Analysis:** The skill prompt successfully teaches the agent to call lms_labs first when lab is not specified, then ask the user to choose which lab they want to see.
