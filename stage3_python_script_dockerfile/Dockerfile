FROM python:3.13-slim

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy updated Python script
COPY script.py .

# Set entrypoint to run the script
ENTRYPOINT ["python", "script.py"]

# Default arguments (optional)
CMD ["--mode", "hello", "--api-url", "http://localhost", "--local-file", "hello.txt"]

