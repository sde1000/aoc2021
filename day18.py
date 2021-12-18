#!/usr/bin/env python3

import json
from itertools import permutations

with open("day18-input.txt") as f:
    homework = [ json.loads(l) for l in f ]

def tree_to_depths(n, depth=0):
    for i in range(2):
        if isinstance(n[i], int):
            yield [depth, n[i]]
        else:
            yield from tree_to_depths(n[i], depth + 1)

def depths_to_tree(dl, depth=0):
    r = []
    for i in range(2):
        if dl[0][0] == depth:
            r.append(dl[0][1])
            dl.pop(0)
        else:
            r.append(depths_to_tree(dl, depth + 1))
    return r

def explode(dl):
    for i in range(len(dl) - 1):
        if dl[i][0] >= 4 and dl[i + 1][0] == dl[i][0]:
            if i:
                dl[i - 1][1] += dl[i][1]
            if i + 2 < len(dl):
                dl[i + 2][1] += dl[i + 1][1]
            dl[i][0] -= 1
            dl[i][1] = 0
            del dl[i + 1]
            return dl

def split(dl):
    for i in range(len(dl)):
        if dl[i][1] > 9:
            l = dl[i][1] // 2
            r = dl[i][1] - l
            dl[i][0] += 1
            dl[i][1] = l
            dl.insert(i + 1, [dl[i][0], r])
            return dl

def reduce(n):
    dl = list(tree_to_depths(n))
    while True:
        if new := explode(dl):
            dl = new
            continue
        else:
            if new := split(dl):
                dl = new
                continue
        return depths_to_tree(dl)

def add(a, b):
    return reduce([ a, b ])

def magnitude(n):
    if isinstance(n, int):
        return n
    return magnitude(n[0]) * 3 + magnitude(n[1]) * 2

def addlist(l):
    c = l[0]
    for i in l[1:]:
        c = add(c, i)
    return c

print(f"Part 1: {magnitude(addlist(homework))}")

maxmag = max(magnitude(add(a, b)) for a, b in permutations(homework, 2))
print(f"Part 2: {maxmag}")
