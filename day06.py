#!/usr/bin/env python3

with open("day06-input.txt") as f:
    fish = [ 0 ] * 9
    for f in (int(x) for x in f.read().split(',')):
        fish[f] += 1

def gen():
    fish.append(r := fish.pop(0))
    fish[6] += r

for _ in range(80):
    gen()

print(f"Part 1: {sum(fish)}")

for _ in range(80, 256):
    gen()

print(f"Part 2: {sum(fish)}")
