"""Here threads dont need mutual exclusion to write to the file"""

import threading
import time


def thread1():
    print("Thread 1 writing to file...")
    with open("demo.txt", "a") as f:
        f.write("Thread 1 wrote something\n")
    time.sleep(0.2)

    print("Thread 1 doing network operation...")
    time.sleep(0.2)


def thread2():
    print("Thread 2 writing to file...")
    with open("demo.txt", "a") as f:
        f.write("Thread 2 wrote something\n")
    time.sleep(0.2)

    print("Thread 2 doing network operation...")
    time.sleep(0.2)


t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)


t1.start()
t2.start()


t1.join()
t2.join()

print("Done")
