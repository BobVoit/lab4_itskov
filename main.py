import numpy as np
import random
import math
import lab1
import lab2
import lab3
from distribution import Distribution
from interval import Interval

def binomial_value(n, p):
    d = Distribution(p, n)
    series = d.get_discrete_series()
    gamma = random.random()
    for index, current in enumerate(series):
        if current > gamma:
            return index
    return n

def uniform_distribution(count, a, b):
    N = int(math.log2(count))
    gamma = random.random()
    data = []
    for _ in range(count):
        gamma = random.random()
        x = Interval.F_reverse(gamma, a, b)
        data.append(x)

    # interval = Interval(a, b, N)

    # interval.set_intervals(data)
    # intervals =interval.get_intervals()
    return data

def normal_distribution(count, sigma, m):
    x = np.array([])
    for i in range(count):
        sum_elements = 0
        for j in range(12):
            sum_elements += random.random()
        x = np.append(x, sum_elements - 6)
    y = np.array([])
    for element in x:
        y = np.append(y, sigma * element + m)
    return y


# 1
count = 100
n = 13
p = 0.82
values = np.array([binomial_value(n, p) for _ in range(count)])
variations, freqs = np.unique(values, return_counts=True)
# +++ БИНОМИНАЛЬНОЕ РАСПРЕДЕЛЕНИЕ
# Математическое ожидание
expected_value = n * p
# Дисперсия
dispersion = n * p * (1 - p)
# Выборочное среднее
sample_mean = np.sum(variations * freqs) / count
# Выборочная дисперсия и среднее квадратичное отклонение
middle_value = [(value - sample_mean)**2 for value in values]
sample_dispersion = sum(middle_value) / count
standard_deviation = math.sqrt(sample_dispersion)
# Исправлленная дисперсия и среднее квадратичное отклонение
corrected_sample_dispersion = (count / (count - 1)) * sample_dispersion
corrected_standard_deviation = math.sqrt(corrected_sample_dispersion)
# Вывод результатов
print("Лабораторная работа №1")
print(f"Математическое ожидание: {expected_value}")
print(f"Дисперсия: {dispersion}")
print(f"Выборочное среднее: {sample_mean}")
print(f"Выборочная дисперсия: {sample_dispersion}")
print(f"Выборочное среднее квадратичное отклонение: {standard_deviation}")
print(f"Исправленная выборочная дисперсия: {corrected_sample_dispersion}")
print(f"Исправленное среднее квадратичное отклонение: {corrected_standard_deviation}")
print("\n")


# 2
count = 200
a = 4
b = 5
# values = np.array([binomial_value(n, p) for _ in range(count)])
values = uniform_distribution(count, a, b)
variations, freqs = np.unique(values, return_counts=True)
# +++ РАВНОМЕРНОЕ РАСПРЕДЕЛЕНИЕ
# Математическое ожидание
expected_value = (a + b) / 2
# Дисперсия
dispersion = ((b - a)**2) / 12
# Выборочное среднее
sample_mean = np.sum(variations * freqs) / count
# Выборочная дисперсия и среднее квадратичное отклонение
middle_value = [(value - sample_mean)**2 for value in values]
sample_dispersion = sum(middle_value) / count
standard_deviation = math.sqrt(sample_dispersion)
# Исправлленная дисперсия и среднее квадратичное отклонение
corrected_sample_dispersion = (count / (count - 1)) * sample_dispersion
corrected_standard_deviation = math.sqrt(corrected_sample_dispersion)
# Вывод результатов
print("Лабораторная работа №2")
print(f"Математическое ожидание: {expected_value}")
print(f"Дисперсия: {dispersion}")
print(f"Выборочное среднее: {sample_mean}")
print(f"Выборочная дисперсия: {sample_dispersion}")
print(f"Выборочное среднее квадратичное отклонение: {standard_deviation}")
print(f"Исправленная выборочная дисперсия: {corrected_sample_dispersion}")
print(f"Исправленное среднее квадратичное отклонение: {corrected_standard_deviation}")
print("\n")

# 3
count = 200
m = 0.5
sigma = 2
# values = np.array([binomial_value(n, p) for _ in range(count)])
values = normal_distribution(count, sigma, m)
variations, freqs = np.unique(values, return_counts=True)
# +++ РАВНОМЕРНОЕ РАСПРЕДЕЛЕНИЕ
# Математическое ожидание
expected_value = m
# Дисперсия
dispersion = sigma ** 2
# Выборочное среднее
sample_mean = np.sum(variations * freqs) / count
# Выборочная дисперсия и среднее квадратичное отклонение
middle_value = [(value - sample_mean)**2 for value in values]
sample_dispersion = sum(middle_value) / count
standard_deviation = math.sqrt(sample_dispersion)
# Исправлленная дисперсия и среднее квадратичное отклонение
corrected_sample_dispersion = (count / (count - 1)) * sample_dispersion
corrected_standard_deviation = math.sqrt(corrected_sample_dispersion)
# Вывод результатов
print("Лабораторная работа №3")
print(f"Математическое ожидание: {expected_value}")
print(f"Дисперсия: {dispersion}")
print(f"Выборочное среднее: {sample_mean}")
print(f"Выборочная дисперсия: {sample_dispersion}")
print(f"Выборочное среднее квадратичное отклонение: {standard_deviation}")
print(f"Исправленная выборочная дисперсия: {corrected_sample_dispersion}")
print(f"Исправленное среднее квадратичное отклонение: {corrected_standard_deviation}")
print("\n")


# Доверительные интервалы
print("Доверительные интервалы")
alpha = 0.95
t = 0.1826 
min_value = sample_mean - ((sigma * t) / count)
max_value = sample_mean + ((sigma * t) / count)
print(f"{min_value} < m < {max_value}")

t = 1.971956544249395    
s = corrected_standard_deviation
min_value = sample_mean - ((s * t) / count)
max_value = sample_mean + ((s * t) / count)
print(f"{min_value} < m < {max_value}")

t = 1.971956544249395    
xi1 = 161.82618
xi2 = 239.95968
min_value = (corrected_sample_dispersion  * (count - 1)) / (xi2)
max_value = (corrected_sample_dispersion  * (count - 1)) / (xi1)
print(f"{min_value} < sigma^2 < {max_value}")