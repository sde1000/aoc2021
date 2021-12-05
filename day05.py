#!/usr/bin/env python3

from collections import Counter

with open("day05-input.txt") as f:
    vents = [ tuple(tuple(int(x) for x in e.split(','))
                    for e in l.split(' -> '))
              for l in f.readlines() ]

def lrange(start, end):
    n = start
    while True:
        yield n
        if n == end:
            return
        n += 1 if start < end else -1

def line(start, end, include_diagonals=False):
    xs = lrange(start[0], end[0])
    ys = lrange(start[1], end[1])
    if start[0] == end[0]:
        yield from ((start[0], y) for y in ys)
    elif start[1] == end[1]:
        yield from ((x, start[1]) for x in xs)
    elif include_diagonals:
        yield from zip(xs, ys)

def danger(include_diagonals=False):
    c = Counter()
    for vent in vents:
        for point in line(*vent, include_diagonals=include_diagonals):
            c[point] += 1
    return sum(val >= 2 for val in c.values())

print(f"Part 1: {danger()}")
print(f"Part 2: {danger(include_diagonals=True)}")
