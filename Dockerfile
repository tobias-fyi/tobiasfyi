# Use an official Python runtime as a parent image
FROM python:3.8.0-slim-buster
LABEL maintainer="tobyreaper@gmail.com"

# Set the working directory to /usr/src/app/
WORKDIR /usr/src/app/

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install -r /usr/src/app/requirements.txt
RUN pip install gunicorn

# Copy the current directory contents into the container at /usr/src/app/
COPY . /usr/src/app/

RUN useradd wagtail
RUN chown -R wagtail /usr/src/app
USER wagtail
