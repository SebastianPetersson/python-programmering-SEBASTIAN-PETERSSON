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

print(f"Träffsäkerheten av modellen är {procent:.2f}%.\n")

#_______________________________________________________________________

print("Uppgift 3\n")

tp = 2
fp = 2
fn = 11
tn = 985

accuracy = (tp+tn)/(tp+tn+fn+fp)

print(f"Träffsäkerheten av ml-modellen är {accuracy*100}%.\n")

#_______________________________________________________________________

print("Uppgift 4\n")

#Punkter A: (4,4), B (0,1).

x1=4
y1=4
x2=0
y2=1

k = (y2-y1)/(x2-x1)
m = y2-k*x2

print(f"Formeln för linjen är y={k}x+{m:.0f}.\n")

#_______________________________________________________________________

print("Uppgift 5)\n")

p1 = (3, 5)
p2 = (-2, 4)

distance = math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)

print(f"Längden är ungefär {distance:.1f} l.u.\n")

#_______________________________________________________________________

print("Uppgift 5)\n")

p1(2, 1, 4)
p2(3, 1, 0)

distance = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

print(distance)
