FROM python:3.6.5-slim-stretch

WORKDIR /usr/src/app

COPY ./d20bot .

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "d20.py"]
