# https://leetcode.com/problems/total-cost-to-hire-k-workers/description/
# 00 : 25 : 48
import time
import heapq


class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        #  [0123456]_7 - 2         * 2 - 3 = 0   # one element no used
        if len(costs) - candidates * 2 - k < 0:  # intersection case
            return sum(sorted(costs)[:k])

        rlt: int = 0
        vault: list[tuple[int, int]] = []  # (cost, idx)
        low, top = candidates - 1, len(costs) - candidates

        for idx in range(low + 1):
            heapq.heappush(vault, (costs[idx], idx))
        for idx in range(top, len(costs)):
            heapq.heappush(vault, (costs[idx], idx))

        for _ in range(k):
            cst, idx = heapq.heappop(vault)
            rlt += cst
            to_do, low, top = (top - 1, low, top - 1) if idx >= top else (low + 1, low + 1, top)
            heapq.heappush(vault, (costs[to_do], to_do))
        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([1, 2, 4, 1], 3, 3), 4),
    ]

    foo = Solution()
    method2test = Solution.totalCost
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
