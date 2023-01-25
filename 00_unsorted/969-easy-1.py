# https://leetcode.com/problems/two-sum/description/
import time


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        vault: dict[int, int] = dict()
        for idx in range(len(nums)):
            jdx = vault.get(target - nums[idx], None)
            if jdx is not None:
                return [jdx, idx]
            vault[nums[idx]] = idx
        return []   # never_will - one valid answer exists


if __name__ == '__main__':
    tests = [
        ('test_00', ([2, 7, 11, 15], 9), [0, 1]),
        ('test_01', ([3, 2, 4], 6), [1, 2]),
        ('test_02', ([3, 3], 6), [0, 1]),
    ]

    foo = Solution()
    method2test = Solution.twoSum   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
