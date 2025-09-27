FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies for aiohttp + other packages
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libffi-dev \
    libssl-dev \
    python3-dev \
    cargo \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (to cache deps layer)
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port (change if needed)
EXPOSE 8000

# Start app (adjust entrypoint if not main.py)
CMD ["python", "main.py"]
