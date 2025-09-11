#Exercise_01_If_statement_exercises

print("Uppgift 1: Check sign(*)\n")

n = int(input("Skriv in ett nummer: "))

if n < 0:
    print(f"Du skrev {n}, det är ett negativt tal.")

elif n > 0:
    print(f"Du skrev {n}, det är ett positivt tal.")

else:
    print("Ditt nummer är 0.")

#__________________________________________________________________________________________________________

print("\nUppgift 2: Smallest(*)\n")

print("I det här programmet kommer du få skriva in två siffror. Jag kommer därefter avgöra vilken av de som är minst.")

x = float(input("Skriv in din första siffra: "))
y = float(input("Skriv in din andra siffra: "))

if x < y:
    print(f"Du skrev in siffrorna {x} och {y}. Den första, {x}, är minst.")
elif y < x:
    print(f"Du skrev in siffrorna {x} och {y}. Den senare, {y}, är minst.")
else:
    print(f"Du skrev in siffrorna {x} och {y}, de är lika stora.")

#__________________________________________________________________________________________________________

print("\nUppgift 3: Right angle(*)\n")

print("I det här programmet kommer du skriva tre valfria vinklar som tillsammans bildar en triangel.\n Jag kommer sedan kontrollera om det är en triangel samt om den är rätvinklig eller ej.")
a = int(input("Skriv in din första vinkel: "))
b = int(input("Skriv in din andra vinkel: "))
c = int(input("skriv in din sista vinkel: "))

if (a+b+c) == 180:
    print(f"De tre vinklarna {a}, {b} och {c} är korrekta och skapar en triangel.")
    if a == 90 or b == 90 or c == 90:
        print("Triangeln är rätvinklig.")
    else:
        print("Triangeln är inte rätvinklig.")
else:
    print("Något är fel med vinklarna, de skapar inte en triangel.")

# __________________________________________________________________________________________________________

print("\nUppgift 4: Medicine(*)\n")

print("Skriv in hur gammal du är och hur mycket du väger, så kommer du få en rekommenderad dos.")
age = int(input("Hur gammal är du?: "))
weight = int(input("Hur mycket väger du?: "))

if age > 12:
    if weight >= 40:
        print("Din rekommenderade dos är 1-2 tabletter.")
    else:
        print("Kontakta läkare för förnyad rekommenderad dos.")
elif age >= 3:

    if weight > 40:
        print("Kontakta läkare.")
    elif weight >= 26:
        print("Din rekommenderade dos är 1/2-1 tablett.")
    elif weight >= 15:
        print("Din rekommenderade dos är 1/2 tablett.")
    else:
        print("Kontakta läkare.")
else:
    print("Du är för ung för att käka tabletterna.")

# __________________________________________________________________________________________________________

print("\nUppgift 5: Divisible(*)\n")

siffra = int(input("Skriv in en siffra så ska du få veta om den är jämn eller udda, samt om den är delbar med fem: "))

if siffra % 2 != 0 and siffra % 5 == 0:
    print(f"Din siffra {siffra} är udda och delbar med fem.")
elif siffra % 2 == 0 and siffra % 5 == 0:
    print(f"Din siffra {siffra} är jämn och delbar med fem.")
elif siffra % 2 == 0:
    print(f"Din siffra {siffra} är jämn.")
else:
    print(f"Din siffra {siffra} är udda.")

# __________________________________________________________________________________________________________

print("\nUppgift 6: Luggage size(*)\n")

we = int(input("Skriv in väskans vikt: "))

if we <= 8:
    le = int(input("Skriv in väskans längd: "))
    wi = int(input("Skriv in väskans bredd: "))
    he = int(input("Skriv in väskans höjd: "))
    
    if le <= 55 and wi <= 40 and he <= 23:
          print("Din väska är godkänd!")
    else:
          print("Din väska är okej i vikt men håller sig inte inom måtten.")
else:
        print("Din väska är för tung.")
