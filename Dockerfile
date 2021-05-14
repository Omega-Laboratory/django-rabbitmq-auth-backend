FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

#RUN apt-get update \
#    && apt-get install -y --no-install-recommends gcc and-build-dependencies
RUN pip install django       
RUN pip install pyjwt==1.7.1 cryptography python-decouple==3.1 numpy==1.19.1

COPY . /code

EXPOSE 8000
RUN chmod u+x /code/start.sh
ENTRYPOINT ["/code/start.sh"]
