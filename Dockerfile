FROM python:3.8-alpine

WORKDIR /

COPY . .

RUN pip install flask

EXPOSE 5000

ADD "server.py" /

ENTRYPOINT ["python"]

CMD ["server.py"]