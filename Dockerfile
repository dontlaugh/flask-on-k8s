FROM  python:3.8.1-alpine

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt \
    && addgroup -S app && adduser -S app \
    && chown -R app:app /app

USER app

CMD ["python", "app.py"]