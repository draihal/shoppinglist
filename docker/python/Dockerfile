FROM python:3.6
MAINTAINER draihal

COPY . /code

WORKDIR /code

RUN pip install -r requirements.txt

COPY ./docker/python/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]