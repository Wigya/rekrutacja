FROM node:18.16

WORKDIR /client

COPY package.json .

RUN npm install

COPY . .

EXPOSE 8080

CMD ["npm", "start"]