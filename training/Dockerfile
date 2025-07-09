FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install uv 
RUN pip install --upgrade pip && pip install uv

# Set work directory
WORKDIR /app

# Copy only requirements first for caching
COPY pyproject.toml ./

# Copy the rest of the code
COPY . .

# Set the entrypoint to run main.py
CMD ["uv","run","python", "main.py"]