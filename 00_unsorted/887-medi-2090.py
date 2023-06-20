# https://leetcode.com/problems/k-radius-subarray-averages/description/
# 00 : 33 : 42
import time


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        rlt = [-1] * len(nums)  # create default rlt
        if len(nums) < (2 * k + 1):  # case window > len_array
            return rlt

        low, replace, top = 0, k, 2 * k + 1  # start replacing defaults values
        cur, div = sum(nums[:(2 * k + 1)]), 2 * k + 1
        rlt[replace] = cur // div

        while top < len(nums):
            cur += -nums[low] + nums[top]
            low, top, replace = low + 1, top + 1, replace + 1
            rlt[replace] = cur // div

        return rlt
        

if __name__ == '__main__':
    tests = [
        ('test_00', ([7, 4, 3, 9, 1, 8, 5, 2, 6], 3), [-1, -1, -1, 5, 4, 4, -1, -1, -1]),
        ('test_01', ([100000], 0), [100000]),
        ('test_02', ([8], 100000), [-1]),
    ]

    foo = Solution()
    method2test = Solution.getAverages
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
