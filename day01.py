#!/usr/bin/env python3

from itertools import tee

with open('day01-input.txt') as f:
    depths = [int(x) for x in f]

def sliding_window(data, winsize):
    ds = tee(data, winsize)
    for s in range(1, winsize):
        for i in ds[s:]:
            next(i)
    return zip(*ds)

def increases(depths):
    for a, b in sliding_window(depths, 2):
        yield b > a

def windows(depths):
    for x in sliding_window(depths, 3):
        yield sum(x)

print(f"Part 1: {sum(increases(depths))}")
print(f"Part 2: {sum(increases(windows(depths)))}")
