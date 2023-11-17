# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description/
import time
import heapq


class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        rlt = 0
        events.sort(key=lambda x: x[0], reverse=True)
        cur_day = events[-1][0]
        queue = []

        while events or queue:

            cur_day = cur_day + 1 if queue else events[-1][0]

            while events and events[-1][0] == cur_day:
                heapq.heappush(queue, (events.pop()[1]))

            heapq.heappop(queue)
            rlt += 1

            while queue and queue[0] == cur_day:
                heapq.heappop(queue)

        return rlt
        

if __name__ == '__main__':
    tests = [
        ('test_00', ([[1, 2], [2, 3], [3, 4]],), 3),
    ]

    foo = Solution()
    method2test = Solution.maxEvents
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
