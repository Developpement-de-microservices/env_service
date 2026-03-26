FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir data

COPY ./app.py /app
COPY ../data/env.json /app/data


EXPOSE 5002

CMD ["python", "app.py"]
