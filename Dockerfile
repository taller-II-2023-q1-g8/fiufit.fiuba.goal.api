FROM python:3.10.12-bullseye
# FROM goals_and_metrics_microservices_microservice:latest
WORKDIR /app

COPY . /app
RUN pip3 install --upgrade pip
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY src /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

#uvicorn main:app --host 0.0.0.0 --port 8000 --reload