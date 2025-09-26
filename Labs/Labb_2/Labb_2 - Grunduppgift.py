import numpy as np
import matplotlib.pyplot as plt

datapoints_path = r"C:\Users\Sebastian!\Documents\Programmering\python-programmering-SEBASTIAN-PETERSSON\Labs\Labb_2\datapoints.txt"
testpoints_path = r"C:\Users\Sebastian!\Documents\Programmering\python-programmering-SEBASTIAN-PETERSSON\Labs\Labb_2\testpoints.txt"

#Cleaning and packing datapoints.txt into new list training_data.
training_data = []
with open(datapoints_path, "r") as tr_file:
    next(tr_file)
    for line in tr_file:
        row = [float(value) for value in line.split(",")]
        training_data.append(row)

#Cleaning of test data, and packing them into the list test_data.
test_data = []
with open(testpoints_path, "r") as te_file:
    next(te_file)
    for line in te_file:
        row = [float(value.split(". ", 1)[-1].strip().strip("()")) for value in line.split(",")]
        test_data.append(row)

#Separating by labels.
pichu = [(w,h) for (w,h,label) in training_data if label == 0]
pikachu = [(w,h) for (w,h,label) in training_data if label == 1]
test_data_points = [(w,h) for (w,h) in test_data]

def euclidean_distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return np.sqrt(dx**2 + dy**2)

#Classify the 1 nearest neighbor
def classify_test(test_point, training_data):
    distances =[]

    for data_point in training_data:
        train_coordinates = data_point[:2]
        label = data_point[2]
        distance = euclidean_distance(test_point, train_coordinates)
        distances.append((distance, label))

    _, nearest_label = min(distances, key=lambda x: x[0])
    return nearest_label

predictions = []

for point in test_data_points:
    pred = classify_test(point, training_data)
    predictions.append(pred)

for i, prediction in enumerate(predictions, start = 1):
    if prediction == 0:
        print(f"Testdata {i} är närmast en Pichu.")
    else:
        print(f"Testdata {i} är närmast en Pikachu.")

#Unzipping coordinates for Plotting.
pichu_x, pichu_y = zip(*pichu)
pikachu_x, pikachu_y = zip(*pikachu)
test_x, test_y = zip(*test_data_points)

#Visuals.
colors = ["crimson" if pred == 0 else "yellow" for pred in predictions]
plt.scatter(pichu_x, pichu_y, color = "crimson", edgecolor = "black", alpha = 0.7, label = "Pichu(0)")
plt.scatter(pikachu_x, pikachu_y, color = "yellow", edgecolor = "black", alpha = 0.7, label = "Pikachu(1)")
plt.scatter(test_x, test_y, color = colors, edgecolor = "black", alpha = 0.6, s = 50, label = "Testpoints", marker = "D")
plt.title("Labb 2 - Pichu eller Pikachu")
plt.xlabel("Width(cm)")
plt.ylabel("Height(cm)")
plt.grid(True, linestyle = ":", )
plt.legend(loc="upper left")
plt.show()