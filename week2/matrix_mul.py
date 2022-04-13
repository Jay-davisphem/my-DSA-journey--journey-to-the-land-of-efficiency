from binhex import BinHex
from copy import deepcopy
from pprint import pprint

from typing import List


def mat_mul(A: List[List[int]], B: List[List[int]]):
    i_b = len(B)
    i_a = len(A)

    if i_a < 1 or i_b < 1:
        return []
    j_a = len(A[0])
    j_b = len(B[0])
    if j_a != i_b:
        raise Exception("Incompatible Array multiplication ")

    C = []
    for i in range(i_a):
        C.append([0] * j_b)
        for j in range(j_b):
            for k in range(j_b):
                C[i][j] += A[i][k] * B[k][j]
    return C


def div_to_four(arr):
    h_n = len(arr) // 2

    A = [[arr[i][j] for j in range(h_n)] for i in range(h_n)]
    B = [[arr[i][j + h_n] for j in range(h_n)] for i in range(h_n)]
    C = [[arr[i + h_n][j] for j in range(h_n)] for i in range(h_n)]
    D = [[arr[i + h_n][j + h_n] for j in range(h_n)] for i in range(h_n)]

    return A, B, C, D


[58, 52, 37, 42]
[126, 90, 48, 48]
[583, 208, 77, 169]
[232, 132, 89, 128]


def merge_to_one(A):
    return [
        A[0][0][0] + A[0][1][0],
        A[0][0][1] + A[0][1][1],
        A[1][0][0] + A[1][1][0],
        A[1][0][1] + A[1][1][1],
    ]


def mat_mul_r(X, Y):
    """
    Asymptotic running time = O(n^3)
    Does 8 recursive calls
    """
    n = len(X)
    if n == 1:
        return X[0][0] * Y[0][0]
    else:
        A, B, C, D = div_to_four(X)
        E, F, G, H = div_to_four(Y)

        AE = mat_mul_r(A, E)
        BG = mat_mul_r(B, G)
        CE = mat_mul_r(C, E)
        DG = mat_mul_r(D, G)
        AF = mat_mul_r(A, F)
        BH = mat_mul_r(B, H)
        CF = mat_mul_r(C, F)
        DH = mat_mul_r(D, H)

        return [[add(AE, BG), add(AF, BH)], [add(CE, DG), add(CF, DH)]]


def add(A, B):
    if isinstance(A, int):
        return A + B
    C = [[0 for _ in range(len(A))] for __ in range(len(A[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j] + B[i][j]
    return C


def sub(A, B):
    if isinstance(A, int):
        return A - B
    C = [[0 for _ in range(len(A))] for __ in range(len(A[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j] - B[i][j]
    return C


def printArray(A):
    for i in range(len(A)):
        pprint(A[i], width=20)


def strassen_mul(X, Y):
    """
    Asymptotic running time = O(n^(log3))(sub-cubic running time)
    safes one recursive call compared to conventional matrix
    multiplication doing 8 recursive calls
    """
    n = len(X)
    if n == 1:
        return X[0][0] * Y[0][0]
    else:
        A, B, C, D = div_to_four(X)
        E, F, G, H = div_to_four(Y)

        P1 = strassen_mul(A, sub(F, H))
        P2 = strassen_mul(add(A, B), H)
        P3 = strassen_mul(add(C, D), E)
        P4 = strassen_mul(D, sub(G, E))
        P5 = strassen_mul(add(A, D), add(E, H))
        P6 = strassen_mul(sub(B, D), add(G, H))
        P7 = strassen_mul(sub(A, C), add(E, F))

        return [
            [add(sub(add(P5, P4), P2), P6), add(P1, P2)],
            [add(P3, P4), sub(sub(add(P1, P5), P3), P7)],
        ]


# import os


# print(add([[2, 4], [3, 5]], [[2, 5], [2, 3]]), "akjfkkaj")
printArray(
    merge_to_one(
        strassen_mul(
            [[1, 2, 3, 6], [3, 4, 2, 9], [23, 6, 9, 1], [7, 8, 9, 2]],
            [[23, 6, 0, 3], [7, 8, 5, 3], [1, 2, 5, 9], [3, 4, 2, 1]],
        )
    )
)
# os.system("clear")
# 1 2  1 2 3
# 1 2  1 2 3
# 1 2
