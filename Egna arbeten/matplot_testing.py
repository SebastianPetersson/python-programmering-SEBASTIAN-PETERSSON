# import matplotlib.pyplot as plt
# import math

# x = list(range(10))
# k = 2
# m = 2
# y = [k*x+m for x in x]

# plt.plot(x, y)
# plt.xlabel = "x"
# plt.ylabel = "y"
# plt.title = "Funktion av y=kx+m"
# plt.grid()
# plt.gca().set_aspect("equal")

# plt.show()

import numpy as np
import matplotlib.pyplot as plt


A_list = [2,3,4,5]
B_list = ["a", 'b', 'c', 'd']
C_list = [7, 8, 9, 10]

tuple_list = list(zip(A_list, B_list, C_list))

print(tuple_list)

print(list(zip(*tuple_list)))


# def medelvärde(*args):
#     summa = 0
#     värden = [1,4,5,8,7,9,6,3,2]
#     for arg in args:


def draw_circle(radius = 1, center = (0,0)):
    x = np.linspace(0, 2*np.pi)
    plt.plot(radius*np.sin(x)+center[0], radius*np.cos(x)+center[1])






