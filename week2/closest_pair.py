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


def closest_pair_2d(Px: List[Tuple], Py: List[Tuple[int]]) -> Tuple[Tuple[int]]:
    ...


if __name__ == "__main__":
    print(closest_pair_1d([1, 9, 2, 5, 21, 7, 3, 8, 3, 9, 3, 6, 7, 9, 3, 134, 3]))
