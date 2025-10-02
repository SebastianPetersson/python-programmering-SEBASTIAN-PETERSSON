import matplotlib.pyplot as plt
import pandas as pd
data_path = rf"C:\Users\Sebastian!\Documents\Programmering\python-programmering-SEBASTIAN-PETERSSON\Labs\Labb_3"
write_path = rf"{data_path}\Labelled_data.csv"
k = -1
m = 0

def label_datapoints(k, m, x, y):
    
    if y > k*x + m:
        label = 1
    else:
        label = 0
    return label

datapoints = pd.read_csv(rf"{data_path}\unlabelled_data.csv", header = None, names = ['x', 'y'])
datapoints['label'] = datapoints.apply(lambda line: label_datapoints(k, m, line['x'], line['y']), axis = 1) #Kolla upp vektorisering, bättre för större dataset.

with open(rf"{write_path}", 'w', newline='') as labelledData:
    datapoints.to_csv(labelledData, index = False)

print("Classified datapoints has been written to 'Labelled_file.csv'")
count = datapoints['label'].value_counts()
print(count)

#Plotting
x_min, x_max = datapoints['x'].min(), datapoints['x'].max()
x_values = [x_min, x_max]
y_values = [k*x + m for x in x_values]
above = datapoints[datapoints['label'] == 1]
below = datapoints[datapoints['label'] == 0]

plt.scatter(above['x'], above['y'], color = 'crimson', s = 10)
plt.scatter(below['x'], below['y'], color = 'navy', s = 10)
plt.plot((x_values),(y_values), color = 'gold', label = 'My splitting line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Linjär klassificering")
plt.grid(True, linestyle = ':')
plt.legend(loc = "upper left")
plt.show()