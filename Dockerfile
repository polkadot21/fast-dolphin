# Use the official Python base image as the foundation
FROM python:3.8-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
RUN mkdir /app
WORKDIR /app

# Install system dependencies
RUN apt-get update -y && \
    apt-get install -y build-essential libssl-dev libffi-dev python3-dev gcc

# Copy the requirements.txt file and install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application code and files
COPY . /app/

ENV BACKEND_URL=$BACKEND_URL
ENV VERSION=$VERSION

# Expose the port that the FastAPI app runs on
EXPOSE 5050

# Run the FastAPI app
CMD bash -c "env > /app/.env && exec uvicorn main:app --host 0.0.0.0 --port 5050"