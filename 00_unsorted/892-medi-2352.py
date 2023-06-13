# https://leetcode.com/problems/equal-row-and-column-pairs/description/
# 00 : 06 : 49
import time


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        rlt: int = 0
        row_s: dict[tuple[int, ...], int] = dict()  # tuple2count
        for row in grid:
            cur_row = tuple(row)
            count = row_s.get(cur_row, 0) + 1
            row_s[cur_row] = count
        for col_idx in range(len(grid)):
            cur_col = tuple([row[col_idx] for row in grid])
            rlt += row_s.get(cur_col, 0)
        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([[3, 2, 1], [1, 7, 6], [2, 7, 7]],), 1),
        ('test_01', ([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]],), 3),
    ]

    foo = Solution()
    method2test = Solution.equalPairs

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
