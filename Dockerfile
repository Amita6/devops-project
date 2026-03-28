FROM python:3.9-slim
WORKDIR /app
COPY app/ /app/
RUN pip install Flask prometheus_client
CMD ["python", "app.py"]