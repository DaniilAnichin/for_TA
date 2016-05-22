#!usr/bin/python
# -*- coding: utf-8 -*-#
from math import log


def merge_sort(num_list):
    half_len = len(num_list) / 2
    if len(num_list) > 2:
        return merge(merge_sort(num_list[:half_len]),
                     merge_sort(num_list[half_len:]))
    elif len(num_list) == 2:
        return merge(num_list[:1], num_list[1:])
    else:
        return num_list


def merge(list_a, list_b):
    result_list = []
    for i in range(len(list_a) + len(list_b)):
        if len(list_a) == 0:
            result_list.append(list_b.pop(0))
        elif len(list_b) == 0:
            result_list.append(list_a.pop(0))
        elif list_a[0] < list_b[0]:
            result_list.append(list_a.pop(0))
        else:
            result_list.append(list_b.pop(0))
    return result_list


if __name__ == '__main__':
    print merge_sort([1, 5, 6, 2, 7, 1, 8, 5, 3])
