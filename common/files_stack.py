#!/usr/bin/python3
# coding: utf-8
import random

from . import rd


def add_file_stack(file_id, file_name):
    v = ','.join([str(file_id), file_name])
    is_finded = False
    # 查询当前的v 是否存在，如果存在，则删除其后的value
    for i, pre_v in enumerate(rd.lrange('pre_file_id', 0, -1)):
        if v == pre_v:
            is_finded = True
            rd.ltrim('pre_file_id', 0, i)

    if not is_finded:  # 如果未找到，则压入回退栈中
        rd.rpush('pre_file_id', v)


def pop_file_stack():
    _ = rd.rpop('pre_file_id')
    file_id, filename = rd.rpop('pre_file_id').split(',')
    return file_id, filename


def get_pre_file_stack():
    return [tuple(x.split(',')) for x in rd.lrange('pre_file_id', 0, -1)]


def clear_pre_file_stack():
    rd.delete('pre_file_id')

