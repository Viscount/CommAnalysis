#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os
from entity.Record import Record
from util import constants
import util.FileUtil as file_util

__author__ = 'Liao Zhenyu'


def read_record_from_file(file_path, lines):
    records = []
    with codecs.open(file_path, "rb") as f:
        current_index = 0
        while current_index < lines:
            line = f.readline()
            record_args = line.strip().split("\t")
            record = Record(record_args)
            records.append(record)
            current_index += 1
    return records

if __name__ == "__main__":
    file_path = os.path.join(file_util.FileUtil.get_local_data_dir(), constants.DATA_FILE_NAME)
    print file_util.FileUtil.get_file_line_count(file_path)
    records = read_record_from_file(file_path, 100)
    print len(records)
