from typing import List
import numpy as np


def can_sum(n: int, arr: List[int]) -> bool:
    tab_arr = np.full(n+1, fill_value=False, dtype=bool)
    tab_arr[0] = True
    for ind in range(n+1):
        if tab_arr[ind]:
            for each in arr:
                if ind+each <= n:
                    tab_arr[ind+each] = True
    return tab_arr[n]


if __name__ == "__main__":
    n = 300
    arr = [7, 14]
    res = can_sum(n, arr)
    print(f"Res: {res}")
