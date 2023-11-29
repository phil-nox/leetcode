# https://leetcode.com/problems/plates-between-candles/description/
import time


class Solution:

    @staticmethod
    def setup(s: str, left_s: list[int], righ_s: list[int], cand_s: list[int]) -> None:
        idx = count = 0
        last_candle = -1

        while idx < len(s) and s[idx] == '*':
            idx += 1
        last_candle = idx

        while idx < len(s):
            if s[idx] == '*':
                left_s[idx] = last_candle
                count += 1
            else:
                last_candle = left_s[idx] = idx
                cand_s[idx] = count
            idx += 1

        last_candle = -1
        while (idx := idx - 1) > -1:
            if s[idx] == '*':
                righ_s[idx] = last_candle
            else:
                last_candle = righ_s[idx] = idx
        return

    @staticmethod
    def get_value(query: list[int], left_s: list[int], righ_s: list[int], cand_s: list[int]) -> int:
        bot, top = query
        if righ_s[bot] > left_s[top] or righ_s[bot] == -1 or left_s[top] == -1:
            return 0
        return cand_s[left_s[top]] - cand_s[righ_s[bot]]

    def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
        left_s = [-1] * len(s)
        righ_s = [-1] * len(s)
        cand_s = [0] * len(s)
        rlt = []

        self.setup(s, left_s, righ_s, cand_s)
        for el in queries:
            rlt.append(self.get_value(el, left_s, righ_s, cand_s))

        return rlt
        

if __name__ == '__main__':
    tests = [
        ('test_00', ('**|**|***|', [[2,5],[5,9]]), [2,3]),
    ]

    foo = Solution()
    method2test = Solution.platesBetweenCandles
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
