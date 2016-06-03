#!/use/bin/python
# -*- coding: utf-8 -*-
from urllib2 import urlopen


class Heap(list):
    def __init__(self, values, direction):
        super(Heap, self).__init__(values)
        self.direction = direction

    def get_left(self, index):
        if len(self) > index * 2 + 1:
            return index * 2 + 1
        else:
            return -1

    def get_right(self, index):
        if len(self) > index * 2 + 2:
            return index * 2 + 2
        else:
            return -1

    def get_parent(self, index):
        return (index - 1) / 2

    def check_heap(self, index):
        left = self.get_left(index)
        right = self.get_right(index)

        if self.direction == 'up':
            if left > 0 and self[left] > self[index]:
                top = left
            else:
                top = index
            if right > 0 and self[right] > self[top]:
                top = right
        else:
            if left > 0 and self[left] < self[index]:
                top = left
            else:
                top = index
            if right > 0 and self[right] < self[top]:
                top = right

        if top != index:
            self[index], self[top] = self[top], self[index]
            self.check_heap(top)

    def make_heap(self):
        for i in range(len(self) / 2 - 1, -1, -1):
            self.check_heap(i)

    def restore_heap(self, index):
        parent = self.get_parent(index)

        if self.direction == 'up':
            if parent >= 0 and self[parent] < self[index]:
                self[index], self[parent] = self[parent], self[index]
                self.restore_heap(parent)
        else:
            if parent >= 0 and self[parent] > self[index]:
                self[index], self[parent] = self[parent], self[index]
                self.restore_heap(parent)

    def sort_insert(self, value):
        self.append(value)
        self.restore_heap(len(self) - 1)

    def delete_head(self):
        self[len(self) - 1], self[0] = self[0], self[len(self) - 1]
        head = self.pop(len(self) - 1)
        self.check_heap(0)
        return head


def both_append(upper, lower, value):
    if len(lower) > 0 and value < lower[0]:
        lower.sort_insert(value)
    else:
        upper.sort_insert(value)

    if len(upper) - len(lower) > 1:
        head = upper.delete_head()
        lower.sort_insert(head)
    elif len(upper) - len(lower) < -1:
        head = lower.delete_head()
        upper.sort_insert(head)


def get_medians(upper, lower):
    if len(lower) > len(upper):
        return lower[0]
    elif len(lower) < len(upper):
        return upper[0]
    else:
        return lower[0], upper[0]


if __name__ == '__main__':
    t_upper = Heap([], direction='down')
    t_lower = Heap([], direction='up')
    page = urlopen('http://courses.prometheus.org.ua/c4x/KPI/'
                 'Algorithms101/asset/input_16_10000.txt')
    numbers = [int(number) for number in page.readlines()[1:]]
    # print numbers[:20]
    medians = []
    lower_heap = []
    upper_heap = []
    for number in numbers:
        both_append(t_upper, t_lower, number)
        medians.append(get_medians(t_upper, t_lower))
        lower_heap.append(t_lower[:5])
        upper_heap.append(t_upper[:5])
    for i in range(25, 30):
        print 'medians: ', medians[i]
        print 'lower: ', lower_heap[i]
        print 'upper: ', upper_heap[i]

    print 'Median 2015: ', medians[2014]
    print 'Median 9876: ', medians[9875]
    print 'lower: ', lower_heap[2014]
    print 'upper: ', upper_heap[2014]
