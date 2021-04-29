FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /Django_Blog
COPY . .
RUN pip3 install -r requirements.txt
