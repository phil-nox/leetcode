# https://leetcode.com/problems/find-xor-beauty-of-array/description/
import time


class Solution:
    def xorBeauty(self, nums: list[int]) -> int:
        rlt = 0
        for el in nums:
            rlt ^= el
        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([1, 4],), 5),
        ('test_01', ([15, 45, 20, 2, 34, 35, 5, 44, 32, 30],), 34),
    ]

    foo = Solution()
    method2test = Solution.xorBeauty   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
