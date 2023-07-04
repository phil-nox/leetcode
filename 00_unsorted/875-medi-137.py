# https://leetcode.com/problems/single-number-ii/description/
import time


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        a, b = 0b0, 0b0

        for n in nums:
            n_a = (~b & n) | (a & ~b) | (a & b & ~n)    # https://en.wikipedia.org/wiki/Karnaugh_map
            n_b = (~b & a & n) | (b & ~n)
            a, b = n_a, n_b
        return a


if __name__ == '__main__':
    tests = [
        ('test_00', ([0, 1, 0, 1, 0, 1, 99],), 99),
    ]

    foo = Solution()
    method2test = Solution.singleNumber
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
