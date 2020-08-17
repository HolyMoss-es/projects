import os
import time
import zipfile


# Cкрипт, распределяющий файлы по годам и месяцам из архива.
#
# Например:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg


class Arranger:

    def __init__(self, read_f):
        self.read_f = read_f

    def walking(self):
        z = zipfile.ZipFile(self.read_f, 'r')
        for file in z.namelist():
            z.extract(file, self.mkdir(file))

    def get_time(self, file):
        epoch_sec = os.path.getmtime(file)
        return time.gmtime(epoch_sec)

    def mkdir(self, file):
        icons = 'icons_by_year'
        year = self.get_time(file)[0]
        month = self.get_time(file)[1]
        dest = os.path.join(icons, str(year), str(month))
        return os.makedirs(dest, exist_ok=True)


p = Arranger(None)
p.walking()
