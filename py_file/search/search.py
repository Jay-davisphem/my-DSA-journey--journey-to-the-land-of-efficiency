from typing import Any, List


def linear_search_r(arr: List[Any], low: int, high: int, key: Any):
    if high < low:
        return "NOT_FOUND"
    if arr[low] == key:
        return low
    return linear_search_r(arr, low + 1, high, key)


def binary_search_r(arr: List[Any], low: int, high: int, key: Any):
    if high < low:
        return low - 1
    mid = (low + high) // 2
    if key == arr[mid]:
        return mid
    elif key < arr[mid]:
        return binary_search_r(arr, low, mid - 1, key)
    else:
        return binary_search_r(arr, mid + 1, high, key)


def binary_search(arr: List[Any], low: int, high: int, key: Any):
    while low <= high:
        mid = (low + high) // 2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return low - 1
