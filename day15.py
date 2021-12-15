#!/usr/bin/env python3

import heapq

with open("day15-input.txt") as f:
    risks = [ [ int(c) for c in s.strip() ] for s in f.readlines() ]

risks = { (y, x): risks[y][x]
          for y in range(len(risks)) for x in range (len(risks[0])) }

def neighbours(c):
    y, x = c
    yield (y - 1, x)
    yield (y + 1, x)
    yield (y, x - 1)
    yield (y, x + 1)

def safest(risks):
    target = max(risks.keys(), key=lambda p: p[0] * p[1])

    costs = { target: 0 }
    q = [ (0, target) ]

    while q:
        val, current = heapq.heappop(q)
        new_cost = risks[current] + costs[current]
        for n in (x for x in neighbours(current) if x in risks):
            if new_cost < costs.get(n, 1000000):
                costs[n] = new_cost
                heapq.heappush(q, (new_cost, n))

    return costs[(0, 0)]

def expand(risks):
    n = {}
    size = (max(x[0] for x in risks.keys()) + 1,
            max(x[1] for x in risks.keys()) + 1)
    for tile in ((y, x) for y in range(5) for x in range(5)):
        n.update(
            ((size[0] * tile[0] + loc[0], size[1] * tile[1] + loc[1]),
             (risk + tile[0] + tile[1] - 1 ) % 9 + 1)
            for loc, risk in risks.items())
    return n

print(f"Part 1: {safest(risks)}")
print(f"Part 2: {safest(expand(risks))}")
