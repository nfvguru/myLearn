#!/usr/bin/env python3

class Circle():
    def __init__(self, data, maxtimes):
        self.data = data
        self.maxtimes = maxtimes
        self.index = 0
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= self.maxtimes:
            self.count = 0
            raise StopIteration
        value = self.data[self.index % len(self.data)]
        self.index += 1
        self.count += 1
        return value

c = Circle('abcd', 7)

print(f"A: {'-'*60}")
for item in c:
    print(item)

print(f"B: {'-'*60}")
for item in c:
    print(item)
