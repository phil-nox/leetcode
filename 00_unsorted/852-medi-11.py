# https://leetcode.com/problems/container-with-most-water/description/
# git commit -m "2023_08_30 - 852 - medi -   11"
import time


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left: int = 0
        righ: int = len(height) - 1
        level: int
        rlt:  int = 0

        while left < righ:
            level = (righ - left) * min(height[left], height[righ])
            rlt = level if level > rlt else rlt
            left, righ = (left + 1, righ) if height[righ] > height[left] else (left, righ - 1)

        return rlt



if __name__ == '__main__':
    tests = [
        ('test_00', ([1, 8, 6, 2, 5, 4, 8, 3, 7],), 49),
        ('test_01', ([1, 1],), 1),
        ('test_02', ([2, 1],), 1),
    ]

    foo = Solution()
    method2test = Solution.maxArea
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
