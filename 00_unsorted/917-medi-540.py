# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
import time

'''
    def singleNonDuplicate(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        idx, jdx, mem, mid = 0, len(nums) // 2, 0, -1
        while mem != mid:
            mem, mid = mid, (jdx - idx) // 2 + idx
            idx, jdx = (mid, jdx) if nums[mid*2] == nums[mid*2+1] else (idx, mid)
        return nums[jdx*2]
'''


class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        idx, jdx, mem = 0, len(nums) // 2, -1
        while (mid := (jdx - idx) // 2 + idx) != mem and jdx != 0:
            idx, jdx, mem = (mid, jdx, mid) if nums[mid*2] == nums[mid*2+1] else (idx, mid, mid)
        return nums[jdx*2]


if __name__ == '__main__':
    tests = [
        ('test_00', ([1, 1, 2, 3, 3, 4, 4, 8, 8],), 2),
        ('test_01', ([3, 3, 7, 7, 10, 11, 11],), 10),
        ('test_02', ([1, 2, 2, 3, 3],), 1),
        ('test_03', ([1, 1, 2, 3, 3],), 2),
        ('test_04', ([1, 1, 2, 2, 3],), 3),
        ('test_05', ([1, 1, 2],), 2),
        ('test_06', ([1, 2, 2],), 1),
        ('test_07', ([1],), 1),
    ]

    foo = Solution()
    method2test = Solution.singleNonDuplicate

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
