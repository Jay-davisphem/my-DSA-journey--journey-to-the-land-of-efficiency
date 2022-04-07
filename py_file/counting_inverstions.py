from typing import List


def count_invertions(arr: List[int]) -> int:
    """'An iterative and brute force(O(n^2)) approach of counting the number of invertions in an array(usefull in recommendations system"""
    n = len(arr)
    n_inv = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                n_inv += 1
    return n_inv


def count_split(arr: List[int]):
    """count split of recursive count_inversions"""
    pass


def count_inversions(arr: List[int]):
    """'An recursive and efficient(O(nlogn)) approach of counting the number of invertions in an array(usefull in recommendations system"""
    ...


print(count_invertions([1, 3, 5, 2, 4, 6]))
