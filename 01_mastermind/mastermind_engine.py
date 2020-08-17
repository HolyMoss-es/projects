from random import randint

_holder = []
_turn_count = [0]


def make_up_number():
    global _holder
    _holder = []
    while len(_holder) < 4:
        number = randint(0, 9)
        if len(_holder) == 0 and number == 0:
            continue
        elif str(number) in _holder:
            continue
        else:
            _holder.append(str(number))
    print(_holder)
    return _holder


def check_number(number):
    bull, cow = 0, 0
    for i in range(4):
        if number[i] == _holder[i]:
            bull += 1
        elif number[i] in _holder:
            cow += 1
    print({'bull': bull, 'cow': cow})
    return {'bull': bull, 'cow': cow}


def valid_number(number):
    return not (number[0] == '0' or len(number) != 4 or len(number) != len(set(number)))

