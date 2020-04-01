# Use an official Python runtime as a parent image
FROM python:3.8.0-slim-buster
LABEL maintainer="tobyreaper@gmail.com"

# Install dependencies
RUN apt-get update && \
    apt-get upgrade -y gcc libpq-dev && \
    apt-get clean

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /usr/src/app/
# RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Add user
RUN addgroup --system wagtail && adduser --system --no-create-home --group wagtail
RUN chown -R wagtail:wagtail /usr/src/app && chmod -R 755 /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install -r /usr/src/app/requirements.txt

# Switch to non-root user
USER wagtail

# Copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# Copy the current directory contents into the container at /usr/src/app/
COPY . /usr/src/app/

# Run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
