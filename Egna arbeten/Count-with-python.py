#ÖVNINGSUPPGIFTER - RÄKNING MED PYTHON

# A right  angled triangle has the catheti: a = 3 and b = 4 length units. 
# Compute the hypothenuse of the triangle. (*) Första Lösning

import math

print("Uppgift 1a")
#a = 3.0
#b = 4.0
#print(f"Längden av hypotenusan är", math.sqrt(a**2 + b**2))

#Annan version, beräkna_hypotenusa definieras som en funktion och använder math.hypot (inbyggd funktion) för att räkna ut hypotenusan. 
def beräkna_hypotenusa (a: float, b: float) -> float:
    return math.hypot(a, b)

a = 3.0
b = 4.0
hypotenusa = beräkna_hypotenusa(a, b)

print(f"Längden av hypotenusan är {hypotenusa:.1f} cm.")

#__________________________________
print("Uppgift 1b")

#Uppgift 2: b)   A right angled triangle has hypothenuse c = 7.0 and a cathetus a = 5.0 length units. 
# Compute the other cathetus and round to one decimal. (*)

a = 5.0
c = 7.0
b = math.sqrt(c**2-a**2)

print(f"Längden av den andra katetern är: {b:.1f}")

#__________________________________
print("Uppgift 2")
#2. Classification accuracy (*)
#A machine learning algorithm has been trained to predict whether or not it would rain the next day. 
# Out of 365 predictions, it got 300 correct, compute the accuracy of this model.

correct_predictions = 300
total_predictions = 365
accuracy = (correct_predictions/total_predictions)
percentage = accuracy * 100

print(f"Träffsäkerheten av ML-algoritmen är: {percentage:.1f}%")

#__________________________________
print("Uppgift 3")

#Classification accuracy, uträknat från en matris.

True_positive = TP = 2
True_negative = TN = 985
False_positive = FP = 2
False_negative = FN = 11

accuracy = (TP + TN)/(TP + TN + FP + FN)

percentage = accuracy * 100

print(f"Träffsäkerheten av modellen är: {percentage:.2f}%")

#__________________________________
print("Uppgift 4")

#Compute the slope and the constant term of this line using the points A (4,4) and B (0,1).

x1 = 4
y1 = 4
x2 = 0
y2 = 1

k = (y2-y1)/(x2-x1)
m = y2-k*x2

print(f"Formeln för linjen är y={k:.2f}x+{m:.0f}")

#_________________________________
print("Uppgift 5")

#The Euclideam distance between the points P1 and P2 is the length of a line between them. 
# Let P1: (3,5) and P2: (-2,4) and compute the distance between them.

#P1
x1 = 3
y1 = 5
x2 = -2
y2 = 4

distance = math.sqrt((x2 - x1)**2+(y2 - y1)**2)

print(f"Längden mellan P1 och P2 är ungefär {distance:.1f} cm.")

#________________________________
print("Uppgift 6")

#Calculate the distance between the points P1: (2, 1, 4) and P2: (3, 1, 0)

#P1 = (p1, p2, p3) & P2 = (q1, q2, q2)

#p1 = 2
#p2 = 1
#p3 = 4
#q1 = 3
#q2 = 1
#q3 = 0
#
#distance = math.sqrt((p1-q1)**2 + (p2-q2)**2 + (p3-q3)**2)
#
#print(f"Längden mellan P1 & P2 är {distance:.2f} l.u.")

#p = (2, 1, 4)
#q = (3, 1, 0)
#
#distance = math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2 + (p[2]-q[2])**2)
#
#print (f"Längden mellan P1 och P2 är {distance:.2f} l.u.")





