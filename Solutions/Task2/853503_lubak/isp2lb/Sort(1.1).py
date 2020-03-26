import tempfile, os, random, math

with open('numbers.txt', 'w') as f:
    f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(500000))

class Vector(object):
    def __init__(self, array):
        self.n = len(array)
        self.arr = array

    def __add__(self, other):
        if self.n != other.n:
            print ("error")
            return
        arr = [0] * self.n
        vector = Vector(arr)
        for i in range (0, self.n):
            vector.arr[i] = self.arr[i] + other.arr[i]
        return vector

    def __sub__(self, other):
        if self.n != other.n:
            print ("error")
            return
        arr = [0] * self.n
        vector = Vector(arr)
        for i in range (0, self.n):
            vector.arr[i] = self.arr[i] - other.arr[i]
        return vector

    def __mul__(self, other):
        if self.n != other.n:
            print ("error")
            return
        arr = [0] * self.n
        vector = Vector(arr)
        for i in range (0, self.n):
            vector.arr[i] = self.arr[i] * other.arr[i]
        return vector

    def __mul__(self, other):
        arr = [0] * self.n
        vector = Vector(arr)
        for i in range (0, self.n):
            vector.arr[i] = self.arr[i] * other
        return vector

    def __eq__(self, other):
        if self.n != other.n:
            return False
        for i in range(0, self.n):
            if self.arr[i] != other.arr[i]:
                return False
        return True

    def __len__(self):
        return self.n

    def __str__(self):
        line = ''
        for i in range(0, self.n):
            line += str(self.arr[i]) + ' '
        return line

    def __getitem__(self, item):
        return self.arr[item]


def merge_sort():
    count_length = 0

    with open('numbers.txt') as file:
        for line in file:  # подсчет количества строк в файле
            count_length += 1
    files = []
    k = 0
    with open('numbers.txt') as file:
        while k < count_length / 128:
            mass = []
            i = 0
            while i < 128:
                temp = file.readline()  # считываем с файла
                if len(temp) != 0:
                    mass.append(int(temp))  # заносим в массив
                else:
                    break
                i += 1
            mass.sort()
            with tempfile.NamedTemporaryFile('w', delete=False) as tfile:
                # Эта функция создает временный файл в системной директории  и возвращает файлоподобный объект
                # Мы можем сохранить имя ВФ и использовать после закрытия файла или заверш програм. (delete=False).
                for i in mass:
                    tfile.write(str(i) + '\n')  # заносим массивв в временный файл
                tfile.write('\n')
                files.append(tfile.name)  # в мссив заносим название файла гре хран. знач
            k += 1
    kolvonew = len(files)
    while kolvonew != 1:
        k = knew = 0
        while k < kolvonew:

            if k + 1 == kolvonew:
                files[knew] = files[k]
                knew += 1
                k += 1
            else:
                k1 = k
                k2 = k + 1
                len1 = len2 = 0
                with open(files[k1]) as file:
                    for line in file:
                        len1 += 1
                with open(files[k2]) as file:
                    for line in file:
                        len2 += 1

                j1 = j2 = 1

                with open(files[k1]) as file1:
                    with open(files[k2]) as file2:
                        with tempfile.NamedTemporaryFile('w', delete=False) as t:
                            a1 = file1.readline()
                            a2 = file2.readline()
                            while j1 < len1 and j2 < len2:
                                if int(a1) < int(a2):
                                    t.write(a1)
                                    a1 = file1.readline()
                                    j1 += 1

                                else:
                                    t.write(a2)
                                    a2 = file2.readline()
                                    j2 += 1
                            while j1 < len1:
                                t.write(a1)
                                a1 = file1.readline()
                                j1 += 1

                            while j2 < len2:
                                t.write(a2)
                                a2 = file2.readline()
                                j2 += 1
                            t.write('\n')

                            files[knew] = t.name
                knew += 1
                k += 2
        kolvonew = knew

    with open('sorted_numbers.txt', 'w') as file:
        with open(files[0]) as t:
            for line in t:
                file.write(line)


def main():
    merge_sort()


if __name__ == "__main__":
    main()







