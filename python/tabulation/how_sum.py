from typing import List


def how_sum(n: int, arr: List[int]) -> List[int]:
    res_arr = [None] * (n+1)
    res_arr[0] = []
    for ind in range(n+1):
        if res_arr[ind] is not None:
            for arr_val in arr:
                if ind + arr_val <= n:
                    res_arr[ind+arr_val] = [arr_val] + res_arr[ind]
    return res_arr[n]


if __name__ == "__main__":
    n = 10
    arr = [1, 2, 3]
    res = how_sum(n, arr)
    print(f"Res: {res}")
