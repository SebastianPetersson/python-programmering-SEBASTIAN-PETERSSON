import matplotlib.pyplot as plt
import numpy as np

data_path = r"C:\Users\Sebastian!\Documents\Programmering\python-programmering-SEBASTIAN-PETERSSON\Labs\Labb_3\unlabelled_data.csv"
clean_data = []

with open(data_path, "r") as unlabelled_data:
    for line in unlabelled_data:
        data = [float(value) for value in line.split(",")]
        clean_data.append(data)

def separate_datapoints(clean_data):
    
    above_list = []
    below_list = []
    m=0
    k=-1

    for x, y in clean_data:
        
        split_line = k * x + m
        if y > split_line:
            above_list.append((x, y, 1))
        else: 
            below_list.append((x, y, 0))
    return above_list, below_list

above_list, below_list = separate_datapoints(clean_data)

labelled_list = (above_list + below_list)
with open("Labelled_data.csv", "w") as labelled_data:
    for x, y, label in labelled_list:
        labelled_data.write(f"{x}, {y}, {label}\n")

ax, ay, _ = zip(*above_list)
bx, by, _ = zip(*below_list)

plt.scatter(ax, ay, color = "navy", s = 10, label = "datapoints above line.")
plt.scatter(bx, by, color = "crimson", s = 10, label = "datapoints below line")
plt.axline((-2,2), (2,-2), color = "gold", label = "Splitting line")
plt.grid(True, linestyle = ":")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Labelled data.")
plt.show()

