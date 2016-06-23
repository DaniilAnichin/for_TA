#!/use/bin/python
# -*- coding: utf-8 -*-


def has_sum(check_list, summ):
    for num in check_list:
        try:
            id = check_list.index(summ - num)
            if check_list[id] != num:
                return True
        except ValueError:
            pass
    return False


def calc_sums(check_list, summ_list):
    summ_num = 0
    for summ in summ_list:
        print summ
        if has_sum(check_list, summ):
            summ_num += 1
    return summ_num


if __name__ == '__main__':
    with open('./test_06.txt', 'rt') as out:
        numbers = [int(number) for number in out.readlines()]
    print numbers[:50]
    print calc_sums(numbers, range(-1000, 1001))
    # my_list = [1, 2, 3, 4]
    # print numbers.index(68248163335)
    # print has_sum(my_list, 3)
