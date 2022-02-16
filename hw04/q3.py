import csv
import os

import numpy as np

P = 500
idx = np.arange(10, 21)
L = np.power(2, idx)
func = L * (idx + 1) / (L - P + 1)

with open(os.path.join(os.getcwd(), "hw04", "q3.csv"), 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["v", "cost"])
    writer.writerows(zip(idx, func))
