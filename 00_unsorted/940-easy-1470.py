# https://leetcode.com/problems/shuffle-the-array/description/
import time
import itertools


class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        return list(itertools.chain(*(zip(nums[:n], nums[n:]))))


if __name__ == '__main__':
    tests = [
        ('test_00', ([2, 5, 1, 3, 4, 7], 3), [2, 3, 5, 4, 1, 7]),
        ('test_01', ([1, 2, 3, 4, 4, 3, 2, 1], 4), [1, 4, 2, 3, 3, 2, 4, 1]),
        ('test_02', ([1, 1, 2, 2], 2), [1, 2, 1, 2]),
    ]

    foo = Solution()
    method2test = Solution.shuffle

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
