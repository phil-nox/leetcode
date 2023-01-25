# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/description/
import time
from typing import List
import heapq


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        rlt = 0
        bags2fill = []
        for bag_cap, bag_rock in zip(capacity, rocks):
            if bag_cap > bag_rock:
                heapq.heappush(bags2fill, bag_cap - bag_rock)
            else:
                rlt += 1

        while additionalRocks > 0 and len(bags2fill) > 0:
            additionalRocks -= heapq.heappop(bags2fill)
            if additionalRocks > -1:
                rlt += 1

        return rlt


if __name__ == '__main__':
    foo = Solution()
    time_diff = -time.perf_counter()
    for name, inpt, outpt in [
        ('test_00', ([2,3,4,5], [1,2,4,4], 2), 3),
        ('test_01', ([10,2,2], [2,2,0], 100), 3),
    ]:
        if name == 'test_0':
            print(foo.maximumBags(*inpt))
            quit()
        assert foo.maximumBags(*inpt) == outpt, print('👉', name, foo.maximumBags(*inpt), 'vs', outpt)
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
