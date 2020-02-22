#!/usr/bin/python3
# coding: utf-8
from redis import Redis


# decode_responses响应的字节数据直接解码
# 如： b'123'.decode()
rd = Redis('119.3.170.97', db=3, decode_responses=True)
