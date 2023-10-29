import math
import random
from interval import Interval

def get():
    
    n = 200
    N = int(math.log2(n))
    a = 4
    b = 5

    data = []
    for _ in range(n):
        gamma = random.random()
        x = Interval.F_reverse(gamma, a, b)
        data.append(x)

    interval = Interval(a, b, N)

    interval.set_intervals(data)

    # print(interval)

    # interval.print_gistoram()
    # interval.print_f_graph()

    return interval.get_intervals()

