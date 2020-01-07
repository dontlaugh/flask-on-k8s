FROM python:3.7-stretch

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt \
    && useradd app \
    && chown -R app:app /app

USER app

CMD ["python", "app.py"]