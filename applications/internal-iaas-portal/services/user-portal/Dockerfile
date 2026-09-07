ARG NGINX_IMAGE=nginxinc/nginx-unprivileged:1.27-alpine
FROM ${NGINX_IMAGE}
COPY services/user-portal/nginx.conf /etc/nginx/conf.d/default.conf
COPY services/user-portal/index.html /usr/share/nginx/html/index.html
COPY services/user-portal/assets /usr/share/nginx/html/assets
USER 101:101
EXPOSE 8080
