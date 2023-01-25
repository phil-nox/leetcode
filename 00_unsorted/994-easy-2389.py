# https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/
import time
from typing import List
import heapq


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        q_heap, n_heap = list(), list()
        total = 0
        rlt = [0] * len(queries)

        for el in nums:
            heapq.heappush(n_heap, -el)
            total -= el

        for idx, el in enumerate(queries):
            heapq.heappush(q_heap, (-el, idx))

        val_to_set = len(nums)
        while len(q_heap) > 0 and len(n_heap) > 0:
            q_val, q_idx = heapq.heappop(q_heap)

            diff = 0
            while len(n_heap) > -1:
                total -= diff
                if total >= q_val:
                    rlt[q_idx] = val_to_set
                    break
                diff = heapq.heappop(n_heap)
                val_to_set -= 1

        return rlt


if __name__ == '__main__':
    foo = Solution()
    time_diff = -time.perf_counter()
    for name, inpt, outpt in [
        ('test_00', ([4, 5, 2, 1], [3, 10, 21]), [2, 3, 4]),
        ('test_01', ([2, 3, 4, 5], [1]), [0]),
    ]:
        if name == 'test_0':
            print(foo.answerQueries(*inpt))
            quit()
        assert foo.answerQueries(*inpt) == outpt, print('👉', name, foo.answerQueries(*inpt), 'vs', outpt)
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
