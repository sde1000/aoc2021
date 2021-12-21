#!/usr/bin/env python3

from collections import namedtuple, defaultdict, Counter

with open("day21-input.txt") as f:
    starts = tuple(int(l[28:]) for l in f.readlines())

def advance(pos, move):
    return (pos + move - 1) % 10 + 1

def ddie():
    while True:
        yield from range(1, 101)

scores = [0, 0]
pos = list(starts)
player = 0
roll = ddie()
rollcount = 0

while max(scores) < 1000:
    move = sum(next(roll) for _ in range(3))
    rollcount += 3
    pos[player] = advance(pos[player], move)
    scores[player] += pos[player]
    player = not player

print(f"Part 1: {min(scores) * rollcount}")

State = namedtuple(
    'State', ['p0_pos', 'p1_pos', 'p0_score', 'p1_score', 'next_player'])
initial = State(starts[0], starts[1], 0, 0, False)
universes = defaultdict(int)
universes[initial] = 1
wins = [0, 0]
rolls = Counter(
    a + b + c + 3 for a in range(3) for b in range(3) for c in range(3))

while universes:
    count = universes.pop(state := next(iter(universes)))  # FIFO
    player = state.next_player
    pa = 'p1_pos' if player else 'p0_pos'
    sa = 'p1_score' if player else 'p0_score'
    pos, score = getattr(state, pa), getattr(state, sa)
    for move, ways in rolls.items():
        new_pos = advance(pos, move)
        new_score = score + new_pos
        new_universes = count * ways
        if new_score >= 21:
            wins[player] += new_universes
        else:
            new_state = state._replace(**{pa: new_pos, sa: new_score,
                                          "next_player": not player})
            universes[new_state] += new_universes

print(f"Part 2: {max(wins)}")
