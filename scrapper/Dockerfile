FROM python:3.9.17-alpine3.18

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt
COPY ./scrap.py .

CMD ["python", "scrap.py"]
