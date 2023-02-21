# https://leetcode.com/problems/search-insert-position/description/
import time

''' version_0
    def searchInsert(self, nums: list[int], target: int) -> int:
        idx, jdx = 0, len(nums)
        while True:
            mid = (jdx - idx) // 2 + idx
            if target > nums[mid]:
                if idx == mid:              # case out_of_range_right  test_00  [15, 16] -> mid = 15
                    return jdx
                idx = mid
            elif target < nums[mid]:
                jdx = mid
                if idx == jdx:              # case out_of_range_left  test_00   [0, 0] -> mid = 0
                    return jdx  # <=> return idx
            else:
                return mid
'''


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        idx, jdx, mem, mid = 0, len(nums), 0, -1
        while mem != mid:
            mem, mid = mid, (jdx - idx) // 2 + idx
            if target == nums[mid]:
                return mid
            idx, jdx = (mid, jdx) if target > nums[mid] else (idx, mid)
        return jdx      # top index


if __name__ == '__main__':
    tests = [
        ('test_00', ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], -16), 0),
        ('test_00', ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 32), 16),

        ('test_01', ([0, 1, 2, 3, 4, 5], 0), 0),
        ('test_02', ([0, 1, 2, 3, 4, 5], 1), 1),
        ('test_03', ([0, 1, 2, 3, 4, 5], 2), 2),
        ('test_04', ([0, 1, 2, 3, 4, 5], 3), 3),
        ('test_05', ([0, 1, 2, 3, 4, 5], 4), 4),
        ('test_06', ([0, 1, 2, 3, 4, 5], 5), 5),
        ('test_07', ([0, 1, 2, 3, 4, 5], 6), 6),

        ('test_08', ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 0), 0),
        ('test_09', ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 1), 1),
        ('test_10', ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 2), 2),
        ('test_11', ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 3), 3),

        ('test_12', ([1, 3, 5, 6], 5), 2),
        ('test_13', ([1, 3, 5, 6], 2), 1),
        ('test_14', ([1, 3, 5, 6], 7), 4),
    ]

    foo = Solution()
    method2test = Solution.searchInsert

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
