FROM python:3.14-alpine3.23

LABEL description="Microservice for the management of environments."
LABEL service="env_service"

RUN apk add --no-cache curl

WORKDIR /app

COPY /app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/app.py .


EXPOSE 5002

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 CMD curl -f http://localhost:5002/environments/health || exit 1

CMD ["python", "app.py"]
