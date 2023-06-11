# https://leetcode.com/problems/ipo/description/
import time
import heapq

'''
        cap2prof: list[tuple[int, int]] = []         # capital, profits
        max_prof: list[int] = []                     # max profit for current capital

        for c, p in zip(capital, profits):
            heapq.heappush(cap2prof, (c, p))

        while len(cap2prof) > 0 and w >= cap2prof[0][0]:
            _, prj_prof = heapq.heappop(cap2prof)
            heapq.heappush(max_prof, -prj_prof)

        while (k := k - 1) > -1 and len(max_prof):
            w -= heapq.heappop(max_prof)
            while len(cap2prof) > 0 and w >= cap2prof[0][0]:
                _, prj_prof = heapq.heappop(cap2prof)
                heapq.heappush(max_prof, -prj_prof)
        return w
'''


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        cap2prof: list[tuple[int, int]] = sorted(zip(capital, profits), reverse=True)
        max_prof: list[int] = [-w]                      # max_profit for current_capital    a_kind_of_init
        w, k = 0, k + 1                                 # because of max_prof = [-w]        a_kind_of_init

        while (k := k - 1) > -1 and max_prof:
            w -= heapq.heappop(max_prof)
            while cap2prof and w >= cap2prof[-1][0]:
                heapq.heappush(max_prof, -cap2prof.pop()[1])
        return w


if __name__ == '__main__':
    tests = [
        ('test_00', (2, 0, [1, 2, 3], [0, 1, 1]), 4),
        ('test_00', (3, 0, [1, 2, 3], [0, 1, 2]), 6),
    ]

    foo = Solution()
    method2test = Solution.findMaximizedCapital

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
