FROM python:3.8-alpine

ENV TZ=America/Sao_Paulo

WORKDIR /code

#RUN apt-get update && apt install -y build-essential libpoppler-cpp-dev pkg-config python3-dev curl libpq-dev

COPY . /code

RUN pip install -r requirements.txt

CMD ["python3","app.py"]
