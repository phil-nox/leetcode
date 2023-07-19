# https://leetcode.com/problems/non-overlapping-intervals/description/
# git commit -m "2023_07_19 - 854 - medi -  435"
import time


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda el: el[1])
        # [print(el) for el in intervals]

        rlt, lim = 0, -10**5
        for st, en in intervals:    # start, end
            if st >= lim:               # no intersection
                lim = en
                continue
            rlt += 1                    # intersection remove interval with st, en

        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([[1, 2], [2, 3], [3, 4], [1, 3]],), 1),
        ('test_00', ([[0, 2], [1, 3], [1, 3], [2, 4], [3, 5], [3, 5], [4, 6]],), 4),
    ]

    foo = Solution()
    method2test = Solution.eraseOverlapIntervals
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
