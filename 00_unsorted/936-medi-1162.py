# https://leetcode.com/problems/as-far-from-land-as-possible/description/
import time


class Solution:

    def _debug(self, grid):
        for row in grid:
            for el in row:
                print(el, end='')
            print()

    def maxDistance(self, grid: list[list[int]]) -> int:
        to_do: set[tuple[int, int]] = set()
        ntx_do: set[tuple[int, int]] = set()

        for idx in range(len(grid)):
            for jdx in range(len(grid[0])):
                if grid[idx][jdx] == 1:
                    to_do.add((idx, jdx))

        if len(to_do) == 0 or len(to_do) == len(grid) * len(grid[0]):
            return -1

        dist = -1
        while len(to_do) > 0:
            while len(to_do) > 0:
                idx, jdx = to_do.pop()
                grid[idx][jdx] = 8
                for n_idx, n_jdx in ((idx + 1, jdx), (idx - 1, jdx), (idx, jdx + 1), (idx, jdx - 1)):
                    if n_idx < 0 or n_idx >= len(grid) or n_jdx < 0 or n_jdx >= len(grid[0]):
                        continue
                    if (n_idx, n_jdx) in to_do or grid[n_idx][n_jdx] in (1, 8):
                        continue
                    ntx_do.add((n_idx, n_jdx))

            to_do, ntx_do = ntx_do, to_do
            dist += 1
        return dist


if __name__ == '__main__':
    tests = [
        ('test_00', ([[1, 0, 1], [0, 0, 0], [1, 0, 1]],), 2),
        ('test_01', ([[1, 0, 0], [0, 0, 0], [0, 0, 0]],), 4),
        ('test_02', ([[1,0,0,0,0,1,0,0,0,1],[1,1,0,1,1,1,0,1,1,0],[0,1,1,0,1,0,0,1,0,0],[1,0,1,0,1,0,0,0,0,0],[0,1,0,0,0,1,1,0,1,1],[0,0,1,0,0,1,0,1,0,1],[0,0,0,1,1,1,1,0,0,1],[0,1,0,0,1,0,0,1,0,0],[0,0,0,0,0,1,1,1,0,0],[1,1,0,1,1,1,1,1,0,0]],), 2),
    ]

    foo = Solution()
    method2test = Solution.maxDistance

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
