from random import randint
from typing import List


class Mastermind:
    def __init__(self, color_types=5, row_size=4):
        self.color_types = color_types
        self.row_size = row_size

    def generate_random_combination(self):
        return [randint(1, self.color_types) for _ in range(self.row_size)]

    def check_combination(self, combination: List[int], 
                          winning_combination: List[int]):
        """In result combination, 1 is match, 0 is not matched but present
        in winning combination, -1 is not present in winning combination"""
    
        assert len(combination) == len(winning_combination)

        result = []
        for c, wc in zip(combination, winning_combination):
            if c == wc:
                result.append(1)
            elif c in winning_combination:
                result.append(0)
            else:
                result.append(-1)

        return result

    def random_start(self):
        winning_combination = self.generate_random_combination()
        self.start(winning_combination)

    def start(self, winning_combination: List[int]):
        assert len(winning_combination) == self.row_size

        current_combination = [-1 for _ in range(self.row_size)]
        guesses = 0

        print('New Game')
        print(f'Colors: {self.color_types}, Row size: {self.row_size}')

        while True:
            guesses += 1
            print('\033[92m', end='')
            inp = input()
            print('\033[0m', end='')

            current_combination = [int(i) for i in inp.split(' ')]
            check_result = self.check_combination(current_combination, 
                                                  winning_combination)

            print('\033[94m', end='')
            [print(x, end=' ') for x in check_result]
            print('\033[0m')

            if current_combination == winning_combination:
                break

        print(f'You won in {guesses} guesses!')


game = Mastermind()
game.random_start()

