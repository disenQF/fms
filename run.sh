#!/bin/bash

cd /usr/src
echo "服务器已启动"
gunicorn -w 1 -b 0.0.0.0:8000 fms.wsgi:application
