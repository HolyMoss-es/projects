# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Проверки строк файла:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки формируются 2 файла
# - registrations_good.log - правильные данные
# - registrations_bad.log - ошибочные данные


import os

file = os.path.realpath('registrations.txt')


class NotNameError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class NotEmailError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class LogPars:

    def __init__(self, input_f):
        self.input_f = input_f
        self.good = 'registrations_good.log'
        self.bad = 'registrations_bad.log'

    def pars(self):
        with open(self.input_f, 'r', encoding='utf8') as input_file:
            for line in input_file:
                try:
                    self.check(line)
                except NotNameError as nne:
                    self.reg_bad(line=line, exc=nne)
                except NotEmailError as nee:
                    self.reg_bad(line=line, exc=nee)
                except ValueError as ve:
                    self.reg_bad(line=line, exc=ve)

    def check(self, line):
        try:
            self.unpack(line)
        except ValueError:
            raise ValueError('One of the fields is empty, or operands are misplaced')

        name, mail, age = self.unpack(line) # а почему не так?...

        if not name.isalpha():
            raise NotNameError('Invalid name')
        elif '@' not in mail or '.' not in mail:
            raise NotEmailError('Invalid email')
        elif age > 99 or age < 10:
            raise ValueError('Invalid age')
        else:
            self.reg_good(line)

    def unpack(self, line):
        self.oper_1, self.oper_2, self.oper_3 = line.split(' ')
        self.oper_1 = str(self.oper_1)
        self.oper_2 = str(self.oper_2)
        self.oper_3 = int(self.oper_3)
        res = [self.oper_1, self.oper_2, self.oper_3]
        return res

    def reg_good(self, line):
        with open(self.good, 'a', encoding='utf8') as good_f:
            good_f.write(line)

    def reg_bad(self, line, exc):
        with open(self.bad, 'a', encoding='utf8') as bad_f:
            exc = str(exc)
            res = f'{exc} - {line}'
            bad_f.write(res)


p = LogPars(file)
p.pars()
