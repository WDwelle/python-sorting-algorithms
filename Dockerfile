FROM python:3

WORKDIR /app

RUN mkdir app

COPY . /app

RUN cd /app
RUN apt-get -y update
RUN pip3 install -r requirements.txt

EXPOSE 5000

#Run the command
ENTRYPOINT ["python3", "/app/server.py"]