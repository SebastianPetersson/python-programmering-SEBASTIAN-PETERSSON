import numpy as np
import matplotlib.pyplot as plt
import random as rnd
datapoints_path = r"C:\Users\Sebastian!\Documents\Programmering\python-programmering-SEBASTIAN-PETERSSON\Labs\Labb_2\datapoints.txt"
k = 10
n_simulations = 10

#Cleaning and packing datapoints.txt into clean_data
clean_data = []
with open(datapoints_path, "r") as tr_file:
    next(tr_file)
    for line in tr_file:
        row = [float(value) for value in line.split(",")]
        clean_data.append(row)

#Separating pichu and pikachu into separate groups.
pichu = [(w,h,label) for (w,h,label) in clean_data if label == 0]
pikachu = [(w,h,label) for (w,h,label) in clean_data if label == 1]

def euclidean_distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return np.sqrt(dx**2 + dy**2)

actual_label = []
predicted_label = []

def classify_pokemon(test_set, training_set, k=10):

    actual_label.clear()
    predicted_label.clear()

    for test_data in test_set:
        distances = []
        test_coordinates = test_data [:2]
        test_label = test_data[2]
        actual_label.append(test_label)

        for training_data in training_set:
            train_coordinates = training_data[:2]
            label = training_data[2]
            distance = euclidean_distance(test_coordinates, train_coordinates)
            distances.append((distance, label))
        #Sorts distances and extracts predicted labels from the k nearest.
        distances.sort(key = lambda x: x[0])                          
        k_nearest = distances[:k]
        labels = [label for distance, label in k_nearest]
        prediction = max(set(labels), key=labels.count)             
        predicted_label.append(prediction)
    return predicted_label

accuracy = []
for i in range(n_simulations):

    #Each simulation: shuffling initial lists, making new sets, and shuffling the sets.
    rnd.shuffle(pichu)
    rnd.shuffle(pikachu)
    training_set = pichu [:50] + pikachu [:50]
    test_set = pichu [50:] + pikachu [50:]
    rnd.shuffle(training_set)
    rnd.shuffle(test_set)
    #Runs the classifier each time.
    predictions = classify_pokemon(test_set, training_set, k)
    
    TP = sum(1 for a, p in zip(actual_label, predicted_label) if a == 1 and p == 1)
    TN = sum(1 for a, p in zip(actual_label, predicted_label) if a == 0 and p == 0)

    acc = (TP + TN)/len(actual_label)
    accuracy.append(acc)

mean_accuracies = np.mean(accuracy)
print(f"The mean of the accuracy through 10 simulations is {mean_accuracies*100:.2f} %.")

#Visuals
plt.plot(accuracy, marker = "o", linestyle = ':', color = "crimson", label = "Accuracies")
plt.axhline(mean_accuracies, linestyle = ":", color = "navy", label= "Mean")
plt.title("Lab 2 - Uppg. 3 & 4.")
plt.xlabel("Number of simulations.")
plt.ylabel("Accuracy")
plt.xlim(0, n_simulations-1)
plt.ylim(0.8, 1)
plt.grid(True, linestyle = ":", )
plt.legend(loc="lower left")
plt.show()