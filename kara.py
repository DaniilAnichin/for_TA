#!usr/bin/python
# -*- coding: utf-8 -*-#
from math import log


ozf = 0
st = 0
ot = 0


def kara(x, y):
    half_len = _half_len(x, y)
    if half_len == 0:
        return x * y
    x_div = to_two(x, half_len)
    y_div = to_two(y, half_len)

    ac = kara(x_div[0], y_div[0])
    bd = kara(x_div[1], y_div[1])
    mid = kara(x_div[0] + x_div[1], y_div[0] + y_div[1])
    check = mid - ac - bd
    if check == 105:
        global ozf
        ozf += 1
    if check == 72:
        global st
        st += 1
    if check == 12:
        global ot
        ot += 1
    return ac * 10 ** (half_len * 2) + check * 10 ** half_len + bd


def _half_len(x, y):
    len_x = len(str(x))
    len_y = len(str(y))
    len_max = max(len_x, len_y)

    log_2 = log(len_max, 2)
    if int(log_2) == log_2:
        half_len = int(2 ** (log_2 - 1))
    else:
        half_len = int(2 ** int(log_2))
    return half_len


def to_two(x, half_len):
    first = int(str(x)[:-half_len]) if str(x)[:-half_len] is not '' else 0
    second = int(str(x)[-half_len:])
    return [first, second]


if __name__ == '__main__':
    # print to_two(11)
    print kara(1685287499328328297814655639278583667919355849391453456921116729,
               7114192848577754587969744626558571536728983167954552999895348492)
    print '105: %d\n72: %d\n12: %d' % (ozf, st, ot)
