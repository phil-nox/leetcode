# https://leetcode.com/problems/last-day-where-you-can-still-cross/description/
import time
from dataclasses import dataclass


@dataclass(slots=True)
class Pool:
    left:       int
    right:      int
    point_s:    set[tuple[int, int]]

    @classmethod
    def merge(cls, point: tuple[int, int], pool_s: list['Pool']) -> tuple['Pool', set[tuple[int, int]]]:
        pnt_s2update = {point}
        the_pool = max(pool_s, key=lambda x: len(x.point_s))

        the_pool.point_s.add(point)
        the_pool.left = point[1] if point[1] < the_pool.left else the_pool.left
        the_pool.right = point[1] if point[1] > the_pool.right else the_pool.right

        for another in pool_s:
            if another is the_pool:
                continue
            pnt_s2update |= another.point_s
            the_pool.point_s |= another.point_s
            the_pool.left = another.left if another.left < the_pool.left else the_pool.left
            the_pool.right = another.right if another.right > the_pool.right else the_pool.right

        return the_pool, pnt_s2update


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        rlt: int = 0
        vault: dict[tuple[int, int], Pool] = dict()                         # coordinates 2 corresponding Pool
        touched: list[Pool]
        for r, c in cells:
            rlt, r, c = rlt + 1, r - 1, c - 1
            touched = []
            for n_r, n_c in (
                    (r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
                    (r, c - 1), (r, c + 1),
                    (r + 1, c - 1), (r + 1, c), (r + 1, c + 1),
            ):
                if n_r < 0 or n_r >= row or n_c < 0 or n_c >= col:                          # + - borders
                    continue                                                                # |

                if (n_r, n_c) in vault:                                                     # + - touch a pool
                    touched.append(vault[(n_r, n_c)])                                       # |

            if not touched:                                                             # + - create new pool
                vault[(r, c)] = Pool(left=c, right=c, point_s={(r, c)})                 # |
                continue                                                                # |

            the_pool, to_update = Pool.merge((r, c), touched)                           # + - merge logic

            if the_pool.left == 0 and the_pool.right == col - 1:                        # + - done logic
                return rlt - 1                                                          # |

            for pnt in to_update:                                                       # + - update the vault
                vault[pnt] = the_pool                                                   # |

        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', (3, 3, [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]), 3),
    ]

    foo = Solution()
    method2test = Solution.latestDayToCross
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
