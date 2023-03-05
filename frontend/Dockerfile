FROM node:14 as builder

WORKDIR /frontend

COPY . .

RUN yarn install \
  --prefer-offline \
  --frozen-lockfile \
  --non-interactive \
  --production=false

COPY ./package.json /usr/src/frontend/ 

RUN yarn build

RUN rm -rf node_modules && \
  NODE_ENV=production yarn install \
  --prefer-offline \
  --pure-lockfile \
  --non-interactive \
  --production=true

FROM node:14

WORKDIR /frontend

ENV HOST 0.0.0.0
EXPOSE 3000

CMD [ "yarn", "start" ]