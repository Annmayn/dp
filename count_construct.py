from typing import List
import time
import signal


def count_construct(val: str, arr: List[str]) -> int:
    count: int = 0
    if val == "":
        return 1
    if val is None:
        return 0
    for substr in arr:
        tmp_count: int = 0
        if len(substr) > len(val) or substr != val[:len(substr)]:
            new_val = None
        else:
            new_val = val[len(substr):]
        res = count_construct(new_val, arr)
        count += res
    return count


def count_construct_memoized(val: str, arr: List[str], memo: dict = None) -> int:
    count: int = 0
    if memo is None:
        memo = {}
    if val in memo:
        return memo[val]
    if val == "":
        return 1
    if val is None:
        return 0
    for substr in arr:
        tmp_count: int = 0
        if len(substr) > len(val) or substr != val[:len(substr)]:
            new_val = None
        else:
            new_val = val[len(substr):]
        res = count_construct_memoized(new_val, arr, memo)
        memo[val] = res
        count += res
    return count


if __name__ == "__main__":
    def custom_handler(signum, stackframe):
        raise Exception("Took too long to complete (>5 seconds)")

    signal.signal(signal.SIGALRM, custom_handler)
    val = "eeeeeeeeeeeeeeeeeeeeeeeeeef"
    arr = "e ee eee eeee eeeee eeeeee eeeeeee".split()

    try:
        signal.alarm(5)
        t1 = time.time()
        res = count_construct(val, arr)
        print("Result: {res} | Executed in {tm:.2f} seconds".format(
            res=res, tm=time.time()-t1))
    except Exception as e:
        print(e)
    finally:
        signal.alarm(0)
    t1 = time.time()
    res = count_construct_memoized(val, arr)
    print("Result: {res} | Executed in {tm:.2f} seconds".format(
        res=res, tm=time.time()-t1))
