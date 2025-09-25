import math

import numpy as np
import matplotlib.pyplot as plt
import re

def read_test_points(filename):
    with open(filename, 'r') as f:
        text = f.read()

    matches = re.findall(r"\(([^)]*)\)", text)
    return [(float(match[0].strip()), float(match[1].strip())) for match in map(lambda m: m.split(','), matches)]


def distance(p1, p2) -> float:
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def split_data(data):
    pichu = [(x, y) for (x, y, n) in data if n == 0]
    pikachu = [(x, y) for (x, y, n) in data if n == 1]

    return pichu, pikachu


def plot_points(pichu, pikachu):
    # Unpack tuples into x and y lists
    x1, y1 = zip(*pichu)
    x2, y2 = zip(*pikachu)

    # Scatter plot
    plt.scatter(x1, y1, color="blue", label="Pichu", marker="o")
    plt.scatter(x2, y2, color="red", label="Picachu", marker="x")

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Two Datasets as Points")
    plt.legend()
    plt.show()


def classify(test_points, pichu, pikachu):
    for p in test_points:
        d_pichu = min(map(lambda x: distance(x, p), pichu))
        d_pikachu = min(map(lambda x: distance(x, p), pikachu))

        character_type = 'Pichu' if d_pichu < d_pikachu else 'Pikachu'
        print(f'Sample with (width, height): {p} classified as {character_type}')


def main():
    data = np.genfromtxt(r"C:\Users\Sebastian!\Documents\Programmering\python-programmering-SEBASTIAN-PETERSSON\Labs\datapoints.txt", delimiter=',', names=True)
    test_points = read_test_points(r"C:\Users\Sebastian!\Documents\Programmering\python-programmering-SEBASTIAN-PETERSSON\Labs\testpoints.txt")

    pichu, pikachu = split_data(data)

    plot_points(pichu, pikachu)

    classify(test_points, pichu, pikachu)


main()