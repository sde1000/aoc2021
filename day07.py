#!/usr/bin/env python3

with open("day07-input.txt") as f:
    crabs = [ int(x) for x in f.read().split(',') ]

def linear(move):
    return move

def triangular(move):
    return move * (move + 1) // 2

def costs(pos, costfunc):
    return sum(costfunc(abs(c - pos)) for c in crabs)

print(f"Part 1: {min(costs(pos, linear) for pos in range(max(crabs)))}")
print(f"Part 1: {min(costs(pos, triangular) for pos in range(max(crabs)))}")
