#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import os

"""
文件存取的操作
"""

__author__ = "htwxujian@gmail.com"


class FileUtil(object):
    # 如果路径存在，并且是一个文件夹，那么返回true；否则返回false。
    @staticmethod
    def is_dir_exists(dir_path):
        if os.path.isdir(dir_path):
            return True
        else:
            return False

    # 如果路径存在，并且是一个文件，那么返回true；否则返回false。
    @staticmethod
    def is_file_exists(file_path):
        if os.path.isfile(file_path):
            return True
        else:
            return False

    # 如果文件夹不存在，那么创建该文件夹，路径链中的文件夹若不存在也将会一同被创建。
    @staticmethod
    def create_dir_if_not_exist(dir_path):
        if FileUtil.is_dir_exists(dir_path) is False:
            os.makedirs(dir_path)

    # 获得当前脚本的运行目录。
    @staticmethod
    def _get_cur_dir():
        return os.path.dirname(os.path.realpath(__file__))

    # 获得项目的根路径。
    @staticmethod
    def get_project_root_path():
        (project_root_path, util_path) = os.path.split(FileUtil._get_cur_dir())
        return project_root_path

    # 获得本地数据目录。
    @staticmethod
    def get_local_data_dir():
        base_path = FileUtil.get_project_root_path()
        local_data_path = os.path.join(base_path, "data")
        FileUtil.create_dir_if_not_exist(local_data_path)
        return local_data_path

        # 分块读取文件的内容。

    @staticmethod
    def __read_file_by_block(input_file, buffer_size=65536):
        while True:
            nb = input_file.read(buffer_size)
            if not nb:
                break
            yield nb

    # 获得当前文件的总行数。
    @staticmethod
    def get_file_line_count(file_path):
        if not FileUtil.is_file_exists(file_path):
            return False
        with open(file_path, "rb") as input_file:
            # 返回一个迭代器，对迭代器中的数据汇总。
            return sum(line.count("\n") for line in FileUtil.__read_file_by_block(input_file))

if __name__ == "__main__":
    print FileUtil.get_project_root_path()
    print FileUtil.get_local_data_dir()
