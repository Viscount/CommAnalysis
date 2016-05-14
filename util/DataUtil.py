#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util import Dataloader, constants
import logging
import random

__author__ = 'Liao Zhenyu'


def extract_all_users(file_path):
    records = Dataloader.read_record_from_file(file_path)
    calling_user_dict = dict()
    calling_user_count = 0
    for record in records:
        if record.calling_num not in calling_user_dict:
            calling_user_dict[record.calling_num] = calling_user_count
            calling_user_count += 1
    return calling_user_dict


def get_default_file_path_list():
    file_path_list = []
    for day_index in range(constants.TOTAL_DAY_NUM):
        file_path_list.append(Dataloader.get_part_data_file_prefix(day_index + 1))
    return file_path_list


def extract_common_users(file_path_list=get_default_file_path_list()):
    common_users = set()
    first_dict_flag = True
    for file_path in file_path_list:
        logging.info("Loading file " + file_path + "...")
        calling_users = extract_all_users(file_path)
        calling_user_set = set(calling_users.keys())
        if first_dict_flag:
            common_users = calling_user_set.copy()
            first_dict_flag = False
        else:
            common_users = common_users.intersection(calling_user_set)
    common_user_dict = dict()
    user_count = 0
    for user in common_users:
        common_user_dict[user] = user_count
        user_count += 1
    return common_user_dict


def extract_user_records_from_file(user_num, file_path):
    records = Dataloader.read_record_from_file(file_path)
    user_records = []
    for record in records:
        if record.calling_num == user_num:
            user_records.append(record)
    return user_records


def extract_user_records(user_num, all_records):
    user_records = []
    for record in all_records:
        if record.calling_num == user_num:
            user_records.append(record)
    return user_records


def extract_all_records(file_path):
    return Dataloader.read_record_from_file(file_path)


def extract_user_selective(user_dict, num_of_select):
    if num_of_select >= len(user_dict):
        return user_dict
    elif num_of_select <= 0:
        empty_set = set()
        return empty_set
    else:
        random.seed(constants.RANDOM_SEED)
        selected = random.sample(user_dict, num_of_select)
        selective_user_dict = dict()
        user_count = 0
        for user in selected:
            selective_user_dict[user] = user_count
            user_count += 1
        return selective_user_dict


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    # file_path = Dataloader.get_part_data_file_prefix("20120201")
    # callingDay1 = extract_all_users(file_path)
    # print len(callingDay1)
    # test_key = callingDay1.keys()[2]
    # records = extract_user_records(test_key, file_path)
    # print len(records)

    # calling_dict = extract_common_users()
    # print len(calling_dict)

    test_user_set = dict()
    test_user_set["abcd"] = 1
    test_user_set["dcba"] = 2
    test_user_set["cbad"] = 3
    test_user_set["bcda"] = 4
    selective = extract_user_selective(test_user_set, 2)
    print len(selective)




