#!/usr/bin/env python3

import __main__

x = 100

def foo():
    __main__.x = 200
    print(f"In foo, x = {__main__.x}")

print(f"Before, x = {x}")
foo()
print(f"After, x = {x}")


# L  local
# E  enclosing function

# G  global
# B  builtins
