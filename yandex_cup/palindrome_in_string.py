# Пробная задача из олимпиады по программированию от яндекса. Направление - алгоритмы.
# скрипт ищет палиндромы в строке

test = 'AGGAhjhABAklANNA'


def palindrome_search(s):
    n = len(s)
    max_radius = (n - 1) // 2
    radius_data = [x for x in range(1, max_radius+1)]
    palindromes = []

    def search(odd):
        x = 1 if odd is True else 2

        for pivot in range(1, n - 1):
            for i in radius_data:
                if pivot < i or n - pivot <= i:
                    break
                left_chunk = s[pivot-i:pivot]
                right_chunk = s[pivot:pivot+i+x]
                new_string = left_chunk + right_chunk

                if new_string == new_string[::-1]:
                    if new_string in palindromes:
                        continue
                    else:
                        palindromes.append(new_string)
    search(True)
    search(False)

    if not palindromes:
        return None
    else:
        print(palindromes)
        return min(palindromes)


print(palindrome_search(test))
