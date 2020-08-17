# -*- coding: utf-8 -*-

# Декоратор, логирующий ошибки в декорируемой функции


def log_errors(filename):
    def inner(func):
        def inner_inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as exception:
                with open(file=filename, mode='a', encoding='utf8') as logfile:
                    s = f'{func.__name__}, {args}, {kwargs}, {str(exception)}\n'
                    logfile.write(s)
                raise
        return inner_inner
    return inner


@log_errors(filename='function_errors.log')
def perky(param):
    return param / 0


@log_errors(filename='function_errors.log')
def check_line(ln):
    name, email, age = ln.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not an email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')
perky(param=42)

