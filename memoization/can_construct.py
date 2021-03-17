from typing import List, NewType
import signal
import time

def can_construct(val: str, arr: List) -> bool:
    if val == "":
        return True
    if val is None:
        return False

    for substr in arr:
        if len(substr) > len(val) or val[:len(substr)] != substr:
            new_val = None
        else:
            new_val = val[len(substr):]
        if can_construct(new_val, arr):
            return True
    return False


def can_construct_memoized(val: str, arr: List, memo: dict = None) -> bool:
    if memo is None:
        memo = {}
    if val in memo:
        return memo[val]
    if val == "":
        return True
    if val is None:
        return False

    for substr in arr:
        if len(substr) > len(val) or val[:len(substr)] != substr:
            new_val = None
        else:
            new_val = val[len(substr):]
        if can_construct_memoized(new_val, arr, memo):
            memo[val] = True
            return True
    memo[val] = False
    return False


if __name__ == "__main__":
    def custom_handler(signum, stackframe):
        raise Exception("Took too long to finish (>5 seconds)")
    signal.signal(signal.SIGALRM, custom_handler)
    val = 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef'
    arr = "e ee eee eeee eeeee eeeeee".split()
    # arr = ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boa']
    signal.alarm(5)
    try:
        t1 = time.time()
        print("Standard Result: {res} | Executed in {tm:.2f} seconds".format(res=can_construct(val, arr), tm=time.time()-t1))
    except Exception as e:
        print(e)
    finally:
        signal.alarm(0)
    t1 = time.time()
    print("Memoized Result: {res} | Executed in {tm:.2f} seconds".format(res=can_construct_memoized(val, arr), tm=time.time()-t1))
