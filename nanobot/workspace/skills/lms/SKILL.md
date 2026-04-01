---
name: lms
description: Use LMS MCP tools for live course data
always: true
---

# LMS Skill

You have access to the LMS (Learning Management System) via MCP tools. Use them to provide real-time data about the course.

## Available Tools

- `lms_health` - Check if the LMS backend is healthy and get item count
- `lms_labs` - Get list of all available labs
- `lms_learners` - Get list of all learners/students
- `lms_pass_rates` - Get pass rates for a specific lab
- `lms_timeline` - Get submission timeline for a specific lab
- `lms_groups` - Get group performance data
- `lms_top_learners` - Get top performing learners for a specific lab
- `lms_completion_rate` - Get completion rate for a specific lab
- `lms_sync_pipeline` - Trigger the ETL sync pipeline

## Strategy

### When user asks about scores, pass rates, completion, groups, timeline, or top learners:

1. **If lab is not specified**: First call `lms_labs` to get available labs
2. **If multiple labs exist**: Ask the user to choose which lab they want to see
   - Use lab titles as user-facing labels (e.g., "Lab 01 – Products, Architecture & Roles")
   - Let the shared `structured-ui` skill decide how to present that choice
3. **Once lab is selected**: Call the appropriate tool with the lab parameter

### When user asks "what can you do?":

Explain your current capabilities:
- You can check LMS backend health
- You can list available labs
- You can show pass rates, completion rates, timelines for specific labs
- You can show group performance and top learners
- You can trigger data sync if data seems outdated

### Response formatting:

- Format percentages nicely (e.g., "75%" not "0.75")
- Keep responses concise
- Include relevant numbers (counts, percentages) when available
- If backend is unhealthy or empty, suggest running `lms_sync_pipeline`

## Important Rules

- Always check if a lab parameter is needed before calling tools
- When in doubt about which lab, call `lms_labs` first
- Use each lab title as the default user-facing label
- Let the shared `structured-ui` skill handle choice presentation on supported channels
