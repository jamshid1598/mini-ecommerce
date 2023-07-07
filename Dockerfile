# syntax=docker/dockerfile:1


FROM python:3.10.9-slim-buster

WORKDIR /backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements.txt
COPY requirements.txt /backend/requirements.txt

# upgrade pip and install dependencies
RUN python3 -m pip install --upgrade setuptools
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r /backend/requirements.txt

# copy project
COPY . /backend/

RUN sed -i 's/\r$//g' /backend/entrypoint.sh
RUN chmod +x /backend/entrypoint.sh

ENTRYPOINT [ "/backend/entrypoint.sh" ]
