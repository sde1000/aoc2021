#!/usr/bin/env python3

with open("day03-input.txt") as f:
    report = [ x.strip() for x in f ]

# Rotate/flip so all 'first bits' are first item in list, etc.
bits = list(''.join(l) for l in zip(*report))

gamma = int(''.join(
    '1' if x.count('1') > x.count('0') else '0' for x in bits), base=2)
epsilon = int(''.join(
    '1' if x.count('0') > x.count('1') else '0' for x in bits), base=2)

print(f"Part 1: {gamma * epsilon}")

def bitfilter(candidates, filter_by_most):
    bit = 0
    while len(candidates) > 1:
        bits = list(''.join(l) for l in zip(*candidates))[bit]
        if filter_by_most:
            common = '1' if bits.count('1') >= bits.count('0') else '0'
        else:
            common = '0' if bits.count('0') <= bits.count('1') else '1'
        candidates = [ x for x, s in zip(
            candidates, (b == common for b in bits)) if s ]
        bit += 1
    return int(candidates[0], base=2)

print(f"Part 2: {bitfilter(report, True) * bitfilter(report, False)}")
