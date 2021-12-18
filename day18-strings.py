#!/usr/bin/env python3

from itertools import permutations

with open("day18-input.txt") as f:
    homework = [ tuple(int(sym) if sym.isdigit() else sym for sym in sl
                       if sym != ',') for sl in (l.strip() for l in f) ]

def explode(n):
    nesting = 0
    num_to_left = 0
    cn = enumerate(n)
    while True:
        try:
            idx, c = next(cn)
        except StopIteration:
            return
        if c == ']':
            nesting -= 1
        elif isinstance(c, int):
            num_to_left = idx
        elif c == '[':
            nesting += 1
            if nesting >= 5 and isinstance(n[idx + 1], int) \
               and isinstance(n[idx + 2], int):
                _, left = next(cn)
                _, right = next(cn)
                _, _ = next(cn)  # ]
                if num_to_left:
                    new = n[:num_to_left]
                    new += (n[num_to_left] + left,)
                    new += n[num_to_left + 1 : idx]
                else:
                    new = n[:idx]
                new += (0,)
                for idx, c in cn:
                    if isinstance(c, int):
                        new += (c + right,) + n[idx + 1:]
                        break
                    else:
                        new += (c,)
                return new

def split(n):
    for idx, c in enumerate(n):
        if isinstance(c, int) and c > 9:
            l = c // 2
            r = c - l
            return n[:idx] + ("[", l, r, "]") + n[idx + 1 :]

def reduce(n):
    while True:
        if new := explode(n):
            n = new
            continue
        elif new := split(n):
            n = new
            continue
        return n

def add(a, b):
    return reduce(("[",) + a + b + ("]",))

def magnitude(n):
    i = iter(n)
    def val():
        if (c := next(i)) == '[':
            l = val()
            r = val()
            assert next(i) == ']'
            return 3 * l + 2 * r
        else:
            return c
    return val()

def addlist(l):
    c = l[0]
    for i in l[1:]:
        c = add(c, i)
    return c

print(f"Part 1: {magnitude(addlist(homework))}")

maxmag = max(magnitude(add(a, b)) for a, b in permutations(homework, 2))
print(f"Part 2: {maxmag}")
