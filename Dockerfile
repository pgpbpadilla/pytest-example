FROM python:3.6-alpine

RUN mkdir -p /app/src
WORKDIR /app/src

COPY requirements.txt /app/src
RUN pip install -r requirements.txt

COPY . /app/src

CMD ["python", "main.py"]
