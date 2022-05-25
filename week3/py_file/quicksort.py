"""Quicksort Algorithm Implementations"""
from typing import List
from random import randint


def partition_sm(arr: List[int], piv: int):
    """partition with O(n) space complexity"""
    part_1 = [x for x in arr if x < piv]
    part_2 = [x for x in arr if x >= piv]
    return part_1, part_2


def partition(arr: List[int], l: int, r: int):
    """partition with O(1) space complexity"""
    if arr:
        piv = arr[l]
        i = l + 1
        for j in range(l + 1, r + 1):
            if arr[j] < piv:  # restore the invariant arr[j] > piv
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        # `i - 1` is index of the rightmost smaller value smaller than arr[l](pivot)
        arr[l], arr[i - 1] = arr[i - 1], arr[l]

        return i - 1, r - l  # final index of the pivot
    raise IndexError("Empty Array")


def pivot_naive_first(arr: List[int], l: int, r: int):
    return l


def pivot_naive_last(arr: List[int], l: int, r: int):
    return r


def pivot_overkill(arr: List[int], l: int, r: int):
    """Using median
    new_arr = arr[:r]
    for i in range(r, l+1):
        new_arr.append((i, arr[i]))
    new_arr_s = arr[:r] + sorted(new_arr[r:])
    return new_arr_s[len(new_arr)//2 + r][0]"""

    new_arr = []
    for i in range(len(arr)):
        new_arr.append([i, arr[i]])
    new_arr = new_arr[l : r + 1]
    return sorted(new_arr, key=lambda x: x[1])[len(new_arr) // 2][0]


def pivot_stan_med(arr: List[int], l: int, r: int):
    m = (l + r) // 2
    new_arr = [(l, arr[l]), (m, arr[m]), (r, arr[r])]
    return sorted(new_arr, key=lambda x: x[1])[1][0]


def pivot_random(arr: List[int], l: int, r: int):
    """Using uniform random distribution"""
    return randint(l, r)


def quicksort_sm(arr: List[int]):
    """Use O(n) space complexity partition in sorting"""
    if len(arr) < 2:
        return arr
    piv = arr.pop(pivot(arr, 0, len(arr) - 1))
    part_1, part_2 = partition_sm(arr, piv)
    return quicksort_sm(part_1) + [piv] + quicksort_sm(part_2)


def quicksort(arr: List[int], l: int, r: int):
    """O(nlogn) sorting algorithm using partion O(n) with O(1) space complexity"""
    c = 0
    if l >= r:
        return c
    i = pivot(arr, l, r)
    arr[l], arr[i] = arr[i], arr[l]
    j, c = partition(arr, l, r)
    c += quicksort(arr, l, j - 1)
    c += quicksort(arr, j + 1, r)
    return c


if __name__ == "__main__":
    with open(input(), "r") as f:
        t_raw = list(map(lambda x: int(x.strip()), f.readlines()))

    vals = t_raw.copy()
    pivot = pivot_overkill
    co = quicksort(vals, 0, len(vals) - 1)
    print("overkill", co)

    vals = t_raw.copy()
    pivot = pivot_naive_first
    co = quicksort(vals, 0, len(vals) - 1)
    print("first", co)

    vals = t_raw.copy()
    pivot = pivot_naive_last
    co = quicksort(vals, 0, len(vals) - 1)
    print("last", co)

    vals = t_raw.copy()
    pivot = pivot_stan_med
    co = quicksort(vals, 0, len(vals) - 1)
    print("fake median", co)

    print(vals)
