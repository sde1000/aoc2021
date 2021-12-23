#!/usr/bin/env python3

import re
from functools import reduce
from operator import mul
from collections import Counter

stepre = re.compile(
    r'^(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)$')

with open("day22-input.txt") as f:
    steps = [ ((m := stepre.match(l))[1] == "on",
               ((int(m[2]), int(m[3])),
                (int(m[4]), int(m[5])),
                (int(m[6]), int(m[7])))) for l in f ]

# size(A | B) = size(A) + size(B) - size(A & B)

def intersect(a, b):
    l = max(a[0], b[0])
    r = min(a[1], b[1])
    return (l, r) if l < r else None

class Cuboid(tuple):
    def large(self):
        return not all(n in range(-50, 52) for a in self for n in a)

    def intersection(self, other):
        c = Cuboid(intersect(a, b) for a, b in zip(self, other))
        return c if all(c) else None

    def cubes(self):
        return reduce(mul, (a[1] - a[0] + 1 for a in self))

def reboot(steps, skip_large=False):
    core = Counter()
    for ins, step in steps:
        cuboid = Cuboid(step)
        if skip_large and cuboid.large():
            continue
        new = []
        for c, cnt in list(core.items()):
            if cnt and (i := c.intersection(cuboid)) is not None:
                core[i] -= cnt
        if ins:
            core[cuboid] += 1
    return sum(cnt * c.cubes() for c, cnt in core.items())

print(f"Part 1: {reboot(steps, skip_large=True)}")
print(f"Part 2: {reboot(steps)}")
