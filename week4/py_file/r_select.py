"""This module is a collection of selection algorithms"""
from typing import List
import random

# This function returns k'th smallest
# element in arr[l..r] using QuickSort
# based method. ASSUMPTION: ELEMENTS
# IN ARR[] ARE DISTINCT
def r_select(arr, l, r, k):

    # If k is smaller than number of
    # elements in array
    if k > 0 and k <= r - l + 1:

        # Partition the array around a random
        # element and get position of pivot
        # element in sorted array
        pos = random_partition(arr, l, r)

        # If position is same as k
        if pos - l == k - 1:
            return arr[pos]
        if pos - l > k - 1:  # If position is more,
            # recur for left subarray
            return r_select(arr, l, pos - 1, k)

        # Else recur for right subarray
        return r_select(arr, pos + 1, r, k - pos + l - 1)

    # If k is more than the number of
    # elements in the array
    return -1


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


# Standard partition process of QuickSort().
# It considers the last element as pivot and
# moves all smaller element to left of it and
# greater elements to right. This function
# is used by random_partition()
def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= x:
            swap(arr, i, j)
            i += 1
    swap(arr, i, r)
    return i


# Picks a random pivot element between l and r
# and partitions arr[l..r] around the randomly
# picked element using partition()
def random_partition(arr, l, r):
    n = r - l + 1
    pivot = random.randint(0, n - 1)
    swap(arr, l, l + pivot)  # making the first the pivot element
    # swap(arr, l + pivot, r) # making the last the pivot element
    return partition(arr, l, r)


# Test Code
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    n = len(arr)
    k = int(input())
    print(f"{k}'th smallest element is", r_select(arr, 0, n - 1, k))
