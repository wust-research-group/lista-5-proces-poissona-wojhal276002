import random

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

I = 0
t = 0
T = 10
lamb = 0.5
skoki = [0]
liczba_skokow = [0]
while True:
    U = np.random.uniform(0, 1)
    t = t - (1 / lamb) * np.log(U)
    if t > T:
        liczba_skokow.append(I)
        skoki.append(T)
        break
    else:
        I += 1
        liczba_skokow.append(I - 1)
        skoki.append(t)
        liczba_skokow.append(I)
        skoki.append(t)

# Druga metoda
I_1 = 0
skoki_1 = [0]
liczba_skokow_1 = [0]
n = np.random.poisson(lamb * T)
if n == 0:
    liczba_skokow_1.append(I_1)
    skoki_1.append(T)
else:
    skokson = sorted([np.random.uniform(0, T) for i in range(n)] * 2)
    for c in range(len(skokson)):
        if c % 2 == 0:
            liczba_skokow_1.append(I_1)
        else:
            I_1 += 1
            liczba_skokow_1.append(I_1)
        skoki_1.append(skokson[c])
    liczba_skokow_1.append(I_1)
    skoki_1.append(T)
print(skoki_1)
print(liczba_skokow_1)
plt.plot(skoki, liczba_skokow)
plt.plot(skoki_1, liczba_skokow_1)
plt.xlim(0, T + 1)
plt.show()
