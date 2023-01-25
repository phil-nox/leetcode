# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
import time
from dataclasses import dataclass

''' # sort_solution_with_sorting_by_end_of_interval
class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[1])
        rlt, win_right = 0, points[0][1]

        for el in points[1:]:
            if el[0] <= win_right:
                continue
            rlt, win_right = rlt + 1, el[1]
        return rlt + 1
'''

''' # sort_solution
class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()
        rlt, win_right = 0, points[0][1]

        for el in points[1:]:
            if el[0] > win_right:
                rlt, win_right = rlt + 1, el[1]
                continue
            win_right = min(win_right, el[1])
        return rlt + 1
'''


@dataclass(slots=True)
class Window:
    left: int
    right: int


class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()
        rlt = 0
        win = Window(left=points[0][0], right=points[0][1])
        for el in points[1:]:
            if el[0] <= win.right:  # intersection case
                win.left = max(win.left, el[0])  # This value don't used in logic
                win.right = min(win.right, el[1])  # This 'min' is important one - maybe points can be sorted by el[1]?
            else:
                rlt += 1
                win = Window(left=el[0], right=el[1])
        rlt += 1
        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([[10, 16], [2, 8], [1, 6], [7, 12]],), 2),
        ('test_01', ([[1, 2], [3, 4], [5, 6], [7, 8]],), 4),
        ('test_02', ([[1, 2], [2, 3], [3, 4], [4, 5]],), 2),
    ]

    foo = Solution()
    method2test = Solution.findMinArrowShots

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
