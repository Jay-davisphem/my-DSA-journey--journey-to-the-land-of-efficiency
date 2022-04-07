from typing import List


def count_invertions(arr: List[int]) -> int:
    """'An iterative and brute force approach of counting the number of invertions in an array(usefull in recommendations system"""
    n = len(arr)
    n_inv = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                n_inv += 1
    return n_inv


print(count_invertions([1, 3, 5, 2, 4, 6]))
