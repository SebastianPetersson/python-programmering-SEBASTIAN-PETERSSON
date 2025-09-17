#print("Uppgift 1")

#1. Check sign (*)
#Ask the user to input a number and check if this number is positive, negative or zero and print it.
#
#nummer = int(input("Skriv in ett nummer så säger jag om det är positivt, noll eller negativt: "))
#
#if nummer>0:
#    print("Ditt nummer är positivt.")
#elif nummer<0:
#    print("Ditt nummer är negativt.")
#elif nummer == 0:
#    print("Ditt nummer är 0.")
#
#Uppgift 2_____________________________

#print("Uppgift 2")

#a = int(input("Skriv in en siffra: "))
#b = int(input("Skriv in en siffra till, så ska jag berätta för dig vilken som är minst: "))
#
#if a < b:
#    print(f"Siffran a: {a:.0f}, var mindre än siffran b: {b:.0f}. Tack för dina siffror.")
#
#if a > b:
#    print(f"Siffran b: {b:.0f}, var mindre än siffran a: {a:.0f}. Tack för dina siffror.")

#Uppgift 3
#3. Right angle (*)
#Ask the user to input three angles and check if the triangle has a right angle. Your code should make sure that all three angles are valid and make up a triangle.

#Egen version:
#print("Du ska nu få skriva in tre vinklar som tillsammans skapar en triangel, alltså 180 grader.")
#x = int(input("Skriv in din första vinkel: "))
#y = int(input("Skriv in din andra vinkel: "))
#z = int(input("Skriv in din tredje vinkel: "))
#
#
#if (x + y + z) == 180:
#    print("Dina vinklar är tillsammans 180 grader och bildar en triangel.")
#else:
#    print("Dina vinklar skapar inte en triangel...")
#
#if 90 in(x, y, z):
#    print("Triangeln är rätvinklig eftersom en av vinklarna är 90 grader.")

#Förbättrad version:

#print("Du ska nu få skriva in tre vinklar som tillsammans skapar en triangel, alltså 180 grader.")
#
#angles = [
#    int(input("Skriv in din första vinkel: ")),
#    int(input("Skriv in din andra vinkel: ")),
#    int(input("Skriv in din tredje vinkel: "))
#]
#
#if sum(angles) == 180:
#    print("Din triangel är korrekt.")
#    if 90 in angles:
#        print("Din triangel är rätvinklig.")
#else:
#    print("Din triangel är inkorrekt.")

#Uppgift 4: Medicine_______________

#print("Uppgift 4.")

#age = int(input("Skriv in din ålder: "))
#vikt = int(input("Skriv in din vikt: "))
#
#if vikt > 40:
#    if age >= 12:
#        print("Du ska ta 1-2 tabletter.")
#    else:
#        print("Du är under 12 men väger över 40 kg, kontakta läkare.")
#elif 26 <= vikt < 40:
#    if age >= 3:
#        print("Du ska ta 1/2-1 tablett.")
#    else:
#        print("Din ålder är för låg, kontakta läkare.")
#elif 15 <= vikt <= 25:
#    if age >= 3:
#        print("Du ska ta 1/2 tablett.")
#    else:
#        print("Din ålder är för låg, kontakta läkare.")

#Uppgift 5_______________
#print ("Uppgift 5.")
#
#num = int(input("Skriv in ett valfritt tal: "))
#
#if num % 5 == 0 and num % 2 != 0:
#    print(f"Ditt tal {num} är delbart med 5 och udda.")
#elif num % 5 == 0 and num % 2 == 0:
#    print(f"Ditt tal {2} är delbart med 5 och jämnt.")
#elif num % 2 == 0:
#    print(f"Ditt tal är jämnt.")
#elif num % 2 != 0:
#    print(f"Ditt tal är udda.")

#Uppgift 6:_____________
print("Uppgift 6.")

we = int(input("Skriv in väskans vikt kg: "))
le = int(input("Skriv in väskans längd i cm: "))
wi = int(input("Skriv in väskans bredd i cm: "))
he = int(input("Skriv in väskans höjd i cm: "))

if le <= 55 and wi <= 40 and he <= 23:
    if we <= 8:
        print("Din väska håller sig inom måtten.")
    else:
        print("Din väska är för tung.")
else:
    if le > 55:
        print("Din väska är för lång.")
    elif wi > 40:
        print("Din väska är för bred.")
    elif he > 23:
        print("Din väska är för hög.")



    




        



