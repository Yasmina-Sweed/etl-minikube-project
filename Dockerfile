FROM python:3.10-slim
WORKDIR /app
COPY etl.py .
RUN pip install pandas psycopg2-binary sqlalchemy
CMD ["python", "etl.py"]

