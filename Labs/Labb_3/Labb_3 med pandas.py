import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data_path = r"C:\Users\Sebastian!\Documents\Programmering\python-programmering-SEBASTIAN-PETERSSON\Labs\Labb_3"
k = -1
m = 0

def label_datapoints(k, m, xCoord, yCoord):
    
    my_splitting_line = k * xCoord + m
    if yCoord > my_splitting_line:
        label = 1
    else:
        label = 0
    return label


raw_datapoints = pd.read_csv(rf"{data_path}\unlabelled_data.csv", header = None)
raw_datapoints[2] = raw_datapoints.apply(lambda line: label_datapoints(k, m, line[0], line[1]))
