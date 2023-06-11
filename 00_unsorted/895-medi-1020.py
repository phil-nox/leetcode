# https://leetcode.com/problems/number-of-enclaves/description/
import time


class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        seen: set[tuple[int, int]] = set()
        at_work: set[tuple[int, int]] = set()
        count: int = 0
        no_path: bool = True
        rlt: int = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) in seen:
                    continue
                if grid[row][col] == 0:
                    continue
                at_work.clear()
                at_work.add((row, col))
                count = 0
                no_path = True

                while at_work:
                    cur_r, cur_c = at_work.pop()
                    if (cur_r, cur_c) in seen:
                        continue
                    if grid[cur_r][cur_c] == 0:
                        continue
                    count += 1
                    seen.add((cur_r, cur_c))
                    for nxt_r, nxt_c in (
                            (cur_r - 1, cur_c),
                            (cur_r, cur_c - 1),
                            (cur_r + 1, cur_c),
                            (cur_r, cur_c + 1),
                    ):
                        if nxt_r in (-1, len(grid)) or nxt_c in (-1, len(grid[0])):
                            no_path = False
                            continue
                        if (nxt_r, nxt_c) in seen:
                            continue
                        at_work.add((nxt_r, nxt_c))
                rlt += count if no_path else 0

        return rlt
        

if __name__ == '__main__':
    tests = [
        ('test_00', ([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]],), 0),
    ]

    foo = Solution()
    method2test = Solution.numEnclaves

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
