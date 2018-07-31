#!/usr/bin/env python3

from typing import Sequence

def hello(name:str) -> str:
    return f"Hello, {name}"

def first(item:Sequence[int]) -> str:
    return item[0]

print(hello('abcd'))
# print(hello(5))
# print(123 + hello('efgh'))

print(first([10, 20,30]))
