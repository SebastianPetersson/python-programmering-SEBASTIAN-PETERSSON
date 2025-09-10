#Uppgift 1

print("Uppgift 1a)\n")

import math 

a = 3
b = 4

c = math.sqrt(a**2 + b**2)

print(f"Med kateterna {a} cm och {b} cm blir hypotenusan {c:.1f} cm.\n")

#_______________________________________________________________________

print("Uppgift 1b)\n")

a = 5.0
c = 7.0

b = math.sqrt(c**2 - a**2)

print(f"Längden av katetern b är {b:.1f} cm.\n")

#_______________________________________________________________________

print("Uppgift 2)\n")

x = 300
y = 365

accuracy = 300/365
procent= accuracy*100

print(f"Träffsäkerheten av modellen är {procent:.2f}%.")

