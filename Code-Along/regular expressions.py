# import re

# text = "Det var en gång en katt som tog på sig en hatt."

# match_list = re.findall(r".att", text) # ?=att, *.att, osv


# print(match_list)

# #I terminal: "grep .att text"

# for x in match_list:
#     match x:
#         case "katt":
#             print("Cat")
#         case "hatt":
#             print("Hat")




# while True:
#     try:
#         age = input("Ange din ålder")
#         age = float(age)
#         if not 0 <= age <= 125:
#             raise ValueError("Åldern måste vara mellan 0 och 125")
#         print(f"Du är {age} år gammal")
#         break
#     except ValueError as err:
#         print(f"Error {err}")


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

f = np.sin(x)

plt.figure(dpi = 100)
plt.plot(x, f)

plt.show()

