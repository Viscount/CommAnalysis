#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
import os
import numpy as np
from util import constants, Dataloader, FeatureUtil, FileUtil, DataUtil


__author__ = 'Liao Zhenyu'


def str_vector(vector):
    vector_list = vector.tolist()
    string = "["
    for item in vector_list:
        string = string + str(item) + ","
    string += "]"
    return string


def dump_matrix(index, matrix):
    logging.info("Dump matrix" + str(index) + " into text file...")
    matrix_file_name = "matrix"+str(index)+".txt"
    with open(os.path.join(FileUtil.FileUtil.get_local_dump_dir(), matrix_file_name), mode="w") as f:
        np.savetxt(f, matrix, fmt='%.2f', newline='\n')


def single_value_analysis(user_set):
    logging.info("Starting Single-value analysis.")
    user_num = len(user_set)
    cmatrix = np.zeros((user_num, constants.TOTAL_DAY_NUM))
    for day_index in range(constants.TOTAL_DAY_NUM):
        logging.info("Calculate feature in day " + str(day_index + 1))
        file_path = Dataloader.get_part_data_file_prefix(day_index+1)
        all_records = Dataloader.read_record_from_file(file_path)
        all_features = FeatureUtil.get_user_features(user_set, all_records, "call_count_single")
        for user in user_set:
            user_index = user_set[user]
            cmatrix[user_index, day_index] = all_features[user]
    dump_matrix(999, cmatrix)
    # 生成相似度矩阵
    matrix_index = 0
    for day_index in range(constants.WINDOW_SIZE-1, constants.TOTAL_DAY_NUM):
        sim_matrix = np.zeros((user_num, user_num))
        start_index = day_index-constants.WINDOW_SIZE+1
        logging.info("Generating matrix " + str(matrix_index) +
                     " from day " + str(start_index + 1) +
                     " to day " + str(day_index+1))
        for user in user_set:
            user_index = user_set[user]
            user_feature_vector = cmatrix[user_index, start_index:day_index+1]
            for user_comp in user_set:
                user_comp_index = user_set[user_comp]
                user_comp_feature_vector = cmatrix[user_comp_index, start_index:day_index+1]
                r = FeatureUtil.pearsonr_sim(user_feature_vector, user_comp_feature_vector)
                sim_matrix[user_index, user_comp_index] = abs(r)
                sim_matrix[user_comp_index, user_index] = abs(r)
        dump_matrix(matrix_index, sim_matrix)
        matrix_index += 1


def detail_value_analysis(user_set):
    logging.info("Starting detail-value analysis.")
    user_num = len(user_set)
    for day_index in range(constants.TOTAL_DAY_NUM):
        logging.info("Calculate feature in day " + str(day_index + 1))
        file_path = Dataloader.get_part_data_file_prefix(day_index + 1)
        all_records = Dataloader.read_record_from_file(file_path)
        all_features = FeatureUtil.get_user_features(user_set, all_records, "call_count_detail")
        # 生成相似度矩阵
        logging.info("Generating matrix " + str(day_index) +
                     " for day " + str(day_index + 1))
        sim_matrix = np.zeros((user_num, user_num))
        for user in user_set:
            user_index = user_set[user]
            user_feature_vector = all_features[user]
            for user_comp in user_set:
                user_comp_index = user_set[user_comp]
                user_comp_feature_vector = all_features[user_comp]
                r = FeatureUtil.pearsonr_sim(user_feature_vector, user_comp_feature_vector)
                sim_matrix[user_index, user_comp_index] = abs(r)
                sim_matrix[user_comp_index, user_index] = abs(r)
        dump_matrix(day_index, sim_matrix)


def detail_value_analysis_aggregative(user_set):
    logging.info("Starting detail-value-aggregative analysis.")
    user_num = len(user_set)
    feature_window = []
    for day_index in range(constants.TOTAL_DAY_NUM):
        logging.info("Calculate feature in day " + str(day_index + 1))
        file_path = Dataloader.get_part_data_file_prefix(day_index + 1)
        all_records = Dataloader.read_record_from_file(file_path)
        all_features = FeatureUtil.get_user_features(user_set, all_records, "call_count_detail_aggregative")
        feature_window.append(all_features)
        # 生成相似度矩阵
        if len(feature_window) == 3:
            logging.info("Generating matrix " + str(day_index-2) +
                         " from day " + str(day_index-1) +
                         " to day " + str(day_index+1))
            all_features = FeatureUtil.combine_user_feature(feature_window, "call_count_detail_aggregative")
            sim_matrix = np.zeros((user_num, user_num))
            for user in user_set:
                user_index = user_set[user]
                user_feature_vector = all_features[user]
                for user_comp in user_set:
                    user_comp_index = user_set[user_comp]
                    user_comp_feature_vector = all_features[user_comp]
                    r = FeatureUtil.pearsonr_sim(user_feature_vector, user_comp_feature_vector)
                    sim_matrix[user_index, user_comp_index] = abs(r)
                    sim_matrix[user_comp_index, user_index] = abs(r)
            dump_matrix(day_index-2, sim_matrix)
            feature_window.pop(0)


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    # single-value analysis process
    user_set = DataUtil.extract_user_selective(DataUtil.extract_all_users_from_list(), constants.SELECTIVE_NUM)
    single_value_analysis(user_set)
    # detail-value analysis process
    # detail_value_analysis(user_set)
    # detail_value_aggregative_analysis process
    # detail_value_analysis_aggregative(user_set)
