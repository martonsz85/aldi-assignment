FROM python:3-slim

WORKDIR /app

# Copy only the application code
COPY app/main.py /app/

# Install FastAPI + Uvicorn
RUN pip install fastapi uvicorn

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
