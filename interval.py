import matplotlib.pyplot as plt
import numpy as np
from distribution_element import DistributionElement

class Interval:
    def __init__(self, a, b, count):
        self.a = a
        self.b = b
        self.count_data = 0
        self.count = count
        self.intervals = self.get_array_intervals(self.a, self.b, self.count)

    # Получить список интервалов
    @staticmethod
    def get_array_intervals(a, b, count):
        length = b - a
        step = length / count
        result = []
        value = b
        while value > a:
            new_segment = Segment(value)
            result.insert(0, new_segment)
            value -= step
        return result

    # Функция распределния
    @staticmethod
    def F(x, a, b):
        if x <= a:
            return 0
        elif b >= b:
            return 1
        else:
            return (x - a) / (b - a)

    # Функция плотности распределния
    @staticmethod
    def f(x, a, b):
        if a < x < b:
            return 1 / (b - a)
        else:
            return 0

    # Обратная функция распределения
    @staticmethod
    def F_reverse(gamma, a, b):
        return gamma * (b - a) + a

    def set_intervals(self, arr_arguments):
        self.clear_intervals()
        self.count_data = 0
        for value in arr_arguments:
            for element in self.intervals:
                if value <= element.argement:
                    element.increment()
                    self.count_data += 1
                    break

    def clear_intervals(self):
        for element in self.intervals:
            element.count = 0

    def __str__(self):
        strs = []
        for element in self.intervals:
            strs.append(str(element))

        return '\n'.join(strs)

    def print_gistoram(self):
        x = []
        y = []
        count_elements = self.count_data
        x_min = self.intervals[0].argement
        x_max = self.intervals[len(self.intervals)-1].argement
        # x_min = self.a
        # x_min = self.b
        h = (x_max - x_min) / len(self.intervals)
        for element in self.intervals:
            x.append(element.argement)
            y.append(element.count / (count_elements * h))


        plt.title('Гистограмма относительных частот')
        plt.bar(x, y, 0.05)

        plt.show()

    def get_intervals(self):
        result = []
        for element in self.intervals:
            new_element = DistributionElement(element.argement, element.count / self.count_data)
            result.append(new_element)
        return result


    def print_f_graph(self):
        plt.title('Плотность распределения')
        x = np.arange(0., 10., 0.05)
        y = [self.f(elem, self.a, self.b) for elem in x]
        plt.plot(x, y, "bo")
        # plt.xlabel('x')
        # plt.ylabel('y')
        plt.show()



class Segment:
    def __init__(self, argement):
        self.argement = argement
        self.count = 0

    def __str__(self):
        return f"{self.argement} : {self.count}"

    @property
    def argement(self):
        return self.__argement

    @argement.setter
    def argement(self, argement):
        self.__argement = argement

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        self.__count = count

    def increment(self):
        self.count += 1