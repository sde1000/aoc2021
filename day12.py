#!/usr/bin/env python3

connections = {}

with open("day12-input.txt") as f:
    for l in f:
        a, b = l.strip().split('-')
        connections.setdefault(a, []).append(b)
        connections.setdefault(b, []).append(a)

def small_twice(path):
    for p in path:
        if p.islower() and path.count(p) > 1:
            return True
    return False

def paths(path=('start',), allow_small_twice=False):
    if path[-1] == 'end':
        yield path
        return
    for p in connections[path[-1]]:
        if p == 'start':
            continue
        if p.islower() and p in path:
            if not allow_small_twice or small_twice(path):
                continue
        yield from paths(path + (p,), allow_small_twice)

print(f"Part 1: {sum(1 for _ in paths())}")
print(f"Part 2: {sum(1 for _ in paths(allow_small_twice=True))}")
