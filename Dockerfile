FROM python:3.11-slim

WORKDIR /app

# Copy requirements file first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy API source code
COPY cyndx_langgraph_api ./cyndx_langgraph_api

# Run FastAPI
CMD ["uvicorn", "cyndx_langgraph_api.main:app", "--host", "0.0.0.0", "--port", "8080"]
