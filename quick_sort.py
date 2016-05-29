#!/use/bin/python
# -*- coding: utf-8 -*-
from random import randint
from urllib2 import urlopen

count = 0


def quick_sort(sort_list, start, end):
    if end != start:
        index = split(sort_list, start, end)
        if index != -1:
            quick_sort(sort_list, start, index - 1)
            quick_sort(sort_list, index + 1, end)


def split(split_list, start, end):
    if end - start < 1:
        return -1
    global count
    before = start
    # middle_index = randint(start, end)
    if end - start == 1:
        middle_index = start
        middle = split_list[middle_index]
        split_list[middle_index] = split_list[end]
        split_list[end] = middle
    else:
        upper = split_list[start]
        lower = split_list[end]
        mid = split_list[(start + end) / 2]
        values = [upper, mid, lower]
        values.pop(values.index(max(values)))
        values.pop(values.index(min(values)))
        middle = values[0]
        if middle == upper:
            middle_index = start
        elif middle == mid:
            middle_index = (start + end) / 2
        else:
            middle_index = end
        split_list[middle_index] = split_list[end]
        split_list[end] = middle

    for i in range(start, end):
        count += 1
        if split_list[i] <= middle:
            if i != before:
                temp = split_list[i]
                split_list[i] = split_list[before]
                split_list[before] = temp
            before += 1
    split_list[end] = split_list[before]
    split_list[before] = middle
    return before


if __name__ == '__main__':
    raw_numbers = urlopen('http://courses.prometheus.org.ua/c4x/KPI/'
                          'Algorithms101/asset/input__10000.txt')
    _list = [int(number) for number in raw_numbers.readlines()[1:]]
    # _list = [12, 8, 7, 1, 3, 5, 6, 4, 10, 2, 9, 11]
    quick_sort(_list, 0, len(_list) - 1)
    print _list[:20]
    print count
