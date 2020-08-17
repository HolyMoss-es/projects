import warnings
import re


class ScoreGetter:

    def __init__(self, res):
        self.x_re = r'[хХxX]'
        self.res = res
        self.score = 0
        self.check_res()

    def check_res(self):

        """
        Проверка правильности формы строки
        """

        x_amount = len(re.findall(self.x_re, self.res))
        formula = (x_amount * 2) + (len(self.res) - x_amount)

        if len(self.res) > 20:
            raise LenError()
        if formula > 20 or x_amount > 10:
            raise TooManyXs

    def x_in(self, elem):
        return bool(re.match(self.x_re, elem))

    def run(self):
        """
        Алгоритм подсчёта очков
        """
        i = 0
        while i != len(self.res):
            if self.x_in(self.res[i]):
                self.score += 20
                i += 1
                continue
            elif self.res[i].isnumeric():
                if i == len(self.res) - 1:
                    raise InputError
                if self.res[i + 1] == '/':
                    self.score += 15
                    i += 2
                    continue
                elif self.res[i + 1] == '-':
                    self.score += int(self.res[i])
                    i += 2
                    continue
                elif self.res[i + 1].isnumeric():
                    add = int(self.res[i]) + int(self.res[i + 1])
                    if add > 10:
                        raise InvalidFrame()
                    elif add == 10:
                        warnings.warn(f'frame - "{self.res[i]}{self.res[i + 1]}" should be written as "{self.res[i]}/".'
                                      f' Scoring 15 points instead of 10.')
                        self.score += 15
                        i += 2
                        continue
                    else:
                        self.score += add
                        i += 2
                        continue
                else:
                    raise InputError()
            elif self.res[i] == '-':
                if self.res[i + 1].isnumeric():
                    self.score += int(self.res[i + 1])
                    i += 2
                    continue
                elif self.res[i + 1] == self.res[i]:
                    i += 2
                    continue
                else:
                    raise InputError()
        return self.score


class InputError(Exception):

    def __init__(self):
        self.message = 'Invalid input..'

    def __str__(self):
        return self.message


class LenError(Exception):

    def __init__(self):
        self.message = 'String size is invalid'

    def __str__(self):
        return self.message


class TooManyXs(Exception):

    def __init__(self):
        self.message = "Too many x's in an input string"

    def __str__(self):
        return self.message


class InvalidFrame(Exception):

    def __init__(self):
        self.message = "Too many pins in a frame"

    def __str__(self):
        return self.message
