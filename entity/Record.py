#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'Liao Zhenyu'


class Record(object):

    # 构造函数，从参数数组构造通话记录
    def __init__(self, args):
        # 时间ID
        self.day_id = args[0]
        # 主叫号码
        self.calling_num = args[1]
        # 被叫号码
        self.called_num = args[2]
        # 主叫运营商
        self.calling_op = args[3]
        # 被叫运营商
        self.called_op = args[4]
        # 主叫号码归属地
        self.calling_city = args[5]
        # 被叫号码归属地
        self.called_city = args[6]
        # 主叫号码漫游地
        self.calling_roam_city = args[7]
        # 被叫号码漫游地
        self.called_roam_city = args[8]
        # 通话开始时间
        self.start_time = args[9]
        # 通话结束时间
        self.end_time = args[10]
        # 通话时长
        self.raw_dur = args[11]
        # 通话类型 1 市话 2 长途 3 漫游
        self.call_type = args[12]
        # 主叫蜂窝号码
        self.call_cell = args[13]
