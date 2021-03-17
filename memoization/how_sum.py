from typing import List
import time
import signal

def has_sum(val: int, arr: List) -> List:
    if val == 0:
        return []
    if val < 0:
        return None
    for each in arr:
        new_val = val-each
        res =  has_sum(new_val, arr)
        if res is not None:
            res.append(each)
            return res
    return None

def has_sum_memoized(val: int, arr: List, memo: dict = None) -> List:
    if memo is None:
        memo = {}
    if val in memo:
        return memo[val]
    if val == 0:
        return []
    if val < 0:
        return None
    for each in arr:
        new_val = val-each
        res =  has_sum_memoized(new_val, arr, memo)
        if res is not None:
            res.append(each)
            memo[val] = res
            return res
    memo[val] = None
    return None

if __name__ == '__main__':
    def timeout_handler(signum: int, stack_frame):
        raise Exception("Took longer than 10 seconds")
    signal.signal(signal.SIGALRM, timeout_handler)
    val = 100
    arr = [3, 3, 3]
    signal.alarm(10)
    try:
        t1 = time.time()
        res = has_sum(val, arr)
        t2 = time.time()
        print("Result: {res} in {tm:.2f} seconds".format(res=res, tm=t2-t1))
    except Exception as e:
        print(e)
    t1 = time.time()
    res = has_sum_memoized(val, arr)
    t2 = time.time()
    print("Result: {res} in {tm:.2f} seconds".format(res=res, tm=t2-t1))
