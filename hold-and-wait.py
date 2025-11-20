"""Causing deadlock cause thread1 dosent release accuried resources before taking new ones"""

import threading
import time

lockA = threading.Lock()
lockB = threading.Lock()


def thread1():
    with lockA:
        print("T1: locked A")
        time.sleep(0.1)
        print("T1: waiting for B")
        with lockB:
            print("T1: locked B")


def thread2():
    with lockB:
        print("T2: locked B")
        time.sleep(0.1)
        print("T2: waiting for A")
        with lockA:
            print("T2: locked A")


t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()

t1.join()
t2.join()
