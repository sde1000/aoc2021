#!/usr/bin/env python3

from itertools import combinations

with open("day19-input.txt") as f:
    scanners = [ [ tuple(int(c) for c in l.split(','))
                   for l in scanner.splitlines() if not l.startswith('---') ]
                 for scanner in f.read().split("\n\n") ]

def rotations(s):
    yield s
    yield [(x, -z, y) for x, y, z in s]
    yield [(x, -y, -z) for x, y, z in s]
    yield [(x, z, -y) for x, y, z in s]

def orientations(s):
    yield from rotations(s) # Forwards
    yield from rotations([(y, -x, z) for x, y, z in s]) # Left
    yield from rotations([(-x, -y, z) for x, y, z in s]) # Back
    yield from rotations([(-y, x, z) for x, y, z in s]) # Right
    yield from rotations([(-z, y, x) for x, y, z in s]) # Up
    yield from rotations([(z, y, -x) for x, y, z in s]) # Down

beacons = set(scanners.pop(0))
scanpos = set([(0, 0, 0)])

def match(s):
    for base in beacons:
        for i in range(len(s)):
            tx, ty, tz = ( b - a for a, b in zip(s[i], base) )
            potential = set(
                ( (x + tx, y + ty, z + tz) for x, y, z in s) )
            if len(beacons & potential) >= 12:
                beacons.update(potential)
                return tx, ty, tz

while scanners:
    print(f"{len(scanners)} to go...")
    for i in range(len(scanners)):
        for o in orientations(scanners[i]):
            if m := match(o):
                scanpos.add(m)
                break
        if m:
            del scanners[i]
            break

print(f"Part 1: {len(beacons)}")
print(f"Part 2: {max(sum(abs(a - b) for a, b in zip(*n)) for n in combinations(scanpos, 2))}")
