# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
import time

'''
check the_value costs O(N)
number of days as a response are sorted - binary search can by apply - O(logN)
so to find answer costs O(NlogN)
'''


class Solution:
    def _number_of_day(self, weights: list[int], capacity: int) -> int:
        rlt, cur = 1, 0
        for el in weights:
            if el > capacity:
                return 100000           # 1 <= days <= 5 * 10^4 < 100000
            rlt, cur = (rlt + 1, el) if cur + el > capacity else (rlt, cur + el)
        return rlt

    def shipWithinDays(self, weights: list[int], days: int) -> int:
        idx, jdx, mem = 1, 25000001, -1       # 500 * 5 * 10^4 = 25000000
        while (mid := (jdx - idx) // 2 + idx) != mem:
            idx, jdx, mem = (mid, jdx, mid) if self._number_of_day(weights, mid) > days else (idx, mid, mid)
        return jdx


if __name__ == '__main__':
    tests = [
        ('test_00', ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 15),
        ('test_01', ([3, 2, 2, 4, 1, 4], 3), 6),
        ('test_02', ([1, 2, 3, 1, 1], 4), 3),
        ('test_03', ([10], 1), 10),
        ('test_03', ([25000000], 1), 25000000),
        ('test_03', ([25000001], 1), 25000001),
        ('test_03', ([25000002], 1), 25000001),
    ]

    foo = Solution()
    method2test = Solution.shipWithinDays

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
