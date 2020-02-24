#!/usr/bin/python3
# coding: utf-8
import random

from . import rd


def add_file_stack(user_id, file_id, file_name):
    v = ','.join([str(file_id), file_name])  # v = f'{file_id},{file_name}'
    is_finded = False
    # 查询当前的v 是否存在，如果存在，则删除其后的value
    for i, pre_v in enumerate(rd.lrange(f'pre_file_id_{user_id}', 0, -1)):
        if v == pre_v:
            is_finded = True
            rd.ltrim(f'pre_file_id_{user_id}', 0, i)  # 将后面的内容截断

    if not is_finded:  # 如果未找到，则压入回退栈中
        rd.rpush(f'pre_file_id_{user_id}', v)


def pop_file_stack(user_id):
    _ = rd.rpop(f'pre_file_id_{user_id}')
    file_id, filename = rd.rpop(f'pre_file_id_{user_id}').split(',')
    return file_id, filename


def get_pre_file_stack(user_id):
    return [tuple(x.split(',')) for x in rd.lrange(f'pre_file_id_{user_id}', 0, -1)]


def clear_pre_file_stack(user_id):
    rd.delete(f'pre_file_id_{user_id}')

