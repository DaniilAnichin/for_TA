#!/use/bin/python
# -*- coding: utf-8 -*-
from urllib2 import urlopen
letter_string = 'abcdefghijklmnopqrstuvwxyz'
global_letter_list = [0 for i in range(len(letter_string))]


def radix_sort(latin_list, sort_num):
    """
    Function will be used for sorting lower-case latin strings list
    by the sort_num indexed letter
    """
    letter_list = [0 for i in range(len(letter_string))]
    for word in latin_list:
        letter_list[letter_string.index(word[sort_num])] += 1
        global_letter_list[letter_string.index(word[sort_num])] += 1

    for i in range(1, len(letter_list)):
        letter_list[i] += letter_list[i - 1]

    result = [None for i in range(len(latin_list))]
    for i in range(len(latin_list) - 1, -1, -1):
        word = latin_list[i]
        letter = word[sort_num]
        result[letter_list[letter_string.index(letter)] - 1] = word
        letter_list[letter_string.index(letter)] -= 1

    return result


if __name__ == '__main__':
    # Yeah, it works!!!
    page = urlopen('http://courses.prometheus.org.ua/c4x/KPI/'
                   'Algorithms101/asset/anagrams.txt')
    word_list = [word[:-1] if word[-1] == '\n' else word
                 for word in page.readlines()]
    print word_list[:20]
    word_list_2 = radix_sort(word_list, 2)
    word_list_3 = radix_sort(word_list_2, 1)
    word_list_end = radix_sort(word_list_3, 0)
    print '%s & %s' % (word_list_end[0], word_list_end[-1])
    print letter_string[global_letter_list.index(max(global_letter_list))]

