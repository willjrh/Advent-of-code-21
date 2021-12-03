import numpy as np


def main(file: str):

    with open(file) as f:
        data_in = f.read().split()
        # convert data into a matrix
        data_matrix = []
        for line in data_in:
            data_matrix.append([int(digit) for digit in line])

    data = np.array(data_matrix)

    # part 1
    gamma, beta = calc_gamma_beta(data)
    print(bin2num(gamma) * bin2num(beta))

    # part 2
    # data = main(("inputs/day_3_test.txt"))
    o2 = filter_gasses(data, "most")
    co2 = filter_gasses(data, "least")

    print(f"o2 is {o2}, with number {bin2num(o2)}")
    print(f"co2 is {co2}, with number {bin2num(co2)}")
    print(f"Part 2 solution is {bin2num(o2) * bin2num(co2)}")


def calc_gamma_beta(mat: np.ndarray):
    gamma = []
    beta = []

    for i in range(np.shape(mat)[1]):
        gamma_elem = int(np.round(np.mean(mat[:, i])))
        gamma.append(gamma_elem)
        beta.append(abs(gamma_elem - 1))

    return gamma, beta


def bin2num(binary):
    # print([x * 2 ** ind for ind, x in enumerate(reversed(binary))])
    return np.sum([x * 2 ** ind for ind, x in enumerate(reversed(binary))])


def filter_gasses(data: np.ndarray, commonality: str) -> np.ndarray:

    for i in range(np.shape(data)[1]):
        if np.shape(data)[0] == 1:
            gas = data.flatten()
            break
        else:
            gas_idx = commonality_filter(commonality, data[:, i])
            data = np.take(data, gas_idx, 0)

        gas = data.flatten()

    return gas


def commonality_filter(
    commonality: str, bits: np.ndarray, eps: float = 1e-15
) -> np.ndarray:
    """
    Take the most or least common bits, and return the indicies to keep
    We add eps so that x.5 always rounds up, it's the behaviour we want.
    """

    if commonality == "most":
        most_common = np.round(np.mean(bits) + eps)
        return np.where(bits == most_common)[0]
    elif commonality == "least":
        most_common = np.round(np.mean(bits) + eps)
        return np.where(bits == abs(most_common - 1))[0]
    else:
        raise ValueError("`commonality` must be 'most' or 'least'.")


if __name__ == "__main__":
    main("inputs/day_3_1.txt")

