#!/usr/bin/env python3

with open("day13-input.txt") as f:
    points, instructions = f.read().split("\n\n")
    points = frozenset(tuple(int(z) for z in l.split(","))
                       for l in points.splitlines())
    instructions = [ (i[11], int(i[13:])) for i in instructions.splitlines() ]

def fold(points, ins):
    if ins[0] == 'x':
        return frozenset(
            (x, y) if x < ins[1] else (2 * ins[1] - x, y) for x, y in points)
    else:
        return frozenset(
            (x, y) if y < ins[1] else (x, 2 * ins[1] - y) for x, y in points)

print(f"Part 1: {len(fold(points, instructions[0]))}")

for i in instructions:
    points = fold(points, i)

print("Part 2:")
for y in range(max(y for x, y in points) + 1):
    print(''.join('#' if (x, y) in points else ' '
                  for x in range(max(x for x, y in points) + 1)))
