# https://leetcode.com/problems/number-of-closed-islands/description/
import time


class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        seen: set[tuple[int, int]] = set()
        island: set[tuple[int, int]] = set()
        rlt: int = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) in seen:
                    continue
                if grid[row][col] == 1:
                    continue
                island.clear()
                island.add((row, col))
                is_closed = 1
                while island:
                    r, c = island.pop()     # current row & col
                    seen.add((r, c))
                    for n_r, n_c in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                        if n_r in (-1, len(grid)) or n_c in (-1, len(grid[0])):
                            is_closed = 0
                            continue
                        if grid[n_r][n_c] == 1:
                            continue
                        if (n_r, n_c) not in seen:
                            island.add((n_r, n_c))
                rlt += is_closed
        return rlt
        

if __name__ == '__main__':
    tests = [
        ('test_00', (
        [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 0]],), 2),
    ]

    foo = Solution()
    method2test = Solution.closedIsland

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
