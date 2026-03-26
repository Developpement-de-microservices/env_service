FROM python:3.11.15-trixie

RUN apt-get update && apt-get upgrade -y && apt-get install -y curl && apt-get clean

WORKDIR /app

COPY /app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/app.py .
COPY ./data/envs.json /app/data


EXPOSE 5002

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 CMD curl -f http://localhost:5002/environments || exit 1

CMD ["python", "app.py"]
