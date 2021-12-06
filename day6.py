from typing import List
import numpy as np

input_file = "inputs/day_6.txt"

with open(input_file) as f:
    data_in = [int(i) for i in f.readlines()[0].split(",")]


def init_count(inital_fish: List[int]):
    counts = []
    for i in range(7):
        counts.append(inital_fish.count(i))
    return counts


def main(days: int):
    fish = init_count(data_in)
    incubator = [0, 0, 0]
    for idx in range(days):
        n_new_fish = fish[np.mod(idx, 7)]
        incubator.append(n_new_fish)
        fish[np.mod(idx - 1, 7)] = fish[np.mod(idx - 1, 7)] + incubator.pop(0)

    return sum(fish) + sum(incubator)


if __name__ == "__main__":
    n_fish = main(80)
    # part 1
    print(f"Number of fishes: {n_fish}")
    n_fish = main(256)
    # part 2
    print(f"Number of fishes: {n_fish}")
