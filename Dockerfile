FROM python:3.9-alpine

RUN mkdir -p /home/gtm_demo
RUN addgroup -S gtm_demo && adduser -S gtm_demo -G gtm_demo

ARG APP_HOME=/home/gtm_demo/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
WORKDIR $APP_HOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk del build-deps \
    && apk --no-cache add musl-dev linux-headers g++

RUN pip install --upgrade pip
COPY ./gtm_demo_web $APP_HOME
COPY ./requirements.prod.txt $APP_HOME
RUN pip install -r requirements.prod.txt

COPY ./deploy/entrypoint.prod.sh $APP_HOME
RUN chmod +x $APP_HOME/entrypoint.prod.sh

RUN chown -R gtm_demo:gtm_demo $APP_HOME

USER gtm_demo

ENTRYPOINT ["/home/gtm_demo/web/entrypoint.prod.sh"]