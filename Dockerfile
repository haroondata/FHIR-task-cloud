FROM python:3.11-slim

WORKDIR /app

# Copy requirements early for layer caching
COPY requirements.txt .

#  Install all required system packages
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# ✅ Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Run the app
CMD ["python", "main.py"]
