FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir data

COPY ./app.py /app
COPY ../data/users.json /app/data
COPY ../data/ssid.json /app/data
COPY ../data/ap.json /app/data


EXPOSE 5002

CMD ["python", "app.py"]
