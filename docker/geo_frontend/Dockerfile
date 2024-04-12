FROM node:lts-alpine

WORKDIR app/

ADD ./geo_front/*.json ./

RUN npm config set registry=http://registry.npmjs.org
RUN npm install

ADD ./geo_front/build ./build
ADD ./geo_front/public ./public
ADD ./geo_front/src ./src
