#FÖRSTA EGENSKAPADE PROGRAMMET:

import random as rnd

antal_av_tal = 0
antal_kast = int(input("Skriv hur många kast du vill göra med tärningen: "))
antal_sidor = int(input("Hur många sidor vill du att tärningen ska ha?: "))
valt_tal = int(input(f"Vilken siffra vill du jag ska räkna antalet av, mellan 1-{antal_sidor}?: "))


for i in range(antal_kast):
    tärning=rnd.randint(1,antal_sidor)
    if tärning == valt_tal:
        antal_av_tal += 1

procent = (antal_av_tal/antal_kast)*100

print(f"Av {antal_kast} kast med en {antal_sidor}-sidig tärning blev det {antal_av_tal} {valt_tal}:or.")
print(f"Sannolikheten för {valt_tal} är ca {procent:.2f}%.")