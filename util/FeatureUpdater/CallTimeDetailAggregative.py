#!/usr/bin/env python
# -*- coding: utf-8 -*-
from util import constants
import numpy as np


__author__ = 'Liao Zhenyu'


class CallTimeDetailAggregative:

    def __init__(self):
        return

    @staticmethod
    def update(old_value, current_record):
        called_user_index = current_record.called_num
        if called_user_index in old_value:
            old_time = old_value[called_user_index]
            old_value[called_user_index] = old_time + current_record.raw_dur
        else:
            old_value[called_user_index] = current_record.raw_dur
        return old_value

    @staticmethod
    def create(current_record):
        called_user_dict = dict()
        called_user_dict[current_record.called_num] = current_record.raw_dur
        return called_user_dict

    @staticmethod
    def finish(dict_value):
        return dict_value
