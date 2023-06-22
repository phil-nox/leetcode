# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
# 00 : 23 : 26
import time


class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        empty, hold = 0, -10**5
        for el in prices:
            empty, hold = max(empty, hold + el), max(hold, empty - el - fee)
        return max(empty, hold)
        

if __name__ == '__main__':
    tests = [
        ('test_00', ([1, 3, 2, 8, 4, 9], 2), 8),
    ]

    foo = Solution()
    method2test = Solution.maxProfit
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
