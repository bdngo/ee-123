import csv

import numpy as np

freqs = np.linspace(-2 * np.pi, 2 * np.pi, 100)
resp = np.sin(3 * freqs) / (6 * np.sin(freqs / 2)) * np.exp(freqs * -5j / 2)

mag = np.abs(resp)
ang = np.angle(resp)

with open("hw01/q6a-mag.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['n', "q6a-mag"])
    writer.writerows(zip(freqs, mag))

with open("hw01/q6a-ang.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['n', "q6a-ang"])
    writer.writerows(zip(freqs, ang))

inputs = np.arange(0, 11)

maf_impulse = 1 / 6 * np.logical_and(np.greater_equal(inputs, 0), np.less_equal(inputs, 5))
x = np.cos(np.pi / 3 * inputs) * np.greater_equal(inputs, 0)

with open("hw01/q6b.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['n', "q6b"])
    writer.writerows(zip(inputs, np.convolve(maf_impulse, x)))
