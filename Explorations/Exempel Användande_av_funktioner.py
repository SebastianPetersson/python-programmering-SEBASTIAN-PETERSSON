import numpy as np
import matplotlib.pyplot as plt

# ====== Filhämtning ======

tr_data_path = r"C:\Users\Sebastian!\Documents\Programmering\python-programmering-SEBASTIAN-PETERSSON\Labs\datapoints.txt"
te_data_path = r"C:\Users\Sebastian!\Documents\Programmering\python-programmering-SEBASTIAN-PETERSSON\Labs\testpoints.txt"

def load_train_data():
    training_data = []
    with open(tr_data_path, "r") as tr_file:
        next(tr_file)  # hoppa över header
        for line in tr_file:
            row = [float(value.strip()) for value in line.split(",")]
            training_data.append(row)
    return training_data

def load_test_data():
    test_data = []
    with open(te_data_path, "r") as te_file:
        next(te_file)
        for line in te_file:
            row = [float(value.split(". ", 1)[-1].strip().strip("()")) for value in line.split(",")]
            test_data.append(row)
    return test_data

# ====== Avståndsberäkning ======
def euclidean_distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return np.sqrt(dx**2 + dy**2)

# ====== Klassificering (närmsta granne) ======
def classify_point(point, training_data):
    distances = []
    for train_point in training_data:
        dist = euclidean_distance(point, train_point[:2])
        label = train_point[2]  # sista kolumnen = klass
        distances.append((dist, label))
    
    distances.sort(key=lambda x: x[0])  # sortera på avstånd
    nearest = [label for _, label in distances[2]]
    
    # majoritetsröstning
    return max(set(nearest), key=nearest.count)

# ====== Plottning ======
def plot_data(training_data, test_data, predictions):
    # splitta träningsdata
    pikachu = [p for p in training_data if p[2] == 1]
    pichu = [p for p in training_data if p[2] == 0]

    plt.scatter([p[0] for p in pikachu], [p[1] for p in pikachu], c="yellow", label="Pikachu (train)")
    plt.scatter([p[0] for p in pichu], [p[1] for p in pichu], c="blue", label="Pichu (train)")

    # testpunkter
    for point, label in zip(test_data, predictions):
        color = "orange" if label == 1 else "cyan"
        plt.scatter(point[0], point[1], c=color, edgecolors="black", marker="x", s=100)

    plt.xlabel("Width")
    plt.ylabel("Height")
    plt.legend()
    plt.show()

# ====== Main ======
def main():
    training_data = load_train_data()
    test_data = load_test_data()

    predictions = []
    for point in test_data:
        label = classify_point(point, training_data)  # ändra till k=10 senare
        predictions.append(label)
        print(f"Sample {point} classified as {'Pikachu' if label == 1 else 'Pichu'}")

    plot_data(training_data, test_data, predictions)

if __name__ == "__main__":
    main()
