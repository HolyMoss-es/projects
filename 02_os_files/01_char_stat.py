# Скрипт, собирающий статистику по кол-ву букв в тексте.
# Может извлекать его из архива при необходимости.
# Выполненно в шаблонном методе проектирования.

import os
import zipfile
import operator
from collections import defaultdict


class Statistics:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = defaultdict(int)

    def __str__(self):
        return self.stat

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect_stat(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        self.stat[char] += 1

    def print_stat(self):
        stats = self.output()
        print('|{x:<5}:'.format(x='Буква'), '{y:>10}|'.format(y='Частота'))
        amount = 0
        for e in stats:
            print('|{x:<1}:'.format(x=e[0]), '{y:>14}|'.format(y=e[1]))
            amount += e[1]
        print('|{x:<5}:'.format(x='Итого'), '{y:>10}|'.format(y=amount))


class SortAmountDescend(Statistics):

    def output(self):
        return sorted(self.stat.items(), reverse=True, key=operator.itemgetter(1))


class SortAmountAscend(Statistics):

    def output(self):
        return sorted(self.stat.items(), reverse=False, key=operator.itemgetter(1))


class SortKeyDescent(Statistics):

    def output(self):
        return sorted(self.stat.items(), reverse=True, key=operator.itemgetter(0))


class SortKeyAscend(Statistics):

    def output(self):
        return sorted(self.stat.items(), reverse=False, key=operator.itemgetter(0))


stat = SortAmountDescend(file_name=None)
stat.collect_stat()
stat.print_stat()
