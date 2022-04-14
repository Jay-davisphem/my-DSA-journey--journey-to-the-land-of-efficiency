from ctypes.wintypes import LPSC_HANDLE
from imp import source_from_cache
from typing import List, Tuple


def closest_pair_1d(x: List):
    x = sorted(x)
    x1 = x[0]
    x2 = x[1]
    m_v = x2 - x1
    for i in range(1, len(x) - 1):
        n_val = x[i + 1] - x[i]
        if m_v > n_val:
            m_v, x1, x2 = n_val, x[i], x[i + 1]
    return x1, x2


def dist_sq(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def min_base(Px: List[Tuple], Py: List[Tuple[int]]) -> Tuple[Tuple[int]]:
    if len(Px) < 2:
        return None
    elif len(Px) == 2:
        return Px
    elif len(Px) == 3:
        p1, p2, p3 = Px[0], Px[1], Px[2]


def closest_pair_2d(Px: List[Tuple], Py: List[Tuple[int]]) -> Tuple[Tuple[int]]:
    if len(Px) <= 3:
        return min_base(Px, Py)
    else:
        ...


if __name__ == "__main__":
    print(closest_pair_1d([1, 9, 2, 5, 21, 7, 3, 8, 3, 9, 3, 6, 7, 9, 3, 134, 3]))
