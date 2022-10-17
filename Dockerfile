# This Dockerfile builds the React client and API together

# Build step #1: build the React front end
FROM node:16-alpine as build-step
WORKDIR /app   
ENV PATH /app/webapp/frontend/node_modules/.bin:$PATH
COPY webapp/frontend/package.json ./
COPY webapp/frontend/yarn.lock ./
COPY webapp/frontend/src ./src
COPY webapp/frontend/public ./public
RUN yarn install
RUN yarn build

# Build step #2: build the API with the client as static files
FROM python:3.10-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY --from=build-step /app/build ./build

RUN mkdir ./backend
COPY requirements.txt webapp/backend/application.py webapp/backend/.flaskenv ./backend
RUN pip install --upgrade pip \
 && pip install -r ./backend/requirements.txt
ENV FLASK_DEBUG production

EXPOSE 3000
WORKDIR /app/backend
CMD ["gunicorn", "-b", ":3000", "application:app"]