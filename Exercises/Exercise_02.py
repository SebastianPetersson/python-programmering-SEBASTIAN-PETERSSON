#While_statements_exercise_02

print("Uppgift 1 - Count numbers(*)\n")

i = -10

while i <= 10:
    print(f"{i}", end = " ")
    i += 1

#_____________________________________________________________________________

print("\n" + "_"*100)
print("\nUppgift 2 - Arithmetic sum (*)\n" + "\na)\n")

summa = 0
n = 1

while n <= 100:
    summa += n
    if n < 100:
        print(f"{n} ", end = "+ ")
    else:
        print(f"{n} ", end = "= ")
    n += 1
print(summa)

print("\nb)\n")

summa = 0
n = 1

while n <= 100:
    summa += n
    if n < 99:
        print(f"{n} ", end = "+ ")
    else:
        print(f"{n} ", end = "= ")
    n += 2
print(summa)


#___________________________________________________________________________________

print("\n" + "_"*100)
print("\nUppgift 3 - Guess number game (*)\n" + "\na)\n")





