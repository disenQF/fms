#!/bin/bash

cd /usr/src
echo "服务器已启动"
gunicorn -w 1 -b 127.0.0.1:8000 fms.wsgi:application
