# https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/description/

import time
from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        rlt = 0
        left_enemy, right_enemy = None, None
        for el in forts:
            if el == 1:
                if right_enemy is not None:
                    rlt = max(right_enemy, rlt)
                    right_enemy = None
                left_enemy = 0
            elif el == 0:
                if left_enemy is not None:
                    left_enemy += 1
                if right_enemy is not None:
                    right_enemy += 1
            elif el == -1:
                if left_enemy is not None:
                    rlt = max(left_enemy, rlt)
                    left_enemy = None
                right_enemy = 0
        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([1, 0, 0, -1, 0, 0, 0, 0, 1],), 4),
        ('test_01', ([0, 0, 1, -1],), 0),
    ]

    foo = Solution()
    method2test = Solution.captureForts   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)

