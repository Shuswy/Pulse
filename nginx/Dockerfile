FROM nginx:stable-alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY default.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /app/static /app/media

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]