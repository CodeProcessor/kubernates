FROM tiangolo/uvicorn-gunicorn-fastapi:latest

RUN apt-get update && apt-get install -y dnsutils

COPY app.py .

CMD ["python3", "-u", "app.py", "--port", "5004"]
