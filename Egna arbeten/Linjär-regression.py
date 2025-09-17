import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data: kvadratmeter och pris (i tusentals kronor)
kvadratmeter = np.array([30, 50, 70, 90, 110]).reshape(-1, 1)
pris = np.array([1000, 1500, 2000, 2500, 3000])  # tusentals kronor

# Skapa och träna modellen
modell = LinearRegression()
modell.fit(kvadratmeter, pris)

# Gör en förutsägelse
ny_bostad = np.array([[80]])  # 80 kvm
förutspått_pris = modell.predict(ny_bostad)
print(f"Förutspått pris för 80 kvm: {förutspått_pris[0]:.0f} tusen kr")

# Visualisera
plt.scatter(kvadratmeter, pris, color='blue', label='Data')
plt.plot(kvadratmeter, modell.predict(kvadratmeter), color='red', label='Linjär regression')
plt.xlabel('Kvadratmeter')
plt.ylabel('Pris (tusen kr)')
plt.title('Huspris vs Boyta')
plt.legend()
plt.show()