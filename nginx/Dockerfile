# start from an official image
FROM nginx:latest

COPY local.conf.template /etc/nginx/conf.d/local.conf.template

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["nginx", "-g", "daemon off;"]