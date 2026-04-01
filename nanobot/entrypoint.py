#!/usr/bin/env python3
"""
Entrypoint for nanobot gateway in Docker.
Resolves environment variables into config.json at runtime.
"""
import json
import os
import sys
from pathlib import Path

def main():
    # Paths
    app_dir = Path("/app")
    nanobot_dir = app_dir / "nanobot"
    config_path = nanobot_dir / "config.json"
    # Write resolved config to /tmp to avoid permission issues
    resolved_path = Path("/tmp/config.resolved.json")
    workspace_dir = nanobot_dir / "workspace"

    # Read base config
    with open(config_path) as f:
        config = json.load(f)

    # Override from environment variables
    # LLM provider settings
    if api_key := os.environ.get("LLM_API_KEY"):
        config["providers"]["custom"]["apiKey"] = api_key
    if api_base := os.environ.get("LLM_API_BASE_URL"):
        config["providers"]["custom"]["apiBase"] = api_base
    if api_model := os.environ.get("LLM_API_MODEL"):
        config["agents"]["defaults"]["model"] = api_model

    # Gateway settings
    if gateway_host := os.environ.get("NANOBOT_GATEWAY_CONTAINER_ADDRESS"):
        config.setdefault("gateway", {})["host"] = gateway_host
    if gateway_port := os.environ.get("NANOBOT_GATEWAY_CONTAINER_PORT"):
        config.setdefault("gateway", {})["port"] = int(gateway_port)

    # Webchat channel settings
    if webchat_host := os.environ.get("NANOBOT_WEBCHAT_CONTAINER_ADDRESS"):
        config.setdefault("channels", {}).setdefault("webchat", {})["host"] = webchat_host
    if webchat_port := os.environ.get("NANOBOT_WEBCHAT_CONTAINER_PORT"):
        config.setdefault("channels", {}).setdefault("webchat", {})["port"] = int(webchat_port)
    
    # Enable webchat channel if env var is set
    if os.environ.get("NANOBOT_WEBCHAT_ENABLED", "").lower() == "true":
        config.setdefault("channels", {}).setdefault("webchat", {})["enabled"] = True
        config["channels"]["webchat"].setdefault("allowFrom", ["*"])

    # MCP LMS server settings
    if "lms" in config.get("tools", {}).get("mcpServers", {}):
        if lms_backend_url := os.environ.get("NANOBOT_LMS_BACKEND_URL"):
            config["tools"]["mcpServers"]["lms"]["env"]["NANOBOT_LMS_BACKEND_URL"] = lms_backend_url
        if lms_api_key := os.environ.get("NANOBOT_LMS_API_KEY"):
            config["tools"]["mcpServers"]["lms"]["env"]["NANOBOT_LMS_API_KEY"] = lms_api_key

    # MCP Webchat server settings
    if webchat_relay_url := os.environ.get("NANOBOT_WEBCCHAT_UI_RELAY_URL"):
        config.setdefault("tools", {}).setdefault("mcpServers", {}).setdefault("webchat", {})
        config["tools"]["mcpServers"].setdefault("webchat", {})["command"] = "python"
        config["tools"]["mcpServers"]["webchat"]["args"] = ["-m", "mcp_webchat"]
        config["tools"]["mcpServers"]["webchat"]["env"] = {
            "NANOBOT_WEBCCHAT_UI_RELAY_URL": webchat_relay_url,
        }
    if webchat_token := os.environ.get("NANOBOT_WEBCCHAT_UI_RELAY_TOKEN"):
        config["tools"]["mcpServers"]["webchat"]["env"]["NANOBOT_WEBCCHAT_UI_RELAY_TOKEN"] = webchat_token

    # Write resolved config
    with open(resolved_path, "w") as f:
        json.dump(config, f, indent=2)

    print(f"Using config: {resolved_path}", file=sys.stderr)

    # Launch nanobot gateway
    os.execvp("nanobot", [
        "nanobot",
        "gateway",
        "--config", str(resolved_path),
        "--workspace", str(workspace_dir)
    ])

if __name__ == "__main__":
    main()
