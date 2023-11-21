# https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/description/
import time

'''
class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        min_idx = 0
        max_idx = 0

        for idx in range(len(nums)):
            if nums[idx] < nums[min_idx]:
                min_idx = idx
            elif nums[idx] >= nums[max_idx]:
                max_idx = idx

        rlt = len(nums) - 1 - max_idx + min_idx   
        return rlt - 1 if min_idx > max_idx else rlt
'''


class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        s_idx = nums.index(min(nums))               # start_index
        e_idx = nums[-1::-1].index(max(nums))       # end_index
        return e_idx + s_idx - 1 if s_idx > len(nums) - 1 - e_idx else e_idx + s_idx
        

if __name__ == '__main__':
    tests = [
        ('test_00', ([3,4,5,5,3,1],), 6),
    ]

    foo = Solution()
    method2test = Solution.minimumSwaps
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
