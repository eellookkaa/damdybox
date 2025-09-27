FROM python:3.12-slim

WORKDIR /app
COPY . .

# Install system deps for building aiohttp
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
