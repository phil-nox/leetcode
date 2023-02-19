# https://leetcode.com/problems/minimum-impossible-or/description/
import time


class Solution:
    def minImpossibleOR(self, nums: list[int]) -> int:
        vault, rlt = set(nums), 1
        while rlt in vault:
            rlt <<= 1      # rlt *= 2
        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([2, 1],), 4),
        ('test_01', ([5, 3, 2],), 1),
    ]

    foo = Solution()
    method2test = Solution.minImpossibleOR

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
