#!/usr/bin/python3
# coding: utf-8

from . import file_types


def get_file_type(mime_type: str):
    if mime_type.startswith('image/'):
        return 1
    elif mime_type.startswith('text/'):
        return 2
    elif mime_type.endswith('.pdf'):
        return 3
    elif mime_type.endswith('.doc') or mime_type.endswith('.docx'):
        return 4
    elif mime_type.endswith('.xls') or mime_type.endswith('.xlsx'):
        return 5
    elif any((mime_type.endswith('.zip'),
              mime_type.endswith('.rar'),
              mime_type.endswith('.tar'),
              mime_type.endswith('.gz'),
              )):
        return 6
    else:
        return 7


def get_file_mime(file_type):
    if file_type == 1:
        return 'image/*'
    elif file_type == 2:
        return 'text/*'
    elif file_type == 3:
        return 'application/pdf'
    elif file_type == 4:
        return 'application/msword'
    elif file_type == 5:
        return 'application/vnd.ms-excel'
    else:
        return 'application/zip'
