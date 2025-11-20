import threading
import time

lockA = threading.Lock()
lockB = threading.Lock()


def safe_thread(name):
    while True:
        gotA = lockA.acquire(blocking=False)
        if gotA:
            print(f"{name}: acquired A")
        else:
            continue

        gotB = lockB.acquire(timeout=0.1)
        if gotB:
            print(f"{name}: acquired B")
            # This is critical section
            print(f"{name}: doing work safely")
            time.sleep(0.2)

            lockB.release()
            lockA.release()
            break

        # Preempt the wait
        print(f"{name}: could not acquire B, releasing A and retrying")

        lockA.release()
        time.sleep(0.05)


t1 = threading.Thread(target=safe_thread, args=("T1",))
t2 = threading.Thread(target=safe_thread, args=("T2",))

t1.start()
t2.start()

t1.join()
t2.join()
