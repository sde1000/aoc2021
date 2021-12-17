#!/usr/bin/env python3

with open("day17-input.txt") as f:
    xrange, yrange = (tuple(sorted(int(n) for n in r.split("..")))
                      for r in f.readline().strip()[15:].split(", y="))

def probe(xvel, yvel):
    x, y = 0, 0
    while True:
        x += xvel
        y += yvel
        xvel = max(xvel - 1, 0)
        yvel -= 1
        yield x, y

def hits(xvel, yvel):
    t = probe(xvel, yvel)
    maxy = 0
    while True:
        x, y = next(t)
        maxy = max(y, maxy)
        if x >= xrange[0] and x <= xrange[1] \
           and y >= yrange[0] and y <= yrange[1]:
            return maxy
        if x > xrange[1]:
            return
        if y < yrange[0]:
            return

maxy = max(y for y in (hits(xvel, yvel)
                       for xvel in range(xrange[1] + 1)
                       for yvel in range(200))
           if y is not None)
print(f"Part 1: {maxy}")

sols = set((xvel, yvel) for xvel in range(xrange[1] + 1)
           for yvel in range(yrange[0], 200)
           if hits(xvel, yvel) is not None)
print(f"Part 2: {len(sols)}")
