import matplotlib.pyplot as plt
import pandas as pd
data_path = r"C:\Users\Sebastian!\Documents\Programmering\python-programmering-SEBASTIAN-PETERSSON\Labs\Labb_3"
write_path = rf"{data_path}\Labelled_data.csv"
k = -1
m = 0

def label_datapoints(k, m, x, y):
    
    if y > k * x + m:
        label = 1
    else:
        label = 0
    return label

datapoints = pd.read_csv(rf"{data_path}\unlabelled_data.csv", header = None, names = ['x', 'y'])
datapoints['label'] = datapoints.apply(lambda line: label_datapoints(k, m, line['x'], line['y']), axis = 1) #Här hade man kunnat göra en vektoriserad version, vilket är mycket snabbare än att iterera över varje rad.

with open(rf"{write_path}", 'w', newline='') as labelledData:
    datapoints.to_csv(labelledData, index = False)

x_min, x_max = datapoints['x'].min(), datapoints['x'].max()
x_values = [x_min, x_max]
y_values = [k*x+m for x in x_values]

print("Labelled_data.csv has been written with classified datapoints.")

colors = ['crimson' if label == 1 else 'navy' for label in datapoints['label']]
plt.scatter(datapoints['x'], datapoints['y'], color = colors, s = 10)
plt.plot((x_values),(y_values), color = 'gold', label = 'My splitting line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Linjär klassificering")
plt.xlim(-6,6)
plt.ylim(-6,6)
plt.grid(True)
plt.legend(loc = "upper left")
plt.show()