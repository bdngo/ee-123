import csv

import numpy as np

freqs = np.linspace(-2 * np.pi, 2 * np.pi, 100)
mag = lambda w: np.abs(np.sin(3 * w) / (6 * np.sin(w / 2)))

with open("hw01/q6a-mag.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['n', "q6a-mag"])
    writer.writerows(zip(freqs, mag(freqs)))
