#!/usr/bin/env python
# -*- coding: utf-8 -*-

from CallCountSingle import CallCountSingle
from CallTimeSingle import CallTimeSingle
from CallCountDetail import CallCountDetail
from CallTimeDetail import CallTimeDetail

__author__ = 'Liao Zhenyu'


def get_feature_updater(method_name):
    updater_dict = dict(call_count_single=CallCountSingle,
                        call_time_single=CallTimeSingle,
                        call_count_detail=CallCountDetail,
                        call_time_detail=CallTimeDetail)
    return updater_dict[method_name]


if __name__ == "__main__":
    updater = get_feature_updater("call_count_single")
    updater.update()
    updater.create()
