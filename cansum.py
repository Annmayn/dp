from typing import List
import time
import signal


def can_sum(val: int, arr: List) -> bool:
    if val == 0:
        return True
    if val < 0:
        return False

    for each in arr:
        new_val = val - each
        if can_sum(val-each, arr):
            return True
    return False


def can_sum_memoized(val: int, arr: List, memo: dict = None) -> bool:
    if memo is None:
        memo = {}
    if val in memo:
        return memo[val]
    if val == 0:
        return True
    if val < 0:
        return False

    for each in arr:
        new_val = val - each
        if can_sum_memoized(val-each, arr, memo):
            memo[new_val] = True
            return True
    memo[val] = False
    return False


if __name__ == "__main__":
    val = 300
    arr = [14, 7]

    def event_handler(signum, stack_frame):
        raise Exception("Execution took too long (>10 seconds). Skipping!!!")
        
    signal.signal(signal.SIGALRM, event_handler)
    signal.alarm(10)
    print("Running base version...")
    try:
        t1 = time.time()
        print(can_sum(val, arr), "in {t:.2f} secs".format(t=time.time()-t1))
    except Exception as e:
        print(e)
    finally:
        signal.alarm(0)
    print("Running memoized version...")
    t1 = time.time()
    print(can_sum_memoized(val, arr),
          "in {t:.2f} secs".format(t=time.time()-t1))
