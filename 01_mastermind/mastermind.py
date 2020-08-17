# Загадывается 4х значное число. Его нужно отгадать. Все цифры разные и первое из них не может быть нулём.
# Cow - одна цифра, которая есть в загаданном числе, но находится не на той позиции.
# Bull - цифра, отгаданная позиционно.
# При загаданном 1234 и отгаданном 1562 будет 1 bull и 1 cow

from mastermind_engine import make_up_number, valid_number, check_number

make_up_number()
turn_count = 0
while True:
    number = list(input('Введите число.\n>'))
    turn_count += 1
    if not valid_number(number):
        print('Недопустимое число.')
        continue

    if check_number(number)['bull'] == 4:
        print('Номер угадан с', turn_count, 'попыток.')
        another = input('Ещё партейку(Y or N)?\n>')
        if another == 'Y' or another == 'y':
            make_up_number()
            continue
        elif another == 'N' or another == 'n':
            break
        else:
            break