FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=receiver.py
ENV PYTHONUNBUFFERED=1

CMD ["python", "receiver.py"]
