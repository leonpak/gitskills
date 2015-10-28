#!/usr/bin/env python3

"""main.python3
小型日志记录管理系统 by siyuany """

import os
from datetime import datetime

# File to store logs
# 文件存储在本模块所在目录下
FILE = os.path.join(os.getcwd(), 'log.dat')

# Record format: [date time]content.
# Example:
# [2015-10-23 10:23:26]人生苦短, Python是岸
# DATETIME_FORMAT
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def store_log_to_file(content):
    ts = datetime.now().strftime(DATETIME_FORMAT)
    content = str(content)
    log = "[%s]%s\n" % (ts, content)
    with open(FILE, 'a') as log_file:
        log_file.write(log)


# 死循环,Ctrl+D结束循环
def add_record():
    while True:
        try:
            content = input('\n> ')
            store_log_to_file(content)
        except EOFError or KeyboardInterrupt:
            print('\n')
            break


# 读取日志
def list_records():
    with open(FILE, 'r') as log_file:
        logs = log_file.readlines()
        for log in logs:
            print(log)


def main():
    help_msg = """
帮助:
    add     进入日志模式,每条日志记录一行,输入Ctrl+D退出
    list    列出所有日志
    quit    退出程序
    """
    print(help_msg)
    while True:
        command = input('add/list/quit: ')
        if command == 'add':
            add_record()
        elif command == 'list':
            list_records()
        elif command == 'quit':
            break
        else:
            print(help_msg)


if __name__ == '__main__':
    main()