FROM python:3

WORKDIR /app

RUN mkdir app

COPY . /app

RUN apt-get -y update
RUN pip3 install -r requirements.txt

EXPOSE 5000

#Run the command
CMD [“python3”, “./app/server.py”]