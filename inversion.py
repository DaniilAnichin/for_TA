#!/usr/bin/python
# -*- coding: utf-8 -*-#
from urllib2 import urlopen


def inversion_calc(like_list):
    inversion_number = 0
    # inversions = []
    for i in range(len(like_list) - 1):
        for j in range(i, len(like_list)):
            if like_list[j] < like_list[i]:
                # inversions.append((i, j))
    # return inversions
                inversion_number += 1
    return inversion_number


def make_list(first_user, second_user):
    result = [None for i in range(len(first_user))]
    for i in range(len(first_user)):
        result[first_user[i] - 1] = second_user[i]
    return result


def inversion_recursion(like_list):
    # there are errors on the huge numbers
    half_len = len(like_list) / 2
    first = like_list[:half_len]
    second = like_list[half_len:]
    if len(like_list) > 2:
        return inversion_recursion(first) + inversion_recursion(second) + \
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


def main():
    small_list = urlopen('http://courses.prometheus.org.ua/c4x/KPI/'
                         'Algorithms101/asset/input_1000_5.txt')
    huge_list = urlopen('http://courses.prometheus.org.ua/c4x/KPI/'
                        'Algorithms101/asset/input_1000_100.txt')

    users = []
    for line in huge_list.readlines()[1:]:
        numbers = line.split(' ')
        index = int(numbers[0])
        users.append([])
        for number in numbers[1:]:
            users[index - 1].append(int(number))

    inversion_list = make_list(users[617], users[0])
    print inversion_recursion(inversion_list)
    print inversion_calc(inversion_list)
    # print users
    # print len(users)


if __name__ == '__main__':
    main()
    # print inversion_calc([4, 1, 3, 2, 0])
    # print inversion_recursion([4, 1, 3, 2, 0])
