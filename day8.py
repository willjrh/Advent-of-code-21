import os
import re
import numpy as np


def load_data(input_file: str):

    with open(input_file) as f:
        data_in = f.read().splitlines()

    segment = []
    signal = []

    for d in data_in:
        data = re.split(r"(\s\|\s)", d)
        signal.append(data[0].split())
        segment.append(data[2].split())

    return signal, segment


def check_occurences(segment):
    num_dict = {2: "1", 3: "7", 4: "4", 5: "2,3,5", 6: "0,6,9", 7: "8"}
    return num_dict[segment]


def get_number(string_nums):
    integer_list = [str(integer) for integer in string_nums]
    four_digit_string = "".join(integer_list)
    return int(four_digit_string)


def decode_six_segs(segment: set, codes: dict):

    num = None
    if len(segment) == 6:
        if codes["4"] <= segment:
            num = "9"
        elif not codes["1"] <= segment and segment <= codes["8"]:
            num = "6"
        else:
            num = "0"

    if num is not None and num not in codes:
        codes[num] = segment

    return codes


def decode_unique(signal, codes):

    for sig in signal:
        if len(sig) == 2:
            num = "1"
        elif len(sig) == 3:
            num = "7"
        elif len(sig) == 4:
            num = "4"
        elif len(sig) == 7:
            num = "8"
        else:
            num = None

        if num is not None and num not in codes:
            codes[num] = set(sig)

    return codes


def decode_five_segs(segment: set, codes: dict):

    num = None

    if len(segment) == 5:
        if codes["1"] <= segment:
            num = "3"
        elif segment <= codes["9"]:
            num = "5"
        else:
            num = "2"

    if num is not None and num not in codes:
        codes[num] = segment

    return codes


def decode_display(display, code):
    num = []
    for dis in display:
        num.append([key for key, seg in code.items() if set(dis) == seg][0])

    return get_number(num)


def main(filename: str):
    signal, segment = load_data(filename)

    # part 1
    numbers = []
    for display in segment:
        for seg in display:
            numbers.append(check_occurences(len(seg)))
    counter = 0
    for num in ["1", "4", "7", "8"]:
        counter += numbers.count(num)
    print(counter)

    # part 2
    total = 0
    for idx, display in enumerate(segment):
        codes = {}
        codes = decode_unique(signal[idx], codes)
        for sig in signal[idx]:
            codes = decode_six_segs(set(sig), codes)
        for sig in signal[idx]:
            codes = decode_five_segs(set(sig), codes)
        # for seg in display:
        total += decode_display(display, codes)
    return


if __name__ == "__main__":
    input_file = os.path.join("inputs", "day8_in.txt")
    main(input_file)
