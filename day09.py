#!/usr/bin/env python3

with open("day09-input.txt") as f:
    heights = [ [ int(c) for c in s.strip() ] for s in f.readlines() ]

def adjacent_coords(y, x):
    if y > 0:
        yield (y - 1, x)
    if y < len(heights) - 1:
        yield (y + 1, x)
    if x > 0:
        yield (y, x - 1)
    if x < len(heights[0]) - 1:
        yield (y, x + 1)

def low_points():
    for y in range(len(heights)):
        for x in range(len(heights[0])):
            if heights[y][x] < min(
                    heights[y][x] for y, x in adjacent_coords(y, x)):
                yield (y, x)

def basin(y, x):
    b = set()
    new_points = set([(y, x)])
    while not new_points.issubset(b):
        b.update(new_points)
        new_points = set(
            (y, x) for p in new_points for y, x in adjacent_coords(*p)
            if heights[y][x] != 9)
    return b

print(f"Part 1: {sum(heights[y][x] + 1 for y, x in low_points())}")
basins = list(sorted(len(basin(y, x)) for y, x in low_points()))
print(f"Part 2: {basins[-1] * basins[-2] * basins[-3]}")
