import numpy as np


def main(file: str) -> np.ndarray:

    with open(file) as f:
        data_in = f.read().split()
        # convert data into a matrix
        data_matrix = []
        for line in data_in:
            data_matrix.append([int(digit) for digit in line])

    return np.array(data_matrix)


def calc_gamma_beta(mat: np.ndarray) -> np.ndarray:
    gamma = []
    beta = []

    for i in range(np.shape(mat)[1]):
        gamma_elem = int(np.round(np.mean(mat[:, i])))
        gamma.append(gamma_elem)
        beta.append(abs(gamma_elem - 1))

    return gamma, beta


def bin2num(binary):
    print([x * 2 ** ind for ind, x in enumerate(reversed(binary))])
    return np.sum([x * 2 ** ind for ind, x in enumerate(reversed(binary))])


if __name__ == "__main__":
    data = main(("inputs/day_3_1.txt"))
    gamma, beta = calc_gamma_beta(data)
    print(bin2num(gamma) * bin2num(beta))

