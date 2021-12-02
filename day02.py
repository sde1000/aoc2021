#!/usr/bin/env python3

from itertools import tee

with open('day02-input.txt') as f:
    commands = [(a, int(b)) for a, b in (x.split() for x in f)]

def execute(commands, with_aim=False):
    h, d, aim = 0, 0, 0
    for verb, amount in commands:
        if verb == "forward":
            h += amount
            d += with_aim * amount * aim
        else:
            aim += amount if verb == "down" else -amount
            if not with_aim:
                d += amount if verb == "down" else -amount
    return h * d

print(f"Part 1: {execute(commands)}")
print(f"Part 2: {execute(commands, with_aim=True)}")
