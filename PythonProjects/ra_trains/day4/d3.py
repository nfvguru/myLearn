#!/usr/bin/env python3

d = {'a':1, 'b':2, 'c':3}

class D3Iterator():
    def __init__(self, d):
        self.d = d
        self.keys = iter(d.keys())

    def __next__(self):
        key = next(self.keys)
        return (key, self.d[key], key * self.d[key])

class D3():
    def __init__(self, d):
        self.d = d

    def __iter__(self):
        return D3Iterator(self.d)

for key, value, kv in D3(d):
    print(f"{key}:{value}, {kv}")  # kv = key * value
