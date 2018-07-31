#!/usr/bin/env python3

@profile
def use_mem(x):
    mylist = [ ]
    for i in range(x):
        mylist.append(i)
    return mylist

for i in range(1000):
    if not i % 10:
        print(i)
        print(len(use_mem(i)))
