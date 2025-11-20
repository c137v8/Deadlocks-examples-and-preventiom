import threading
import time

m1 = threading.Lock()
m2 = threading.Lock()


def task1():
    print("Task1 locking m1...")
    m1.acquire()
    time.sleep(0.1)

    print("Task1 trying to lock m2...")
    m2.acquire()
    print("Task1 acquired both locks")

    m2.release()
    m1.release()


def task2():
    print("Task2 locking m2...")
    m2.acquire()
    time.sleep(0.1)

    print("Task2 trying to lock m1...")
    m1.acquire()
    print("Task2 acquired both locks")

    m1.release()
    m2.release()


t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()
