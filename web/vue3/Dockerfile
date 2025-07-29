# web/vue3/Dockerfile
FROM node:20-alpine

ARG ARG_ENVIRONMENT=unknown
#ENV ENVIRONMENT=$ARG_ENVIRONMENT

ARG ARG_VITE_API_URL=unknown
ARG ARG_VITE_APP_NAME=unknown
ARG ARG_VITE_DEBUG=unknown
ENV VITE_API_URL=$ARG_VITE_API_URL
ENV VITE_APP_NAME=$ARG_VITE_APP_NAME
ENV VITE_DEBUG=$ARG_VITE_DEBUG



WORKDIR /app




COPY ./app/package*.json ./
RUN npm install

COPY ./app .
#RUN npm run build


#CMD ["echo", "Vue.js build completed"]
ENTRYPOINT ["echo", "Vue.js build completed"]

#debug
#ENTRYPOINT [ "tail" ]
#CMD [ "-f", "/dev/null" ]