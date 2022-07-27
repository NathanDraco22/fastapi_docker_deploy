FROM python:alpine

RUN mkdir -p /home/app

COPY . home/app

WORKDIR /home/app

EXPOSE 80

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]