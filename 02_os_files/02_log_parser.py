# Имеется файл вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Скрипт считыает файл и выводит число событий NOK за каждую минуту в другой файл в формате:
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321


from collections import defaultdict
import operator


class Parser:

    def __init__(self, read_f, write_f):
        self.read_f = read_f
        self.write_f = write_f
        self.stat = defaultdict(int)

    def collect_stat(self):
        with open(self.read_f, 'r') as input_file:
            for line in input_file:
                self.stat[self.get_time_from_line(line)] += 'NOK' in line
            self.write_stat()

    def write_stat(self):
        with open(self.write_f, 'w') as output_file:
            for i, e in sorted(self.stat.items(), key=operator.itemgetter(0)):
                output_file.write(('{} {}\n'.format(i, e)))


class SortAll(Parser):

    def get_time_from_line(self, string):
        return string[1:18]


class SortHour(Parser):

    def get_time_from_line(self, string):
        return string[1:14]


class SortMonth(Parser):

    def get_time_from_line(self, string):
        return string[1:8]


class SortYear(Parser):

    def get_time_from_line(self, string):
        return string[1:5]


p = SortHour(None, 'NOK')
p.collect_stat()
