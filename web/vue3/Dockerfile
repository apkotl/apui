# web/vue3/Dockerfile
FROM node:20-alpine

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