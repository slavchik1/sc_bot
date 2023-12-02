# syntax=docker/dockerfile:1
FROM python:3.11-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY images images
COPY other_python_files other_python_files
COPY *.py .
CMD ["python3", "main.py"]
