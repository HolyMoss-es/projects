# Аналог скрипта log parser из директории 02_os_files, выполненный в виде итератора

file = 'events.txt'


class IterParser:

    def __init__(self, read_f):
        self.read_f = read_f
        self.NOK = 0
        self.previous = None
        self.current = None

    def __iter__(self):
        self.NOK = 0
        self.previous = None
        self.current = None
        self.f = open(self.read_f, 'r')
        return self

    def __next__(self):
        for line in self.f:
            self.current = line[1:17]
            if self.previous == self.current or self.previous is None:
                if 'NOK' in line:
                    self.NOK += 1
                self.previous = self.current
                continue
            elif self.previous != self.current:
                if self.NOK > 0:
                    prev_nok = self.NOK
                    prev_to_return = self.previous
                    self.previous = self.current
                    if 'NOK' in line:
                        self.NOK = 1
                    else:
                        self.NOK = 0
                    return prev_to_return, prev_nok
                elif self.NOK == 0:
                    if 'NOK' in line:
                        self.NOK += 1
                    self.previous = self.current
                    continue
        if self.NOK > 0:
            prev_nok = self.NOK
            self.NOK = 0
            return self.previous, prev_nok
        self.f.close()
        raise StopIteration()


ip = IterParser(file)
for i, e in ip:
    print(f'[{i}] {e}')
