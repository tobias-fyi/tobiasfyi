# === EC2 === #

# Pull base image
FROM python:3.8.0-slim-buster
LABEL maintainer="hi@tobias.fyi"

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create directory for app user
RUN mkdir -p /home/app
# Set up app directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir ${APP_HOME}
RUN mkdir ${APP_HOME}/static
RUN mkdir ${APP_HOME}/media
# Set working directory
WORKDIR ${APP_HOME}

# Create the app user
RUN addgroup --system wagtail && \
    adduser --system --no-create-home --group wagtail

# Install psycopg2 dependencies
RUN apt-get update && \
    apt-get upgrade -y gcc libpq-dev && \
    apt-get clean
# Install Python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt ${APP_HOME}
RUN pip install -r ${APP_HOME}/requirements.txt

# Copy entrypoint script
COPY ./entrypoint.dev.sh ${APP_HOME}

# Copy project
COPY . ${APP_HOME}

# chown all the files to the app user
RUN chown -R wagtail:wagtail $APP_HOME && chmod -R 755 $APP_HOME

# Change to non-root user
USER wagtail

# Expose port
EXPOSE 8000

# Run the gunicorn server
CMD gunicorn tobiasfyi.wsgi:application --bind 0.0.0.0:8000 --workers 3
