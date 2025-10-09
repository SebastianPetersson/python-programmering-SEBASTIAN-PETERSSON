import matplotlib.pyplot as plt
import numpy as np
import csv
data_path = r"C:\Users\Sebastian!\Documents\Programmering\python-programmering-SEBASTIAN-PETERSSON\Labs\Labb_3\unlabelled_data.csv"
clean_data = []
k = -1
m = 0

with open(data_path, "r") as unlabelled_data:
    reader = csv.reader(unlabelled_data)
    for row in reader:
        x, y = float(row[0]), float(row[1])
        clean_data.append((x,y))

def classify_datapoints(clean_data, k, m):

    above_list = []
    below_list = []
    for x, y in clean_data:
        
        my_split_line = k*x+m
        if y > my_split_line:
            above_list.append((x, y, 1))
        else: 
            below_list.append((x, y, 0))
    return above_list, below_list

above_list, below_list = classify_datapoints(clean_data, k, m)

labelled_list = (above_list + below_list)
with open("Labelled_data.csv", "w") as labelled_data:
    for x, y, label in labelled_list:
        labelled_data.write(f"{x}, {y}, {label}\n")

#For plotting
ax, ay, _ = zip(*above_list)
bx, by, _ = zip(*below_list)
all_x = list(ax) + list(bx)
x_line = np.linspace(min(all_x), max(all_x))
y_line = k * x_line + m

print(len(above_list))
print(len(below_list))

plt.scatter(ax, ay, color = "navy", s = 10, label = "datapoints above line.")
plt.scatter(bx, by, color = "crimson", s = 10, label = "datapoints below line")
plt.plot(x_line, y_line, color = "gold", label = "My splitting line")
plt.grid(True, linestyle = ":")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Labelled data.")
plt.show()
