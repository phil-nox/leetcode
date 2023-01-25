# https://leetcode.com/problems/minimum-falling-path-sum/description/
import time
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        nxt_row = [0] * len(matrix)
        pre_row = matrix[0]
        for row in matrix[1:]:
            for idx, el in enumerate(row):
                if idx == 0:
                    tmp = (el + pre_row[idx], el + pre_row[idx + 1])
                elif idx == len(matrix) - 1:
                    tmp = (el + pre_row[idx], el + pre_row[idx - 1])
                else:
                    tmp = (el + pre_row[idx - 1], el + pre_row[idx], el + pre_row[idx + 1])
                nxt_row[idx] = min(tmp)
            pre_row, nxt_row = nxt_row, pre_row
        return min(pre_row)


if __name__ == '__main__':
    foo = Solution()
    time_diff = -time.perf_counter()
    for name, inpt, outpt in [
        ('test_00', ([[2, 1, 3], [6, 5, 4], [7, 8, 9]],), 13),
        ('test_01', ([[-19, 57], [-40, -5]],), -59),
        ('test_02', ([[4]],), 4),
    ]:
        if name == 'test_0':
            print(foo.minFallingPathSum(*inpt))
            quit()
        assert foo.minFallingPathSum(*inpt) == outpt, print('👉', name, foo.minFallingPathSum(*inpt), 'vs', outpt)
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
