from typing import List


def best_sum(n: int, arr: List[int]) -> List[int]:
    res = [None] * (n+1)
    res[0] = []
    for ind in range(n+1):
        if res[ind] is not None:
            for val in arr:
                if ind + val <= n:
                    if res[ind+val] is None or len(res[ind+val])-1 > len(res[ind]):
                        res[ind+val] = [val] + res[ind]
    return res[n]


if __name__ == "__main__":
    n = 10
    arr = [1, 2, 3]
    res = best_sum(n, arr)
    print(f"Res: {res}")
