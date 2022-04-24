from typing import List


def partition(arr: List[int], p: int):
    return arr[: len(arr) // 2], arr[len(arr) // 2 :]


def pivot(arr: List[int]):
    return arr[0]


def quicksort(arr: List[int]):
    if len(arr) == 1:
        return
    p = pivot(arr)
    part1, part2 = partition(arr, p)
    quicksort(part1)
    quicksort(part2)
