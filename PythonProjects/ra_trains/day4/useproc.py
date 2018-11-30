#!/usr/bin/env python3

from multiprocessing import Process, Queue, Lock
import time
import random

q = Queue()
l = Lock()

def hello(i):
    with l:
        time.sleep(random.randint(0,3))
        print(f"Hello, with i = {i}")
        q.put(i)

procs = [ ]
for i in range(10):
    p = Process(target=hello, args=(i,))
    p.start()
    procs.append(p)

for one_proc in procs:
    if one_proc is not None:
        one_proc.join()
    else:
        print("None")
        

while not q.empty():
    print(q.get())
    
