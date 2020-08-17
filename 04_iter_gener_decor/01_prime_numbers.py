# Класс итерируемых объектов, возвращающий простые числа до n


class PrimeNumbers:

    def __init__(self, n):
        self.n = n
        self.iter = 1
        self.check = []

    def __iter__(self):
        self.iter = 1
        self.check = []
        return self

    def __next__(self):
        self.iter += 1
        while True:
            if self.iter >= self.n:
                raise StopIteration
            for x in self.check:
                if self.iter % x == 0 and self.iter != x:
                    self.iter += 1
                    break
            else:
                self.check.append(self.iter)
                return self.iter


# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)

# То же самое, но в виде генератора:


def prime_numbers_generator(n):
    prime_num = []
    for i in range(2, n):
        for prime in prime_num:
            if i % prime == 0:
                break
        else:
            prime_num.append(i)
            yield i


# for number in prime_numbers_generator(n=10000):
#     print(number)

