#!/usr/bin/env python3

with open("day10-input.txt") as f:
    lines = [ l.strip() for l in f ]

pairs = {
    '(': (')', 3, 1),
    '[': (']', 57, 2),
    '{': ('}', 1197, 3),
    '<': ('>', 25137, 4),
}

def check(line):
    stack = []
    for c in line:
        if c in pairs:
            stack.append(c)
        else:
            x = stack.pop()
            if c != pairs[x][0]:
                return pairs[x][1]
    return 0

def complete(line):
    stack = []
    for c in line:
        if c in pairs:
            stack.append(c)
        else:
            stack.pop()
    score = 0
    while stack:
        x = stack.pop()
        score = score * 5 + pairs[x][2]
    return score

print(f"Part 1: {sum(check(l) for l in lines)}")
scores = list(sorted(complete(l) for l in lines if not check(l)))
print(f"Part 2: {scores[len(scores) // 2]}")
