import matplotlib.pyplot as plt
import math

x = list(range(10))
k = int(input("Skriv in kurvans lutning: "))
m = int(input("Skriv in kurvans m-värde: "))
y = [k*(x**2)+m for x in x]

plt.plot(x, y)
plt.xlabel = "x"
plt.ylabel = "y"
plt.title = "Funktion av y=kx+m"

plt.show()
