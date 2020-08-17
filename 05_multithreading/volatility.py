# Расчет волатильности ценных бумаг упрощённым способом:
# отклонение в процентах от полусуммы крайних значений цены за торговую сессию:
#   полусумма = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / полусумма) * 100%
# Далее - вывод 3 максимальных и 3 минимальных волатильности, включая нулевые.


import os
import queue
from operator import itemgetter
import threading
from collections import defaultdict


folder = r'trades'


class VolatilityGetter(threading.Thread):

    def __init__(self, filename, vol_cont, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filename = filename
        self.tick = None
        self.volatility = 0
        self.min = None
        self.max = 0
        self.vol_cont = vol_cont

    def formula(self, min_price, max_price):
        half = (min_price + max_price) / 2
        return ((max_price - min_price) / half) * 100

    def run(self):
        with open(self.filename, 'r') as file_to_read:
            for line in file_to_read:
                self.tick, time, price, quant = line.split(',')
                if self.tick == 'SECID':
                    continue
                else:
                    price = float(price)
                    if price > self.max:
                        self.max = price
                    if self.min is None or price < self.min:
                        self.min = price
            self.volatility = round(self.formula(min_price=self.min, max_price=self.max), ndigits=2)
            res = str(self.tick) + str(self.volatility)
            self.vol_cont.put(res)


class CounterContainer(threading.Thread):

    def __init__(self, vol_dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counters = []
        self.vol_dict = vol_dict
        self.vol_que = queue.Queue(maxsize=1)

    def add_counter(self, file):
        counter = VolatilityGetter(filename=file, vol_cont=self.vol_que)
        self.counters.append(counter)

    def run(self):
        for counter in self.counters:
            counter.start()
        while True:
            try:
                res = self.vol_que.get(timeout=1)
                tick = res[0:4]
                vol = float(res[4:])
                self.vol_dict[tick] = vol
            except queue.Empty:
                if not any(counter.is_alive() for counter in self.counters):
                    break
        for counter in self.counters:
            counter.join()


paths = []
volatility_dict = defaultdict(int)
volatility_selected = {}

for dirname, dirpath, filenames in os.walk(folder):
    for file in filenames:
        path = os.path.join(folder, file)
        paths.append(path)

container = CounterContainer(vol_dict=volatility_dict)

for ticker in paths:
    container.add_counter(file=ticker)

container.start()
container.join()

for i, e in sorted(volatility_dict.items(), key=itemgetter(1), reverse=True):
    if len(volatility_selected) == 3:
        break
    volatility_selected[i] = e

for i, e in sorted(volatility_dict.items(), key=itemgetter(1), reverse=False):
    if len(volatility_selected) == 6:
        break
    if e == 0.0:
        continue
    else:
        volatility_selected[i] = e

for i, e in sorted(volatility_dict.items(), key=itemgetter(1), reverse=False):
    if e > 0:
        continue
    else:
        volatility_selected[i] = e

count = 0
for i, e in sorted(volatility_selected.items(), key=itemgetter(1), reverse=True):
    count += 1
    if count == 1:
        print('\nМаксимальная волатильность:')
    elif count == 4:
        print('\nМинимальная волатильность:')
    elif count == 7:
        print('\nНулевая волатильность:')
    print(f'{i}:{e}')