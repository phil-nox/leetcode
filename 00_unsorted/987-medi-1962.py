# https://leetcode.com/problems/remove-stones-to-minimize-the-total/description/
import time
from typing import List
import heapq


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        vault = []
        for el in piles:
            heapq.heappush(vault, -el)

        for idx in range(k):
            el = heapq.heappop(vault)
            heapq.heappush(vault, el // 2)
        return -sum(vault)


if __name__ == '__main__':
    foo = Solution()
    time_diff = -time.perf_counter()
    method2test = Solution.minStoneSum                                          # name_of_the_method
    for name, inpt, outpt in [
        ('test_00', ([5, 4, 9], 2), 12),                      # test_case_from_leetcode
        ('test_01', ([4, 3, 6, 7], 3), 12),
        ('test_02', ([1], 100000), 1),
    ]:
        if name == 'test_0':
            print(method2test(foo, *inpt))
            quit()
        assert method2test(foo, *inpt) == outpt, print('👉', name, method2test(foo, *inpt), 'vs', outpt)
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)