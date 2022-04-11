from typing import List


def count_invertions(arr: List[int]) -> int:
    """'An iterative and brute force(O(n^2)) approach of counting the number of invertions in an array(usefull in recommendations system"""
    n = len(arr)
    n_inv = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                n_inv += 1
    return n_inv


def merge_count_split(l_arr: List[int], r_arr: List[int]):
    """
    count split of recursive count_inversions
    by using merge.
    """
    l = len(l_arr)
    r = len(r_arr)
    n = l + r
    split_arr = [0] * n
    split_count = 0
    i = j = 0
    for k in range(n):
        if i == l or j == r:
            break
        if l_arr[i] < r_arr[j]:
            split_arr[k] = l_arr[i]
            i += 1
        else:
            split_arr[k] = r_arr[j]
            split_count += l - i
            j += 1

    if i < l:
        split_arr[k:] = l_arr[i:]
    elif j < r:
        split_arr[k:] = r_arr[j:]

    return (split_arr, split_count)


def count_inversions_r(arr: List[int]):
    """An recursive and efficient(O(nlogn)) approach of counting
    the number of invertions in an array(usefull in recommendations system
    by partly using merge_sort
    """
    n = len(arr)
    if n < 2:
        return (arr, 0)
    else:
        l_arr, l_count = count_inversions_r(arr[: n // 2])
        r_arr, r_count = count_inversions_r(arr[n // 2 :])
        split_arr, split_count = merge_count_split(l_arr, r_arr)
        return (split_arr, l_count + r_count + split_count)


print(count_inversions_r([1, 3, 5, 2, 4, 6]))
