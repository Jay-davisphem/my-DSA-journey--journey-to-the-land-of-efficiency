def seconnd_largest(arr: list) -> int:
    if len(arr) < 2:
        return None
    largest_ind = 0
    second_largest_ind = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[largest_ind]:
            largest_ind = i
    for i in range(1, len(arr)):
        if arr[i] > arr[second_largest_ind] and i != largest_ind:
            second_largest_ind = i

    return second_largest_ind


def sec_larg(arr: list) -> int:
    if len(arr) < 2:
        return None
    largest_ind = 0
    second_largest_ind = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[second_largest_ind]:
            if arr[i] > arr[largest_ind]:
                largest_ind, second_largest_ind = i, largest_ind
            else:
                second_largest_ind = i
    return second_largest_ind


a = list(map(int, input().split()))
print(sec_larg(a))
