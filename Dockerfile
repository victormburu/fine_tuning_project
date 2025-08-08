# Use a non-root user
FROM python:3.9-slim

# Set environment variables
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port for Streamlit
EXPOSE 8501
CMD ["python", "scheduler.py"]