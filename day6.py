import os
import numpy as np

input_file = os.path.join("inputs", "day_6.txt")

with open(input_file) as f:
    data_in = [int(i) for i in f.readlines()[0].split(",")]


def init_count(inital_fish):
    counts = []
    for i in range(7):
        counts.append(inital_fish.count(i))
    return counts


def main():
    fish = init_count(data_in)
    incubator = [0, 0, 0]
    for idx in range(256):
        n_new_fish = fish[np.mod(idx, 7)]
        incubator.append(n_new_fish)
        fish[np.mod(idx - 1, 7)] = fish[np.mod(idx - 1, 7)] + incubator.pop(0)

    print(f"Number of fishes: {sum(fish) + sum(incubator)}")


if __name__ == "__main__":
    main()
