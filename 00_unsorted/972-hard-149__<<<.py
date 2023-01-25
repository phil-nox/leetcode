# https://leetcode.com/problems/max-points-on-a-line/description/
import time
from typing import Optional
'''
https://en.wikipedia.org/wiki/Linear_equation#Two-point_form

(1,1) and (2,2)
y = kx + b

k = (two[1] - one[1])/(two[0] - one[0])
b = one[1] - k * one[0]

'''


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        if len(points) == 1:
            return 1
        vault: dict[tuple[Optional[float], float], set[int]] = dict()

        for idx in range(len(points)):
            one = points[idx]
            for jdx in range(idx + 1, len(points)):
                two = points[jdx]
                k = (two[1] - one[1])/(two[0] - one[0]) if two[0] != one[0] else None
                b = one[1] - k * one[0] if two[0] != one[0] else one[0]

                line = vault.get((k, b), None)
                if line is None:
                    line = set()
                    vault[(k, b)] = line
                line.update((idx, jdx))
        return max([len(el) for el in vault.values()])


if __name__ == '__main__':
    tests = [
        ('test_00', ([[1, 1], [2, 2], [3, 3]],), 3),
        ('test_01', ([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]],), 4),
        ('test_02', ([[0, 0]],), 1),
    ]

    foo = Solution()
    method2test = Solution.maxPoints   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
