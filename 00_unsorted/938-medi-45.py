# https://leetcode.com/problems/jump-game-ii/description/
import time
from dataclasses import dataclass
import heapq


@dataclass(slots=True)
class Path:
    idx: int
    move: int
    jump: int

    def __lt__(self, other: 'Path'):
        return self.idx + self.move > other.idx + other.move      # opposite for heapq

    def process(self, nums: list[int]) -> list['Path']:
        rlt = []
        for jdx in range(1, self.move + 1):
            if self.idx+jdx >= len(nums):
                continue
            rlt.append(Path(idx=self.idx+jdx, move=nums[self.idx+jdx], jump=self.jump+1))
        return rlt


class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        dijkstra = [Path(idx=0, move=nums[0], jump=0)]

        while len(dijkstra) > 0:
            cur = heapq.heappop(dijkstra)
            for el in cur.process(nums):
                if el.idx == len(nums) - 1:
                    return el.jump
                heapq.heappush(dijkstra, el)
        return -1   # should never happen


if __name__ == '__main__':
    tests = [
        ('test_00', ([2, 3, 1, 1, 4],), 2),
        ('test_01', ([2, 3, 0, 1, 4],), 2),
        ('test_02', ([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0],), 3),
    ]

    foo = Solution()
    method2test = Solution.jump

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
