FROM python:3.11-slim

LABEL description="Microservice Flask pour gérer les environnement" 
LABEL service="evironnement_service"

WORKDIR /app

COPY /app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir data

COPY app/app.py .
COPY ./data/envs.json /app/data


EXPOSE 5002

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 CMD curl -f http://localhost:5004/events || exit 1

CMD ["python", "app.py"]
