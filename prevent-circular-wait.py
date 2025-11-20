import threading

m1 = threading.Lock()
m2 = threading.Lock()


def safe_task1():
    # Lock in the same order: first m1, then m2
    with m1:
        with m2:
            print("Safe Task 1 acquired both locks")


def safe_task2():
    # Lock in the same order: first m1, then m2
    with m1:
        with m2:
            print("Safe Task 2 acquired both locks")


t1 = threading.Thread(target=safe_task1)
t2 = threading.Thread(target=safe_task2)

t1.start()
t2.start()

t1.join()
t2.join()
