import numpy as np
import matplotlib.pyplot as plt
import random as rnd

datapoints_path = r"C:\Users\Sebastian!\Documents\Programmering\python-programmering-SEBASTIAN-PETERSSON\Labs\datapoints.txt"

def get_user_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("The value must be a positive number.")
                continue
            return value
        except ValueError:
            print("You must input a number, please try again.")

user_data = []
user_width = get_user_input("Input your Pokemons width: ")
user_height = get_user_input("Input your Pokemons height: ")
user_data.append((user_width, user_height))

#Cleaning and packing datapoints.txt into new list training_data.
training_data = []
with open(datapoints_path, "r") as tr_file:
    next(tr_file)
    for line in tr_file:
        row = [float(value) for value in line.split(",")]
        training_data.append(row)

pichu = [(w,h) for (w,h,label) in training_data if label == 0]
pikachu = [(w,h) for (w,h,label) in training_data if label == 1]
pichu_x, pichu_y = zip(*pichu)
pikachu_x, pikachu_y = zip(*pikachu)
user_x, user_y = zip(*user_data)

def euclidean_distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return np.sqrt(dx**2 + dy**2)

#Classify the k nearest neighbor
def classify_testpoint(user_data, training_data, k=10):
    distances =[]

    for data_point in training_data:
        train_coordinates = data_point[:2]
        label = data_point[2]
        distance = euclidean_distance(user_data, train_coordinates)
        distances.append((distance, label))

    distances.sort(key=lambda x: x[0])
    k_nearest = distances[:k]
    labels = [label for distance, label in k_nearest]
    prediction = max(set(labels), key=labels.count)
    return prediction

k = int(input("Hur många datapunkter vill du jämföra med?: "))
predictions = []

for point in user_data:
    pred = classify_testpoint(point, training_data, k)
    predictions.append(pred)
    

for prediction in predictions:
    if prediction == 0:
        print(f"Din pokemon är en Pichu.")
    else:
        print(f"Din pokemon är en Pikachu.")

print(predictions)

#plotting
colors = ["crimson" if p == 0 else "yellow" for p in predictions]
plt.scatter(pichu_x, pichu_y, color = "crimson", edgecolor = "black", alpha = 0.7, label = "Pichu(0)")
plt.scatter(pikachu_x, pikachu_y, color = "yellow", edgecolor = "black", alpha = 0.7, label = "Pikachu(1)")
plt.scatter(user_x, user_y, color = colors, edgecolor = "black", alpha = 0.8, s = 50, label = "User Pokemon", marker = "D")
plt.title("Lab 2 - Pichu or Pikachu")
plt.xlabel("Width(cm)")
plt.ylabel("Height(cm)")
plt.grid(True, linestyle = ":", )
plt.legend(loc="upper left")
plt.show()