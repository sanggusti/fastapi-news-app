FROM node:14.17.4-alpine as builder

COPY client ./

RUN yarn
RUN yarn build

FROM python:3.8 as deploy

EXPOSE 80

WORKDIR /app

COPY server ./server
COPY --from=builder build ./client/build

RUN python -mvenv .venv

RUN .venv/bin/pip install -rserver/requirements.txt

CMD .venv/bin/gunicorn server.app:app --bind 0.0.0.0:80 -k uvicorn.workers.UvicornWorker --log-level DEBUG