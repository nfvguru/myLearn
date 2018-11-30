#!/usr/bin/env python3

import threading
import time
import random

class MyThread(threading.Thread):
    def __init__(self, i):
        super().__init__()
        self.i = i
    def run(self):
        time.sleep(random.randint(0,3))
        print(f"I'm in thread {self.i}!")

for i in range(10):
    t = MyThread(i)
    t.start()

for one_thread in threading.enumerate():
    if threading.current_thread() == one_thread:
        continue
    one_thread.join(1)

print("Goodbye!")
