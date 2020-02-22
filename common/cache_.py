#!/usr/bin/python3
# coding: utf-8
import random

from . import rd


def new_code(phone):
    code = set()
    while len(code) < 4:
        code.add(str(random.randint(1, 9)))

    code = ''.join(code)
    rd.set(phone, code, ex=120)  # 单位是秒
    return code

def get_code(phone):
    return rd.get(phone)
