#!/usr/bin/python

import threading
from time import sleep

e = threading.Event()

e.set()

event = e.wait()
print(event)

e.clear()

event = e.wait(2)
print("timeout:",event)


