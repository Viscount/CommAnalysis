#!/usr/bin/env python
# -*- coding: utf-8 -*-
from util import constants
import numpy as np


__author__ = 'Liao Zhenyu'


class CallCountDetailAggregative:

    def __init__(self):
        return

    @staticmethod
    def update(old_value, current_record):
        called_user_index = current_record.called_num
        if called_user_index in old_value:
            old_count = old_value[called_user_index]
            old_value[called_user_index] = old_count + 1
        else:
            old_value[called_user_index] = 1
        return old_value

    @staticmethod
    def create(current_record):
        called_user_dict = dict()
        called_user_dict[current_record.called_num] = 1
        return called_user_dict

    @staticmethod
    def finish(dict_value):
        return dict_value

    @staticmethod
    def combine(feature_window):
        feature_dict = dict()
        for features in feature_window:
            for user, feature in features.items():
                if user not in feature_dict:
                    feature_dict[user] = feature
                else:
                    old_feature = feature_dict[user]
                    feature_dict[user] = combine_feature_vectors(feature, old_feature)
        result_dict = dict()
        for user, feature in feature_dict.items():
            user_feature_vector = feature.values()
            while len(user_feature_vector) < constants.DETAIL_VALUE_DIM:
                user_feature_vector.append(0.0)
            user_feature_vector.sort(reverse=True)
            result_dict[user] = np.array(user_feature_vector[:constants.DETAIL_VALUE_DIM])
        return result_dict


def combine_feature_vectors(feature_vector1, feature_vector2):
    result_feature = dict(feature_vector1)
    for user, value in feature_vector2.items():
        if user in result_feature:
            old_value = result_feature[user]
            result_feature[user] = old_value + value
        else:
            result_feature[user] = value
    return result_feature