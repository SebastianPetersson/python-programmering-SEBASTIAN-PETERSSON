# Can you compute all multiples of 3 and 5
# That are less than 100

# total = 0

# for i in range(1,100):
#     if i % 3 == 0 or i % 5 == 0:
#         total += i

# print(total)

# import math

# def cm (feet = 0, inches = 0):

#     feet_to_cm = feet*12*2.54
#     inches_to_cm = inches*2.54
#     return inches_to_cm + feet_to_cm

# print(cm(feet = 6, inches = 6))

import random as rnd

tärnings_kast = [10, 100, 1000, 10000, 100000, 1000000]

for antal_kast in tärnings_kast:
    sexor = 0
    for i in range(antal_kast):
        kast = rnd.randint(1,6)
        if kast == 6:
            sexor += 1
    sannolikhet = sexor/antal_kast
    print(f"Antal kast: {antal_kast}, Antal sexor: {sexor}, Sannolikhet för sexa {sannolikhet*100:.2f} %.")




    lista = [1, 2, 3, 4, 5]

    x,y = lista[0, 1]