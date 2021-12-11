#!/usr/bin/env python3

with open("day11-input.txt") as f:
    octopi = [ [ int(x) for x in l.strip() ] for l in f ]

def adjacent(y, x):
    return ((ay, ax) for ay in (y - 1, y, y + 1) for ax in (x - 1, x, x + 1)
            if (ay, ax) != (y, x) and ay in range(10) and ax in range(10))

def step():
    flashes = []

    def inc(y, x):
        octopi[y][x] += 1
        if octopi[y][x] == 10:
            flashes.append((y, x))
            for (ay, ax) in adjacent(y, x):
                inc(ay, ax)
            
    for y in range(10):
        for x in range(10):
            inc(y, x)

    for y, x in flashes:
        octopi[y][x] = 0

    return len(flashes)

print(f"Part 1: {sum(step() for _ in range(100))}")

nsteps = 101
while step() != 100:
    nsteps += 1

print(f"Part 2: {nsteps}")
