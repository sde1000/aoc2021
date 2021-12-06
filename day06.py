#!/usr/bin/env python3

with open("day06-input.txt") as f:
    fish = { n: 0 for n in range(9) }
    for f in (int(x) for x in f.read().split(',')):
        fish[f] += 1

def gen():
    global fish
    fish = {
        8: fish[0],
        7: fish[8],
        6: fish[7] + fish[0],
        5: fish[6],
        4: fish[5],
        3: fish[4],
        2: fish[3],
        1: fish[2],
        0: fish[1],
    }

for _ in range(80):
    gen()

print(f"Part 1: {sum(fish.values())}")

for _ in range(80, 256):
    gen()

print(f"Part 2: {sum(fish.values())}")
