# https://leetcode.com/problems/minimum-score-by-changing-two-elements/description/
import time
import heapq


class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        mins: list[int] = []
        maxs: list[int] = []
        for el in nums:
            if len(mins) < 3:
                heapq.heappush(mins, -el)
                heapq.heappush(maxs, el)
                continue
            if -el > mins[0]:
                heapq.heappop(mins)
                heapq.heappush(mins, -el)
            if el > maxs[0]:
                heapq.heappop(maxs)
                heapq.heappush(maxs, el)

        min2, min1, min0 = -heapq.heappop(mins), -heapq.heappop(mins), -heapq.heappop(mins)
        max0, max1, max2 = heapq.heappop(maxs), heapq.heappop(maxs), heapq.heappop(maxs)
        return min(max2 - min2, max0 - min0, max1 - min1)


if __name__ == '__main__':
    tests = [
        ('test_00', ([1, 4, 3],), 0),
        ('test_01', ([1, 4, 7, 8, 5],), 3),
        ('test_02', ([59, 27, 9, 81, 33],), 24),
        ('test_03', ([58, 42, 8, 75, 28],), 30),
    ]

    foo = Solution()
    method2test = Solution.minimizeSum

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
