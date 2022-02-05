import numpy as np
import matplotlib.pyplot as plt
import csv
import os

Q8_AB_PATH = os.path.join(os.getcwd(), "hw02", "q8.csv")
Q8_C_PATH = os.path.join(os.getcwd(), "hw02", "q8c.csv")

indices = np.linspace(-2.5, 2.5, num=11)

X   = np.array([0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0])
X_a = 0.5 * (np.pad(X[2:], (0, 2)) + np.pad(X[:-2], (2, 0)))
X_b = 0.5 * (np.pad(X[1:], (0, 1)) + np.pad(X[:-1], (1, 0)))
X_d = 0.5 * (np.pad(X[2:], (0, 2)) - np.pad(X[:-2], (2, 0)))

indices_dbl = np.linspace(-2.5, 2.5, num=21)
X_dbl = np.array([
    0, 0.5, 1, 0.5, 0,
    0,
    0,
    0,
    0, 0.5, 1, 0.5, 0,
    0,
    0,
    0,
    0, 0.5, 1, 0.5, 0
])
X_c = 0.5 * (
    np.pad(X_dbl[1:], (0, 1))
    + np.pad(X_dbl[:-1], (1, 0))
    + np.pad(X_dbl[3:], (0, 3))
    + np.pad(X_dbl[:-3], (3, 0))
)

with open(Q8_AB_PATH, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["index", "8a", "8b", "8d"])
    writer.writerows(zip(indices, X_a, X_b, X_d))

with open(Q8_C_PATH, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["index", "8c"])
    writer.writerows(zip(indices_dbl, X_c))
