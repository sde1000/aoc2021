#!/usr/bin/env python3

from collections import Counter

with open("day14-input.txt") as f:
    template = f.readline().strip()
    f.readline()
    rules = { tuple(a): b for a, b in (l.strip().split(" -> ") for l in f) }

def run(count):
    p = Counter(zip(template, template[1:]))
    for _ in range(count):
        p, prev_p = Counter(), p
        for pair, count in prev_p.items():
            p[(pair[0], rules[pair])] += count
            p[(rules[pair], pair[1])] += count
    c = Counter()
    for pair, count in p.items():
        c[pair[0]] += count
    c[template[-1]] += 1
    return max(c.values()) - min(c.values())

print(f"Part 1: {run(10)}")
print(f"Part 2: {run(40)}")
