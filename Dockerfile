FROM python:3-slim

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 5487

CMD ["python", "app.py"]