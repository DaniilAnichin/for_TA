#!/usr/bin/python
# -*- coding: utf-8 -*-#


def inversion_calc(like_list):
    # inversions = []
    inversion_number = 0
    for i in range(len(like_list) - 1):
        for j in range(i, len(like_list)):
            if like_list[j] < like_list[i]:
                inversion_number += 1
    return inversion_number
                # inversions.append((i, j))
    # return inversions


def inversion_recurcy(like_list):
    half_len = len(like_list) / 2
    first = like_list[:half_len]
    second = like_list[half_len:]
    if len(like_list) > 2:
        return inversion_recurcy(first) + inversion_recurcy(second) + \
            split_inversions(first, second)
    else:
        return split_inversions(first, second)


def split_inversions(first, second):
    inversion_number = 0
    for i in range(len(first) + len(second)):
        if len(second) == 0:
            return inversion_number
        elif len(first) == 0:
            return inversion_number
        elif first[0] < second[0]:
            first.pop(0)
        else:
            inversion_number += len(first)
            second.pop(0)
    return inversion_number


if __name__ == '__main__':
    print inversion_calc([4, 1, 3, 2, 0])
    print inversion_recurcy([4, 1, 3, 2, 0])
