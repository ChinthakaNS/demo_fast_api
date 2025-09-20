# # ---------- Stage 1: Build dependencies ----------
# FROM python:3.11-slim as builder
# WORKDIR /app
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # ---------- Stage 2: Final image ----------
# FROM python:3.11-slim
# WORKDIR /app

# # Copy installed dependencies
# COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
# COPY --from=builder /usr/local/bin /usr/local/bin

# # Copy project files
# COPY . .

# # Expose port
# EXPOSE 8000

# # Run with Gunicorn + Uvicorn workers
# CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app", "-b", "0.0.0.0:8000", "--workers=2", "--timeout=120"]

# ---------- Stage 1: Build dependencies ----------


    # ---------- Stage 1: Build dependencies ----------
FROM python:3.11-slim AS builder
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---------- Stage 2: Final image ----------
FROM python:3.11-slim
WORKDIR /app

# Copy installed dependencies
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Run with Gunicorn + Uvicorn workers
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app", "-b", "0.0.0.0:8000", "--workers=2", "--timeout=120"]
