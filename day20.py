#!/usr/bin/env python3

with open("day20-input.txt") as f:
    algo = [ c == '#' for c in f.readline().strip() ]
    f.readline()
    img = frozenset((y, x) for y, l in enumerate(f.readlines())
                    for x, c in enumerate(l.strip()) if c == '#')

bit = iter([ 0x100, 0x80, 0x40, 0x20, 0x10, 0x08, 0x04, 0x02, 0x01 ])
neighbours = [ (a, b, next(bit)) for a in range(-1, 2) for b in range(-1, 2) ]

def idx(img, y, x, inverted=False):
    return sum(bit for dy, dx, bit in neighbours
                   if ((y + dy, x + dx) in img) ^ inverted)

def step(img, inverted, yrange, xrange):
    yrange = range(yrange.start - 1, yrange.stop + 1)
    xrange = range(xrange.start - 1, xrange.stop + 1)
    return (frozenset((y, x) for y in yrange for x in xrange
                      if algo[idx(img, y, x, inverted)] ^ inverted ^ algo[0]),
            inverted ^ algo[0], yrange, xrange)

state = (img, False,
         range(min(y for y, x in img), max(y for y, x in img) + 1),
         range(min(x for y, x in img), max(x for y, x in img) + 1))
for _ in range(2):
    state = step(*state)
print(f"Part 1: {len(state[0])}")
for _ in range(2, 50):
    state = step(*state)
print(f"Part 2: {len(state[0])}")
