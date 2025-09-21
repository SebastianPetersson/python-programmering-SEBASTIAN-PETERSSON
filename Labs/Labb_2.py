import numpy as np
import matplotlib.pyplot as plt


training_data = []
test_data = []

#Clean the training data.
with open(r"C:\Users\Sebastian!\Documents\Programmering\python-programmering-SEBASTIAN-PETERSSON\Labs\datapoints.txt", "r") as tr_file:
    next(tr_file)
    for line in tr_file:
        row = [float(value.strip()) for value in line.split(",")]
        training_data.append(row)

#Clean the test data.
with open(r"C:\Users\Sebastian!\Documents\Programmering\python-programmering-SEBASTIAN-PETERSSON\Labs\testpoints.txt", "r") as te_file:
    next(te_file)
    for line in te_file:
        row = [float(value.split(". ", 1)[-1].strip().strip("()")) for value in line.split(",")]
        test_data.append(row)

#Packing pichu and pikachu data-rows in separate lists as (x, y).
pichu_data_points = [(w,h) for (w,h,n) in training_data if n == 0]
pikachu_data_points = [(w,h) for (w,h,n) in training_data if n == 1]
pichu_x, pichu_y = zip(*pichu_data_points)
pikachu_x, pikachu_y = zip(*pikachu_data_points)

test_data_points = [(w,h) for (w,h) in test_data]
test_x, test_y = zip(*test_data_points)



#Visuals
plt.scatter(pichu_x, pichu_y, color = "red", edgecolor = "black", alpha = 0.5, label = "Pichu(0)")
plt.scatter(pikachu_x, pikachu_y, color = "yellow", edgecolor = "black", alpha = 0.5, label = "Pikachu(1)")
plt.scatter(test_x, test_y, color = "blue", edgecolor = "black", alpha = 0.5, label = "Testpoints")


plt.title("Labb 2 - Pichu eller Pikachu")
plt.xlabel("Width(cm)")
plt.ylabel("Height(cm)")
plt.grid()
plt.legend()
plt.show()