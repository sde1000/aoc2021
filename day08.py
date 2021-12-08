#!/usr/bin/env python3

with open("day08-input.txt") as f:
    notes = [ (patterns.split(), output.split()) for patterns, output in
              (l.split(' | ') for l in f.readlines()) ]

print(f"Part 1: {sum(len(o) in (2, 3, 4, 7) for n in notes for o in n[1])}")

def decode(note):
    patterns = [ frozenset(p) for p in note[0] ]
    output = [ frozenset(o) for o in note[1] ]
    digits = [ None ] * 10
    digits[1] = next(p for p in patterns if len(p) == 2)
    digits[7] = next(p for p in patterns if len(p) == 3)
    digits[4] = next(p for p in patterns if len(p) == 4)
    digits[8] = next(p for p in patterns if len(p) == 7)
    digits[6] = next(p for p in patterns if len(p) == 6 and not (p > digits[1]))
    digits[9] = next(p for p in patterns if len(p) == 6 and p > digits[4])
    digits[0] = next(p for p in patterns if len(p) == 6 and p not in digits)
    digits[3] = next(p for p in patterns if len(p) == 5 and p > digits[1])
    digits[5] = next(p for p in patterns if len(p) == 5 and p < digits[6])
    digits[2] = next(p for p in patterns if p not in digits)
    
    numbers = { d: str(x) for x, d in enumerate(digits) }
    return int(''.join(numbers[d] for d in output))

print(f"Part 2: {sum(decode(note) for note in notes)}")
