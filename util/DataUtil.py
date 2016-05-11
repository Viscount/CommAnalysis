#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util import Dataloader

__author__ = 'Liao Zhenyu'


def extract_users(file_path):
    records = Dataloader.read_record_from_file(file_path)
    calling_user_set = set()
    called_user_set = set()
    for record in records:
        if record.calling_num not in calling_user_set:
            calling_user_set.add(record.calling_num)
        if record.called_num not in called_user_set:
            called_user_set.add(record.called_num)
    return calling_user_set, called_user_set


if __name__ == "__main__":
    file_path = Dataloader.get_part_data_file_prefix("20120201")
    calling, called = extract_users(file_path)
    print len(calling)
    print len(called)
