FROM python:3.8-slim-buster

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # app folder
  && mkdir -p /backend \
  # pyhive utilities
  &&  apt-get install gcc\
  &&  apt-get install sasl2-bin libsasl2-2 libsasl2-dev libsasl2-modules\
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

COPY dvd/backend/requirements.txt /dvd/backend/
RUN pip install -r /dvd/backend/requirements.txt

COPY ./conf/backend/scripts/run.sh /run.sh
RUN sed -i 's/\r$//g' /run.sh
RUN chmod +x /run.sh

ENV \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8

WORKDIR /dvd/backend