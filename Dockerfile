FROM python:alpine

RUN mkdir -p /home/app

COPY . home/app

WORKDIR /home/app

EXPOSE 80

RUN pip install --no-cache-dir --upgrade -r requirements.txt

# HEROKU VERSION
CMD uvicorn main:app --host 0.0.0.0 --port $PORT

#DIGITAL OCEAN 
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]