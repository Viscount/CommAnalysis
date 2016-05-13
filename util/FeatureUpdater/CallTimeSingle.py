#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Liao Zhenyu'


class CallTimeSingle:

    def __init__(self):
        return

    @staticmethod
    def update(old_value, current_record):
        return old_value + current_record.raw_dur

    @staticmethod
    def create(current_record):
        return current_record.raw_dur
