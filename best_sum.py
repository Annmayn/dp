from typing import List
import signal
import time


def best_sum(val: int, arr: List) -> List:
    shortest_answer = []
    if val == 0:
        return []
    if val < 0:
        return None

    for each in arr:
        new_val = val - each
        res = best_sum(new_val, arr)
        if res is not None:
            res.append(each)
            if len(shortest_answer) == 0 or len(res) < len(shortest_answer):
                shortest_answer = res
    return shortest_answer or None


def best_sum_memoized(val: int, arr: List, memo: dict = None) -> List:
    if memo is None:
        memo = {}
    if val in memo:
        return memo[val]
    shortest_answer = []
    if val == 0:
        return []
    if val < 0:
        return None

    for each in arr:
        new_val = val - each
        res = best_sum_memoized(new_val, arr, memo)
        if res is not None:
            res_copy = res.copy()
            res_copy.append(each)
            if len(shortest_answer) == 0 or len(res_copy) < len(shortest_answer):
                shortest_answer = res_copy
    memo[val] = shortest_answer or None
    return shortest_answer or None


if __name__ == "__main__":
    val = 101
    arr = [1, 2, 3, 4]

    def custom_handler(signum: int, stackframe):
        raise Exception("Took too long (>5 seconds) to finish!")
    signal.signal(signal.SIGALRM, custom_handler)
    signal.alarm(5)
    try:
        t1 = time.time()
        res = best_sum(val, arr)
        t2 = time.time()
        print(f"Result: {res} | Execution time: {t2-t1:.2f} seconds")
    except Exception as e:
        print(e)
    finally:
        signal.alarm(0)

    t1 = time.time()
    res = best_sum_memoized(val, arr)
    t2 = time.time()
    print(f"Result: {res} | Execution time: {t2-t1:.2f} seconds")
