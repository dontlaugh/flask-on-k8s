FROM  python:3.8.1-alpine

WORKDIR /app
COPY . /app

RUN pip install gunicorn \
    && pip install -r requirements.txt \
    && addgroup -S app && adduser -S app \
    && chown -R app:app /app

USER app

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]

