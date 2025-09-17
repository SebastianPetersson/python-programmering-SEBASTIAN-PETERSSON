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


A_list = [2,3,4,5]
B_list = ["a", 'b', 'c', 'd']
C_list = [7, 8, 9, 10]

tuple_list = list(zip(A_list, B_list, C_list))

print(tuple_list)

print(list(zip(*tuple_list)))