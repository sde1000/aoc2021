#!/usr/bin/env python3

with open("day04-input.txt") as f:
    sections = f.read().split("\n\n")

numbers = [ int(x) for x in sections[0].split(",") ]

wins = iter(range(25))
wins = [ tuple(next(wins) for _ in range(5)) for _ in range(5) ]
wins = wins + list(zip(*wins))

class Board:
    def __init__(self, n):
        self.numbers = [ int(x) for x in n.split() ]
        self.marks = [ False for x in self.numbers ]
        self.won = False

    def mark(self, n):
        if self.won:
            return
        try:
            self.marks[self.numbers.index(n)] = True
        except ValueError:
            pass
        for cond in wins:
            if False in (self.marks[loc] for loc in cond):
                continue
            self.won = True
            return sum(n for n, mark in zip(self.numbers, self.marks)
                       if not mark) * n

boards = [ Board(n) for n in sections[1:] ]

wins = list(score for num in numbers for b in boards
            if (score := b.mark(num)) is not None)

print(f"Part 1: {wins[0]}")
print(f"Part 2: {wins[-1]}")
