FROM python:3.10.12-alpine
WORKDIR /app
COPY ./src ./src
COPY ./main.py ./main.py
COPY ./requirements.txt ./requirements.txt
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt
ENV PATH="/app/src:${PATH}"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]