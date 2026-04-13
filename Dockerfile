FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# Expose port
EXPOSE 7860

# Command to run the app with gunicorn
CMD ["gunicorn", "app_updated:app", "--bind", "0.0.0.0:7860"]
