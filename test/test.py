from scipy.signal import find_peaks, peak_prominences
import numpy as np


def prominence(x):
    peaks, _ = find_peaks(x)
    prominences = peak_prominences(x, peaks)[0]

    res = []

    for p in prominences:
        res.append(int(p))
        print(int(p))

values = [int(_) for _ in input().split()]  # enter velues splitted by space
values.append(0)
values.insert(0, 0)

for i in range(0, len(values)):
    if (values[i] < 1):
        exit(1)

prominence(values)

#### input ####
# 47 43 47 42 48 48 42

#### output ####
# 5
# 5
# 48