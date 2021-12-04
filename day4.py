from typing import List
import numpy as np


class BingoCard:
    def __init__(self, numbers_called: List[int], card: List[List[int]]):
        self.numbers_called = numbers_called
        self.card = card
        self.number_of_rows = len(card[0])
        self.number_of_cols = len(card)
        # find the matched numbers
        self.matched_cols: List[int] = []
        self.matched_rows: List[int] = []
        self.matched_coords: List[List[int, int]] = []
        self.card_status: str = "loser"
        self.unmatched_values: np.ndarray = np.asarray(
            self.card, dtype=np.int32
        ).flatten()

    def find_matched_numbers(self, called_number: str):
        for idx, card_num in enumerate(self.card):
            if called_number in card_num:
                self.matched_rows.append(idx)
                self.matched_cols.append(card_num.index(called_number))
                self.matched_coords.append([idx, card_num.index(called_number)])
                # we remove the matched value from `unmatched_values`
                self.compute_unmatched(called_number)

    def check_if_won(self):
        col = []
        for row in self.matched_rows:
            col = []
            for coord in self.matched_coords:
                if coord[0] == row:
                    col.append(coord[1])
        if len(np.unique(col)) == self.number_of_cols:
            self.card_status = "winner"

        # only check this if loser
        row = []
        if self.card_status == "loser":
            for col in self.matched_cols:
                row = []
                for coord in self.matched_coords:
                    if coord[1] == col:
                        row.append(coord[0])

            if len(np.unique(row)) == self.number_of_rows:
                self.card_status = "winner"

    def compute_unmatched(self, last_number: str):
        self.unmatched_values = self.unmatched_values[
            self.unmatched_values != int(last_number)
        ]


def read_bingo_cards(file: str) -> List[BingoCard]:
    with open(file) as f:
        data_in = f.read().splitlines()

    numbers_called = data_in[0].split(",")

    # init bingo card list
    bingo_cards: List[BingoCard] = []

    card: List[List[int]] = []
    # loop over input and get cards
    for line in data_in[2:]:
        if not line.split():
            bingo_cards.append(BingoCard(numbers_called, card))
            card: List[List[int]] = []
        else:
            card.append(line.split())

    return bingo_cards, numbers_called


def main(file: str):
    bingo_cards, numbers_called = read_bingo_cards(file)

    winners = []
    winning_vals = []
    idx_hold = []
    for called_number in numbers_called:
        for idx, card in enumerate(bingo_cards):
            card.find_matched_numbers(called_number)
            card.check_if_won()
            if card.card_status == "winner":
                winners.append(card)
                if idx not in idx_hold:
                    winning_vals.append(
                        np.sum(card.unmatched_values) * int(called_number)
                    )
                    print(
                        f"winning val: {np.sum(card.unmatched_values) * int(called_number)}, card {idx}"
                    )

                idx_hold.append(idx)


if __name__ == "__main__":
    main("inputs/day_4.txt")
