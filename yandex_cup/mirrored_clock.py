# Пробная задача из олимпиады по программированию от яндекса. Направление - алгоритмы.
# Скрипт, определяющий время на отзеркаленных часах.


def mirrored_clock(hour, minute):
    if hour != 12:
        hour = 12 - hour
    if minute != 00:
        minute = 60 - minute
    return str(f'{hour}:{minute}')


print(mirrored_clock(2, 45))
