# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
import time


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        write_idx, read_idx, check = 1, 0, nums[0]
        while (read_idx := read_idx + 1) < len(nums):
            if nums[read_idx] != check:
                nums[write_idx] = check = nums[read_idx]
                write_idx += 1
        return write_idx


if __name__ == '__main__':
    tests = [
        ('test_00', ([1, 1, 2],), 2),
        ('test_01', ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4],), 5),
    ]

    foo = Solution()
    method2test = Solution.removeDuplicates

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
