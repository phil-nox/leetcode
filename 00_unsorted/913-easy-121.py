# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
import time


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        rlt, low = 0, prices[0]     # int, int
        for el in prices[1:]:
            rlt = rlt if rlt > el - low else el - low
            low = low if low < el else el
        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([7, 1, 5, 3, 6, 4],), 5),
        ('test_01', ([7, 6, 4, 3, 1],), 0),
        ('test_02', ([7],), 0),
        ('test_03', ([7, 1],), 0),
        ('test_04', ([7, 8],), 1),
    ]

    foo = Solution()
    method2test = Solution.maxProfit

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
