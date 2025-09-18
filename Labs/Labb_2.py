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


print(training_data)
print(test_data)


