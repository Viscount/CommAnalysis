#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
import numpy as np
from util import constants, Dataloader, FeatureUtil


__author__ = 'Liao Zhenyu'


def single_value_analysis(user_set):
    user_num = len(user_set)
    cmatrix = np.zeros((user_num, constants.TOTAL_DAY_NUM))
    for day_index in range(constants.TOTAL_DAY_NUM):
        file_path = Dataloader.get_part_data_file_prefix(day_index+1)
        for user in user_set:
            user_index = user_set[user]
            cmatrix[user_index, day_index] = FeatureUtil.get_user_feature(user, file_path, "call_count_single")


def detail_value_analysis(user_set):
    user_num = len(user_set)
    pass


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
