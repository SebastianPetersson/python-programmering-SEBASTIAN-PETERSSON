# Exercise 04 - list exercise

# print("Uppgift 1 - Dice rolls(*) A B C \n")
# print("a)\n")

# import random as rnd

# random_siffror = []

# for i in range(10):
#     kast = rnd.randint(1,6)
#     random_siffror.append(kast)

# random_siffror.sort()
# print(f"Kast i ordning lägst till högst:\n{random_siffror}")

# print("\nb)\n")

# random_siffror.reverse()
# print(f"Kast i ordning högst till lägst:\n{random_siffror}")

# print("\nc)\n")

# random_siffror.reverse()
# max = random_siffror[-1]
# min = random_siffror[0]

# print(f"Det högsta kastet blev {max} och det minsta kastet blev {min}!")

# ________________________________________________________________________________________________________________

# print("\nUppgift 2 - Food menu(*) A B C \n")
# print("a)\n")

# dishes = ["Vegetarisk lasagne", "Spaghetti", "Fisk", "Grönsakssoppa", "Pannkakor"]
# days = ["Mån", "Tis", "Ons", "Tors", "Fre"]

# print("Bambameny:")

# for day, dish in zip(days,dishes):
#     print(f"{day}: {dish}.")

# print("b)\n")


# ________________________________________________________________________________________________________________

# print("\nUppgift 3 - Squares(*) \n")
# print("a)\n")

# import numpy as np
# import matplotlib.pyplot as plt

# numbers = range(-10, 11)

# squared = [n*n for n in numbers]

# print(squared)

# plt.plot(squared)
# plt.title(f"The function x2")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()

# ________________________________________________________________________________________________________________

print("\nUppgift 4 - Chessboard(**) \n")
from pprint import pprint #Ny modul jag hittade för formatering!

letters = "ABCDEFGH"
numbers = "12345678"

chessboard = [[f"{letter}{number}" for letter in letters] for number in numbers]

pprint(chessboard) 

for row in chessboard:
    print(" ".join(row))

#_________________________________________________________________________________________________________________

# print("\nUppgift 5 - Dice rolls convergence(**) \n")
# print("\na)\n")
# # import random as rnd

# # amount = []

# # for i in range(100):
# #     dice_roll = rnd.randint(1,6)
# #     if dice_roll == 6:
# #         amount.append(dice_roll)

# # print(len(amount))

# print("\nb)\n")

# import random as rnd

# throws = [10, 100, 1000, 10000, 100000, 1000000]
# amount_sixes = []
# probability = []

# for i in throws:
#     dice_roll = rnd.randint(1,6)

