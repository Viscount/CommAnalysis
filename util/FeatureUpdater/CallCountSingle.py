#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Liao Zhenyu'


class CallCountSingle:

    def __init__(self):
        return

    @staticmethod
    def update(old_value, current_record):
        return old_value+1

    @staticmethod
    def create(current_record):
        return 1

    @staticmethod
    def finish(dict_value):
        return dict_value
