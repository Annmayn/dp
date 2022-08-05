from types import FrameType
from typing import List, Deque
import time
import signal
from collections import deque


def all_construct(val: str, arr: List[str]) -> List[Deque[str]]:
    final_res = []
    if val == "":
        return [deque()]
    for substr in arr:
        if len(substr) <= len(val) and substr == val[:len(substr)]:
            new_val = val[len(substr):]
            res = all_construct(new_val, arr)
            for each in res:
                each.appendleft(substr)
            final_res.extend(res)
    return final_res


def all_construct_memoized(val: str, arr: List[str], memo: dict=None) -> List[Deque[str]]:
    if memo is None:
        memo = {}
    if val in memo:
        return memo[val]
    final_res = []
    if val == "":
        return [deque()]
    for substr in arr:
        if len(substr) <= len(val) and substr == val[:len(substr)]:
            new_val = val[len(substr):]
            res = all_construct_memoized(new_val, arr, memo)
            for each in res:
                each.appendleft(substr)
            final_res.extend(res)
    memo[val] = final_res
    return final_res


if __name__ == "__main__":
    def custom_handler(signum: int, stackframe: FrameType):
        raise Exception("Took too long to complete (>5 seconds)")

    signal.signal(signal.SIGALRM, custom_handler)
    val = "eeeeeeeeeeeeeeeeeeeeeeeeeef"
    arr = "e ee eee eeee eeeee eeeeee".split()

    try:
        signal.alarm(5)
        t1 = time.time()
        res = all_construct(val, arr)
        print("Result: {res} | Executed in {tm:.2f} seconds".format(
            res=res, tm=time.time()-t1))
    except Exception as e:
        print(e)
    finally:
        signal.alarm(0)
    try:
        signal.alarm(5)
        t1 = time.time()
        res = all_construct_memoized(val, arr)
        print("Result: {res} | Executed in {tm:.2f} seconds".format(
            res=res, tm=time.time()-t1))
    except Exception as e:
        print(e)
    finally:
        signal.alarm(0)
