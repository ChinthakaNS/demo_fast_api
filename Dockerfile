# ---------- Stage 1: Build dependencies ----------
FROM python:3.13-slim AS builder
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---------- Stage 2: Final image ----------
FROM python:3.13-slim
WORKDIR /app

# Copy installed dependencies
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Build argument for debug mode
ARG DEBUG_MODE=false

# Copy project files only if not in debug mode
RUN if [ "$DEBUG_MODE" != true ]; then \
        cp -r demo_fast_api/ ./demo_fast_api/ ; \
    fi

# Expose port
EXPOSE 8000

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "demo_fast_api.main:app", "-b", "0.0.0.0:8000", "--workers=2", "--timeout=120"]