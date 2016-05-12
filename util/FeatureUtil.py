#!/usr/bin/env python
# -*- coding: utf-8 -*-
from util import DataUtil, Dataloader

__author__ = 'Liao Zhenyu'


def get_single_value_feature_call_count(user_num, file_path):
    records = DataUtil.extract_user_records(user_num, file_path)
    return len(records)


def get_single_value_feature_call_time(user_num, file_path):
    records = DataUtil.extract_user_records(user_num, file_path)
    call_time = 0
    for record in records:
        call_time += int(record.raw_dur)
    return call_time


def get_user_feature(user_num, file_path, feature_name):
    if feature_name == "call_count_single":
        return get_single_value_feature_call_count(user_num, file_path)
    elif feature_name == "call_time_single":
        return get_single_value_feature_call_time(user_num, file_path)


if __name__ == "__main__":
    file_path = Dataloader.get_part_data_file_prefix("20120201")
    callingDay1 = DataUtil.extract_all_users(file_path)
    print len(callingDay1)
    test_key = callingDay1.keys()[2]
    print get_single_value_feature_call_count(test_key, file_path)
    print get_single_value_feature_call_time(test_key, file_path)
