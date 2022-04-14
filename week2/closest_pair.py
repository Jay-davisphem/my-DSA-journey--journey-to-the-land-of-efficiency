from ctypes.wintypes import LPSC_HANDLE
from imp import source_from_cache
from typing import List, Tuple, TypeVar


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


def dist_sq(p1: Tuple[int], p2: Tuple[int]):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def min_base(Px: List[Tuple]) -> Tuple[Tuple[int]]:
    if len(Px) < 2:
        return None
    elif len(Px) == 2:
        return Px
    elif len(Px) == 3:
        p1, p2, p3 = Px[0], Px[1], Px[2]
        new_p = [
            ((p1, p2), dist_sq(p1, p2)),
            ((p1, p3), dist_sq(p1, p3)),
            ((p2, p3), dist_sq(p2, p3)),
        ]
        return min(new_p, key=lambda P: P[-1])[0]


def best_of_pairs(P: Tuple[Tuple[Tuple[int]]]):
    fin = [(p, dist_sq(*p)) for p in P if p[0] != None]
    return min(fin, key=lambda p: p[-1])


def filter_pairs(Py: List[Tuple[int]], x: int, delta: int):
    l_b = x - delta
    u_b = x + delta
    new_Py: List[Tuple[int]] = []
    for i, j in Py:
        if l_b <= i <= u_b:
            new_Py.append((i, j))
    return new_Py


def closest_split_pair(
    Px: List[Tuple], Py: List[Tuple[int]], delta: int
) -> Tuple[Tuple[int]]:
    n = len(Px)
    x = Px[n // 2][0]
    Sy = filter_pairs(Py, x, delta)
    l = len(Sy)
    best = delta
    best_pair = (None, None)
    for i in range(l - 1):
        for j in range(min(7, l - 1)):
            if dist_sq(Sy[i], Sy[i + j]) < best:
                best = dist_sq(Sy[i], Sy[i + j])
                best_pair = Sy[i], Sy[i + j]
    return best_pair


def closest_pair_2d(Px: List[Tuple], Py: List[Tuple[int]]) -> Tuple[Tuple[int]]:
    if len(Px) <= 3:
        return min_base(Px)
    else:
        n_hf = len(Px) // 2
        Lx = Px[:n_hf]
        Ly = Py[:n_hf]
        Rx = Px[n_hf:]
        Ry = Py[n_hf:]

        l1, l2 = closest_pair_2d(Lx, Ly)
        r1, r2 = closest_pair_2d(Rx, Ry)

        delta = best_of_pairs(((l1, l2), (r1, r2)))[-1]

        s1, s2 = closest_split_pair(Px, Py, delta)
        return best_of_pairs(((l1, l2), (r1, r2), (s1, s2)))[0]


def closest_pair_2d_sorted(P: List[Tuple]):
    Px = sorted(P, key=lambda p: p[0])
    Py = sorted(P, key=lambda p: p[1])
    return closest_pair_2d(Px, Py)


if __name__ == "__main__":
    print(closest_pair_1d([1, 9, 2, 5, 21, 7, 3, 8, 3, 9, 3, 6, 7, 9, 3, 134, 3]))
