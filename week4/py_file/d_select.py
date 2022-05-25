from typing import List


def d_select(arr: List[int], l: int, r: int, i: int):
    if len(arr) == 1:
        return arr[0]

    grp = (r - l + 1) // 5

    C = [0] * (grp + 1)
    for h in range(l, grp):
        C[h] = arr[h * 5 + 2 : h * 5 + 5 : 5][0]

    p = d_select(C, 0, len(C) - 1, grp)
    j = d_partition(arr, l, r, arr.index(p))
    if j - l == i - 1:
        return arr[j]
    elif j - l > i - 1:
        return d_select(arr, l, j - 1, i)
    else:
        return d_select(arr, j + 1, r, i - j + l - 1)

def pivot(C, l, r):
    grp = (r - l + 1) // 5

    C = [0] * (grp + 1)
    for h in range(l, grp):
        C[h] = arr[h * 5 + 2 : h * 5 + 5 : 5][0]



def swap(arr: List[int], i: int, j: int):
    print(f"len[{arr}], [{i, j}]")
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= x:
            swap(arr, i, j)
            i += 1
    swap(arr, i, r)
    return i


def d_partition(arr: List[int], l: int, r: int, pivot: int):
    n = r - l + 1
    swap(arr, l, l + pivot)  # making the first the pivot element
    return partition(arr, l, r)


# Test Code
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    n = len(arr)
    k = int(input())
    print(f"{k}'th smallest element is", d_select(arr, 0, n - 1, k))
