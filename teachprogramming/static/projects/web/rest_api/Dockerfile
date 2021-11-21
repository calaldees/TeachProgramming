FROM python:alpine

WORKDIR /app/

RUN pip install falcon gunicorn

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0", "falcon_api:app"]