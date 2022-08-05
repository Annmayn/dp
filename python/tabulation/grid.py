from typing import Tuple
import numpy as np


def grid(shape: Tuple[int, int]) -> int:
    _actual_row, _actual_col = shape
    _row, _col = shape[0]+1, shape[1]+1
    arr = np.zeros(shape=(_row, _col), dtype=int)
    arr[1][1] = 1
    for row in range(1, _row):
        for col in range(1, _col):
            if col+1 <= _actual_col:
                arr[row][col+1] += arr[row][col]
            if row+1 <= _actual_row:
                arr[row+1][col] += arr[row][col]
    return arr[_actual_row][_actual_col]


if __name__ == "__main__":
    n = (18, 18)
    res = grid(n)
    print(res)
