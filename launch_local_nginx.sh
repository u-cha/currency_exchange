#!/bin/bash

docker rm -f currency-exchange-front-nginx
docker container run -d --name currency-exchange-front-nginx -p 3333:80 -v $(pwd):/usr/share/nginx/html nginx