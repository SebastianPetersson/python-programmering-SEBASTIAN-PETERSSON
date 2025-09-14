# #Exercise_3_for_statements

# print("\nUppgift 1 - Count numbers(*)\n" + "\na)\n")


# for i in range(-10, 11):
#     print(f"{i}", end = " ")
    

# #_____________________________________________________________________________

# # print("\n" + "_"*100)
# print("\nb)\n")

# låg = -10
# hög = 10

# for i in range(låg, hög, 2):
#     print(f"{i}", end = " ")

# #_____________________________________________________________________________

# print("\n" + "_"*100)
# print("\nUppgift 2 - Arithmetic sum(*).\n")

# sum = 0
# for i in range(1,101):
#     sum = sum + i
# print(sum)

# print("\nb)\n")

# sum = 0
# for i in range(1, 101, 2):
#     sum += i
# print(sum)

# #______________________________________________________________________________________

# print("\n" + "_"*100)
# print("\nUppgift 3 - Multiplikation table(*).\n")

# for i in range(1, 10):
#     product = i * 6
#     print(f"{product}", end = " ")

# print("\nb)\n")

# table = int(input("Which table are you interested in?: "))
# start = int(input("Specify start of table: "))
# end = int(input("Specify end of table: "))

# for i in range(start, (end+1)):
#     product = i * table
#     print(product)

# print("\nc)\n")


# for x in range(11):
#     for y in range(11):
#         print(f"{y * x:4}", end ="")
#     print("")

# #______________________________________________________________________________________

# print("\n" + "_"*100)
# print("\nUppgift 3 - Faculty(*).\n")

# värde = int(input("Skriv in din siffra: "))
# produkt = 1

# for i in range(1, värde+1):
#     produkt *= i
#     i += 1
# print(produkt)

# #______________________________________________________________________________________

# print("\n" + "_"*100)
# print("\nUppgift 3 - Faculty(*).\n")

# import random as rnd

# fourdigitnumber = rnd.randint(1000, 10000)
# counter = 0

# for i in range(fourdigitnumber+1):
#     counter += 1
#     if i == fourdigitnumber:
#         print(f"Numret är {fourdigitnumber}!")
#         print(f"Det tog {counter} försök att hitta siffran!")

print("\n" + "_"*100)
print("\nUppgift 3 - Faculty(*).\n")

rice = 1
chessboard = 8 * 8

for i in range(1,chessboard+1):
    rice *= 2
print(f"{rice} number of grains.")
