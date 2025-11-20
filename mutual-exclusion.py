"""Here deadlock was caused as both threads requred mutual excusion while write to file"""

import threading
import time

file_lock = threading.Lock()
network_lock = threading.Lock()


def thread1():
    print("Thread 1 locking file...")
    file_lock.acquire()
    time.sleep(0.2)

    print("Thread 1 trying to lock network...")
    network_lock.acquire()
    print("Thread 1: acquired both locks")
    network_lock.release()
    file_lock.release()


def thread2():
    print("Thread 2 locking network...")
    network_lock.acquire()
    time.sleep(0.2)

    print("Thread 2 trying to lock file...")
    file_lock.acquire()

    print("Thread 2: acquired both locks")
    file_lock.release()
    network_lock.release()


t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)


t1.start()
t2.start()


t1.join()
t2.join()

print("Done")
