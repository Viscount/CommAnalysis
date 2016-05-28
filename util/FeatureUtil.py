#!/usr/bin/env python
# -*- coding: utf-8 -*-
from util import DataUtil, Dataloader, constants
from scipy.stats.stats import pearsonr
import FeatureUpdater
import math

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
    vector_dict = dict()
    for user in user_dict:
        if user in feature_dict:
            vector_dict[user] = feature_updater.finish(feature_dict[user])
        else:
            vector_dict[user] = feature_updater.zero()
    return vector_dict


def combine_user_feature(feature_window, feature_name):
    feature_updater = FeatureUpdater.get_feature_updater(feature_name)
    return feature_updater.combine(feature_window)


def is_zero_feature(feature_vector):
    for value in feature_vector:
        if value != 0:
            return False
    return True


def pearsonr_sim(user_feature_vector, user_comp_feature_vector):
    flag_user = is_zero_feature(user_feature_vector)
    flag_user_comp = is_zero_feature(user_comp_feature_vector)
    if flag_user | flag_user_comp:
        if flag_user == flag_user_comp:
            return 1.0
        else:
            return 0.0
    r, p_value = pearsonr(user_feature_vector, user_comp_feature_vector)
    if math.isnan(r):
        r = 0.0
    return r


if __name__ == "__main__":
    file_path = Dataloader.get_part_data_file_prefix(1)
    callingDay1 = DataUtil.extract_all_users(file_path)
    all_records = Dataloader.read_record_from_file(file_path)
    print len(callingDay1)
    test_dict = dict()
    test_dict[callingDay1.keys()[0]] = callingDay1[callingDay1.keys()[0]]

