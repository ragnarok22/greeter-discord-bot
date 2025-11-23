# Stage 1: Builder - Install dependencies
FROM python:3.12-slim AS builder

# Install uv package manager
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies using uv
# --no-dev excludes development dependencies
# --frozen ensures we use exact versions from uv.lock
RUN uv sync --frozen --no-dev --no-install-project

# Stage 2: Runtime - Create final minimal image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy Python dependencies from builder stage
COPY --from=builder /app/.venv /app/.venv

# Copy application files
COPY main.py bot.py commands.py events.py ./

# Create non-root user for security
RUN useradd -m -u 1000 botuser && \
    chown -R botuser:botuser /app

# Switch to non-root user
USER botuser

# Add virtual environment to PATH
ENV PATH="/app/.venv/bin:$PATH"

# Set Python to run in unbuffered mode (recommended for Docker)
ENV PYTHONUNBUFFERED=1

# Health check: verify the bot process is running
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD pgrep -f "python main.py" || exit 1

# Run the bot
CMD ["python", "main.py"]
