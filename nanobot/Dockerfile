# Multi-stage Dockerfile for nanobot gateway

ARG REGISTRY_PREFIX_DOCKER_HUB
FROM ${REGISTRY_PREFIX_DOCKER_HUB}astral/uv:python3.14-bookworm-slim AS builder
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
ENV UV_NO_DEV=1
ENV UV_PYTHON_DOWNLOADS=0

WORKDIR /app

# Copy root workspace files
COPY --from=workspace pyproject.toml uv.lock /app/

# Copy workspace packages
COPY --from=workspace mcp/mcp-lms /app/mcp/mcp-lms
COPY --from=workspace mcp/mcp-obs /app/mcp/mcp-obs
COPY --from=workspace nanobot-websocket-channel /app/nanobot-websocket-channel

# Copy nanobot package
COPY pyproject.toml /app/nanobot/pyproject.toml
COPY . /app/nanobot

# Install nanobot with dependencies
RUN --mount=type=cache,target=/root/.cache/uv uv sync --frozen --package nanobot

# Install webchat and obs packages in the venv using uv pip
RUN --mount=type=cache,target=/root/.cache/uv uv pip install nanobot-websocket-channel/nanobot-webchat nanobot-websocket-channel/mcp-webchat nanobot-websocket-channel/nanobot-channel-protocol mcp/mcp-obs

# ---
# Stage 2: Final runtime image
# ---

ARG REGISTRY_PREFIX_DOCKER_HUB
FROM ${REGISTRY_PREFIX_DOCKER_HUB}python:3.14.2-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV LANG=C.UTF-8

ARG APP_UID=1000
ARG APP_GID=1000

RUN groupadd --system --gid ${APP_GID} appuser && useradd --system --gid ${APP_GID} --uid ${APP_UID} --create-home appuser

COPY --from=builder --chown=appuser:appuser /app /app

ENV PATH=/app/.venv/bin:$PATH

USER appuser

WORKDIR /app/nanobot

CMD ["python", "/app/nanobot/entrypoint.py"]
