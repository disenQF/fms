#!/usr/bin/python3
# coding: utf-8
from redis import Redis


# decode_responses响应的字节数据直接解码
# 如： b'123'.decode()
rd = Redis('47.105.137.19', db=3, decode_responses=True)

file_types = (
    (0, '目录'),
    (1, '图片'),
    (2, '文本'),
    (3, 'pdf'),
    (4, 'word'),
    (5, 'excel'),
    (6, '压缩包'),
    (7, '其它'),
)