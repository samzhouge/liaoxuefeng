# coding=utf-8
# 输入时间区间和日志级别

import re
from datetime import datetime


def to_timestamp(dt_str):
    return datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S').timestamp()

log_level = input('Input log level: ')
dt_start_str = input('Input start time: ')
dt_end_str = input('Input end time: ')

dt_start_timestamp = to_timestamp(dt_start_str)
dt_end_timestamp = to_timestamp(dt_end_str)

with open('log.txt', 'r', encoding='utf-8') as f:
    re_log = re.compile(r'^\[(\w+)\] (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+)+')
    for line in f.readlines():
        log_tunple = re_log.match(line).groups()
        if log_tunple[0] == log_level:
            dt_log_timestamp = to_timestamp(log_tunple[1])
            if dt_start_timestamp <= dt_log_timestamp <= dt_end_timestamp:
                print(log_tunple[1], log_tunple[2])