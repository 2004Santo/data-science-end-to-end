
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . ./starter
WORKDIR /app/starter

CMD ["python3", "corregir_fuga.py"]
