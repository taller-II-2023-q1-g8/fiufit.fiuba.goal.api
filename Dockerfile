FROM python:3.12.0a7-bullseye
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

#uvicorn main:app --host 0.0.0.0 --port 8000 --reload