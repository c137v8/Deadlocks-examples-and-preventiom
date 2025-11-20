"""Realse resources before waiting for new ones"""

import threading
import time

lockA = threading.Lock()
lockB = threading.Lock()


def safe_thread(name):
    while True:
        gotA = lockA.acquire(blocking=False)
        if not gotA:
            continue

        gotB = lockB.acquire(blocking=False)
        if not gotB:
            lockA.release()
            continue

        print(f"{name} acquired A and B safely")
        time.sleep(0.2)

        lockB.release()
        lockA.release()
        break


t1 = threading.Thread(target=safe_thread, args=("T1",))
t2 = threading.Thread(target=safe_thread, args=("T2",))

t1.start()
t2.start()

t1.join()
t2.join()
