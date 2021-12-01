import os
import numpy as np


def day_1(file: str):
    """Read in day 1 part 1 input and count increasing values"""
    with open(file) as f:
        data_in = f.read()
    # convert data to float
    data = [float(i) for i in data_in.split()]

    # Part 1
    print(sum(np.diff(np.array(data)) > 0))

    # Part 2
    convolution = []
    for i in range(len(data) - 2):
        convolution.append(data[i] + data[i + 1] + data[i + 2])

    print(sum(np.diff(convolution) > 0))

    pass


def main():
    day_1("inputs/day_1_1.txt")


if __name__ == "__main__":
    main()
