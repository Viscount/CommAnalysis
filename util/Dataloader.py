#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os
import logging
from entity.Record import Record
from util import constants
import util.FileUtil as file_util

__author__ = 'Liao Zhenyu'


def read_record_from_file(file_path, lines=0):
    records = []
    if lines == 0:
        with codecs.open(file_path, "r") as f:
            for line in f.xreadlines():
                record_args = line.strip().split("\t")
                record = Record(record_args)
                records.append(record)
        return records
    else:
        with codecs.open(file_path, "r") as f:
            current_index = 0
            while current_index < lines:
                line = f.readline()
                record_args = line.strip().split("\t")
                record = Record(record_args)
                records.append(record)
                current_index += 1
        return records


def file_split(file_path):
    with codecs.open(file_path, "r") as f:
        current_index = None
        for line in f.xreadlines():
            record_args = line.strip().split("\t")
            date_index = record_args[0]
            if current_index != date_index:
                if current_index is not None:
                    file.close()
                logging.info("Generating file " + date_index)
                current_index = date_index
                file = open(get_part_data_file_prefix(date_index[6:8]), "w")
                file.writelines(line)
            else:
                file.writelines(line)
        file.close()


def get_data_file_path():
    return os.path.join(file_util.FileUtil.get_local_data_dir(), constants.DATA_FILE_NAME)


def get_part_data_file_prefix(index):
    if index < 10:
        index_str = "0" + str(index)
    else:
        index_str = str(index)
    return os.path.join(file_util.FileUtil.get_local_data_dir(), constants.DATA_PART_FILE_NAME_PREFIX
                        + index_str + ".txt")

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    # file_split(get_data_file_path())
    records = read_record_from_file(get_part_data_file_prefix(1))
    print len(records)
