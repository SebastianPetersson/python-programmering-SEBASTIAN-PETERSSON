# #While_statements_exercise_02

# print("Uppgift 1 - Count numbers(*)\n")

# i = -10

# while i <= 10:
#     print(f"{i}", end = " ")
#     i += 1

# #_____________________________________________________________________________

# print("\n" + "_"*100)
# print("\nUppgift 2 - Arithmetic sum (*)\n" + "\na)\n")

# summa = 0
# n = 1

# while n <= 100:
#     summa += n
#     if n < 100:
#         print(f"{n} ", end = "+ ")
#     else:
#         print(f"{n} ", end = "= ")
#     n += 1
# print(summa)

# print("\nb)\n")

# summa = 0
# n = 1

# while n <= 100:
#     summa += n
#     if n < 99:
#         print(f"{n} ", end = "+ ")
#     else:
#         print(f"{n} ", end = "= ")
#     n += 2
# print(summa)


#___________________________________________________________________________________

# print("\n" + "_"*100)
# print("\nUppgift 3 - Guess number game (*)\n" + "\na)\n")

# import random as rnd

# siffra = rnd.randint(1, 100)
# gissning = int(input("Gissa en siffra mellan 1-100: "))
# antal_gissning = 1

# while gissning != siffra:
#     antal_gissning += 1
#     if siffra > gissning:
#         print("Bra gissning, men siffran är högre.")
#     else:
#         print("Bra gissning, men siffran är lägre.")
#     gissning = int(input("Försök igen: "))


# if antal_gissning < 7:
#     print(f"Snyggt, du gissade rätt!! Siffran var {siffra} och du klarade det på endast {antal_gissning} försök!")
# else:
#     print(f"Du gissade rätt! Siffran var {siffra} och du klarade det på {antal_gissning} försök.")

#___________________________________________________________________________________

print("\n" + "_"*100)
print("\nb)\n")

import random as rnd

siffra = rnd.randint(1, 1000)
lägsta = 1
högsta = 1000
antal_gissningar = 0

while True:
    gissning = (lägsta+högsta)//2
    antal_gissningar += 1
    print(f"Jag gissar att siffran är {gissning}.")

    if gissning < siffra:
        print("För lågt, försök igen.")
        lägsta = gissning + 1
    elif gissning > siffra:
        print("För högt, försök igen.")
        högsta = gissning - 1
    else:
        print(f"Nice, jag gissade rätt. Siffran var {siffra} och det tog mig {antal_gissningar} försök.")
        break

