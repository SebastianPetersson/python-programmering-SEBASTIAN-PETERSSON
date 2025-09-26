import numpy as np
import matplotlib.pyplot as plt
import random as rnd

datapoints_path = r"C:\Users\Sebastian!\Documents\Programmering\python-programmering-SEBASTIAN-PETERSSON\Labs\datapoints.txt"

#Cleaning and packing datapoints.txt into training_data.
clean_data = []
with open(datapoints_path, "r") as tr_file:
    next(tr_file)
    for line in tr_file:
        row = [float(value) for value in line.split(",")]
        clean_data.append(row)

pichu = [(w,h) for (w,h,label) in clean_data if label == 0]
pikachu = [(w,h) for (w,h,label) in clean_data if label == 1]

training_set = pichu [:50] + pikachu [:50]
test_set = pichu [50:] + pikachu [50:]

rnd.shuffle(training_set)
rnd.shuffle(test_set)
print(test_set)


# pichu_x, pichu_y = zip(*pichu)
# pikachu_x, pikachu_y = zip(*pikachu)