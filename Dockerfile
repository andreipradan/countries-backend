FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

RUN pip install -U pip
COPY requirements.txt /temp_requirements/
RUN pip install --no-cache-dir -r /temp_requirements/requirements.txt \
    && rm -rf /temp_requirements/

WORKDIR /app
COPY src .

CMD exec gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT --chdir=/app
