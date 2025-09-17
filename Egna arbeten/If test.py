# name = input("Skriv in ditt namn: ")
# kön = input("Skriv in ditt kön (man/kvinna): ")

# print(f"God morgon herr {name}") if kön == "man" else print(f"God morgon fru {name}")

name = input("Skriv in ditt namn: ")


while True:
    kön = input("Skriv in ditt kön (man/kvinna): ").lower()
    if kön == "man": 
        print(f"God morgon herr {name}.")
        break
    elif kön == "kvinna":
        print(f"God morgon fru {name}.")
        break
    else:
        print(f"Du skrev in {kön}, det är inget kön. Prova igen.")

while True: 
    fråga = input("Får jag ställa en fråga? ja/nej: ").lower()
    if fråga == "ja":
        mående = input("Hur mår du idag? bra/dåligt: ").lower()
        if mående == "bra": 
            print("Fint att du mår {mående}!")
            break
        elif mående == "dåligt":
            print("Skit och! Blir bättre ska du se.")
            break
    elif fråga == "nej":
        print(f"Fattar, tråkigt att höra men du får ha en bra dag, {name}.")
        break
    else: 
        print(f"Dra åt helvete va du skriver dåligt, försök igen.")