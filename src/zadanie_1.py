import random

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

te = [0]
iy = [0]
I = 0
T = 10
T_i = 0
lamb = 0.5
while T_i <= T:
    t = np.random.exponential(1 / lamb)
    T_i += t
    iy.append(I)
    I += 1
    if T_i > T:
        te.append(T)
    else:
        te.append(T_i)
        iy.append(I)
        te.append(T_i)
plt.plot(te, iy)
plt.show()

N_t = np.zeros(100)
i = 0
for x in range(100):
    I = 0
    T = 10
    T_i = 0
    lamb = 0.5
    while T_i <= T:
        t = np.random.exponential(1 / lamb)
        T_i += t
        I += 1
    N_t[i] = I
    i += 1
expected_lambda_t = lamb * T
plt.hist(N_t, bins=int(max(N_t)), density=True, label="Empiryczny")
xs = np.arange(0, int(max(N_t)) + 1)
poiss = poisson.pmf(xs, mu=expected_lambda_t)
plt.plot(xs, poiss, "ro-", label="Teoretyczny (Poisson)")
plt.show()
