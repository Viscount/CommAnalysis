#!/usr/bin/env python
# -*- coding: utf-8 -*-
from util import DataUtil, Dataloader

__author__ = 'Liao Zhenyu'


def get_single_value_feature_call_count(user_set, all_records):
    feature_dict = dict()
    for record in all_records:
        user_key = record.calling_num
        if user_key in user_set:
            if user_key in feature_dict:
                last_count = feature_dict[user_key]
                feature_dict[user_key] = last_count + 1
            else:
                feature_dict[user_key] = 1
    return feature_dict


def get_single_value_feature_call_time(user_set, all_records):
    feature_dict = dict()
    for record in all_records:
        user_key = record.calling_num
        if user_key in user_set:
            if user_key in feature_dict:
                last_call_time = feature_dict[user_key]
                feature_dict[user_key] = last_call_time + int(record.raw_dur)
            else:
                feature_dict[user_key] = int(record.raw_dur)
    return feature_dict


def get_user_features(user_dict, all_records, feature_name):
    if feature_name == "call_count_single":
        return get_single_value_feature_call_count(user_dict, all_records)
    elif feature_name == "call_time_single":
        return get_single_value_feature_call_time(user_dict, all_records)


if __name__ == "__main__":
    file_path = Dataloader.get_part_data_file_prefix(1)
    callingDay1 = DataUtil.extract_all_users(file_path)
    all_records = Dataloader.read_record_from_file(file_path)
    print len(callingDay1)
    test_dict = dict()
    test_dict[callingDay1.keys()[0]] = callingDay1[callingDay1.keys()[0]]
    print len(get_single_value_feature_call_count(test_dict, all_records))
    print len(get_single_value_feature_call_time(test_dict, all_records))
