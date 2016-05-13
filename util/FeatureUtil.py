#!/usr/bin/env python
# -*- coding: utf-8 -*-
from util import DataUtil, Dataloader, constants
import FeatureUpdater

__author__ = 'Liao Zhenyu'


def get_user_features(user_dict, all_records, feature_name):
    feature_dict = dict()
    feature_updater = FeatureUpdater.get_feature_updater(feature_name)
    for record in all_records:
        user_key = record.calling_num
        if user_key in user_dict:
            if user_key in feature_dict:
                feature_dict[user_key] = feature_updater.update(feature_dict[user_key], record)
            else:
                feature_dict[user_key] = feature_updater.create(record)
    return feature_dict


if __name__ == "__main__":
    file_path = Dataloader.get_part_data_file_prefix(1)
    callingDay1 = DataUtil.extract_all_users(file_path)
    all_records = Dataloader.read_record_from_file(file_path)
    print len(callingDay1)
    test_dict = dict()
    test_dict[callingDay1.keys()[0]] = callingDay1[callingDay1.keys()[0]]

