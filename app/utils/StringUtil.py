#coding=utf-8
'''
Created on 2015年6月16日

@author: atool
'''
import os
import time
import datetime
import random

def is_empty(s):
    if s == None or s == '':
        return True
    return False


def get_unique_str():
    #随机的名字，可以用于上传文件等等不重复，但有一定时间意义的名字
    datetime_str = time.strftime('%Y%m%d%H%M%S',time.localtime())
    return datetime_str + str(datetime.datetime.now().microsecond / 1000) + str(random.randint(0, 1000))


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)