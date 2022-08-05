import numpy as np
def fib(n: int) -> int:
    arr = np.zeros((n+1,), dtype=int)
    arr[1] = 1
    for i in range(2, len(arr)):
        arr[i] = arr[i-2] + arr[i-1]
    return arr[n]


if __name__ == "__main__":
    n = 20
    res =fib(n)
    print(res)