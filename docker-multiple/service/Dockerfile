FROM tiangolo/uvicorn-gunicorn-fastapi:latest

RUN python3 -m pip install requests

COPY app.py .

CMD ["python3", "-u", "app.py", "--port", "5005"]
