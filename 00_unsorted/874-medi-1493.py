# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/
import time


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        rlt: int = 0
        only_one: int = 1
        old, cur = 0, 0

        for el in nums:
            if el == 1:
                cur += 1
                continue
            rlt = max(rlt, old + cur)
            only_one = 0
            old, cur = cur, 0
        return max(rlt, old + cur - only_one)
        

if __name__ == '__main__':
    tests = [
        ('test_00', ([0, 1, 1, 1, 0, 1, 1, 0, 1],), 5),
        ('test_01', ([1, 1, 1, 1, 1],), 4),
    ]

    foo = Solution()
    method2test = Solution.longestSubarray
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
