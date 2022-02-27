import csv
import os

import numpy as np

x = [0, 0, 1, 1, 0, 1, 1, 0]

# Q1.a
x_interp = np.empty(2 * len(x))
x_interp[::2] = x
x_interp[1::2] = 0.5 * (x + np.roll(x, 1))

# Q1.b
X = np.fft.fft(x)
X_pad = np.hstack((X, np.zeros(8)))
X_pad[:4] *= 2
X_pad[12:16] = 2 * X_pad[4:8]
x_pad = np.fft.ifft(X_pad)

#Q1.c
H8 = 1 / np.sqrt(8) * np.vstack((
    np.ones(8),
    np.hstack((np.ones(4), -np.ones(4))),
    np.hstack((
        np.repeat(np.sqrt(2), 2),
        -np.repeat(np.sqrt(2), 2),
        np.zeros(4)
    )),
    np.hstack((
        np.zeros(4),
        np.repeat(np.sqrt(2), 2),
        -np.repeat(np.sqrt(2), 2)
    )),
    np.pad([2, -2], (0, 6)),
    np.pad([2, -2], (2, 4)),
    np.pad([2, -2], (4, 2)),
    np.pad([2, -2], (6, 0)),
))
H16 = 1 / 4 * np.vstack((
    np.ones(16),

    np.hstack((np.ones(8), -np.ones(8))),
    
    np.hstack((
        np.repeat(np.sqrt(2), 4),
        -np.repeat(np.sqrt(2), 4),
        np.zeros(8)
    )),
    np.hstack((
        np.zeros(8),
        np.repeat(np.sqrt(2), 4),
        -np.repeat(np.sqrt(2), 4)
    )),

    np.pad(np.array([2, 2, -2, 2]), (0, 12)),
    np.pad(np.array([2, 2, -2, 2]), (4, 8)),
    np.pad(np.array([2, 2, -2, 2]), (8, 4)),
    np.pad(np.array([2, 2, -2, 2]), (12, 0)),

    np.pad(np.sqrt(8) * np.array([1, -1]), (0, 14)),
    np.pad(np.sqrt(8) * np.array([1, -1]), (2, 12)),
    np.pad(np.sqrt(8) * np.array([1, -1]), (4, 10)),
    np.pad(np.sqrt(8) * np.array([1, -1]), (6, 8)),
    np.pad(np.sqrt(8) * np.array([1, -1]), (8, 6)),
    np.pad(np.sqrt(8) * np.array([1, -1]), (10, 4)),
    np.pad(np.sqrt(8) * np.array([1, -1]), (12, 2)),
    np.pad(np.sqrt(8) * np.array([1, -1]), (14, 0)),
))
X_haar = H8 @ x
X_haar_pad = np.hstack((np.sqrt(2) * X_haar, np.zeros(8)))
x_haar = H16.T @ X_haar_pad

with open(os.path.join(os.getcwd(), "hw06", "q1.csv"), 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["n", "a", "b_real", "b_imag", "c"])
    writer.writerows(zip(
        range(16),
        x_interp,
        x_pad.real,
        x_pad.imag,
        x_haar
    ))
