#!/usr/bin/env python3

with open("day16-input.txt") as f:
    i = f.read().strip()

class transmission:
    def __init__(self, t):
        if isinstance(t, str):
            self.data = int(t, 16)
            self.available = len(t) * 4
        else:
            self.data = t[0]
            self.available = t[1]

    def get(self, bits):
        self.available -= bits
        return self.data >> self.available & (1 << bits) - 1

    def sub(self, bits):
        self.available -= bits
        return transmission((self.data >> self.available, bits))

class packet:
    def __init__(self, bits):
        self.ver = bits.get(3)
        self.tid = bits.get(3)
        self.subs = []
        if self.tid == 4:
            self.value = 0
            while True:
                self.value = self.value << 4 | (v := bits.get(5)) & 0xf
                if not v & 0x10:
                    break
        else:
            ltype = bits.get(1)
            if ltype == 0:
                sub_bits = bits.sub(bits.get(15))
                while sub_bits.available:
                    self.subs.append(packet(sub_bits))
            else:
                self.subs = [ packet(bits) for _ in range(bits.get(11)) ]
            if self.tid == 0:
                self.value = sum(x.value for x in self.subs)
            elif self.tid == 1:
                self.value = 1
                for x in self.subs:
                    self.value = self.value * x.value
            elif self.tid == 2:
                self.value = min(x.value for x in self.subs)
            elif self.tid == 3:
                self.value = max(x.value for x in self.subs)
            elif self.tid == 5:
                self.value = self.subs[0].value > self.subs[1].value
            elif self.tid == 6:
                self.value = self.subs[0].value < self.subs[1].value
            elif self.tid == 7:
                self.value = self.subs[0].value == self.subs[1].value
        self.vsum = self.ver + sum(x.vsum for x in self.subs)

d = packet(transmission(i))

print(f"Part 1: {d.vsum}")
print(f"Part 2: {d.value}")
