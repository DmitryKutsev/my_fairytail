# syntax=docker/dockerfile:1
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=my_fairy_tale.settings \
    DJANGO_DEBUG=1 \
    PYTHONPATH=/app

CMD ["gunicorn", "my_fairy_tale.wsgi:application", "--bind", "0.0.0.0:8000"]
