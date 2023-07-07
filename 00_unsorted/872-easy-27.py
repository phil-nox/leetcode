# https://leetcode.com/problems/remove-element/description/
import time


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        rlt, low = len(nums), 0

        while low < rlt:
            if nums[low] == val:
                nums[low], rlt = nums[rlt - 1], rlt - 1
                continue
            low += 1
        return rlt
        

if __name__ == '__main__':
    tests = [
        ('test_00', ([0, 1, 2, 2, 3, 0, 4, 2], 2), 5),
    ]

    foo = Solution()
    method2test = Solution.removeElement
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
