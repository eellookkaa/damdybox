# Use Python 3.12 slim (official image)
FROM python:3.12-slim

# Prevent Python from writing .pyc files & enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip & install deps
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip wheel setuptools \
    && pip install -r requirements.txt

# Copy your source code
COPY . .

# Run with Gunicorn (recommended for Flask in production)
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
