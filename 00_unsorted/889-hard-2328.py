# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/description/
# 00 : 38 : 33
import time


class Solution:

    def _dfs(self, row, col, grid, score_s):
        if score_s[row][col] != 0:
            return

        stack = [(row, col, False)]  # row, col, backward_walk
        last_val = 0
        while stack:
            row, col, backward = stack.pop()
            if backward is False and score_s[row][col] != 0:                # short cut (node is already dfs)
                last_val = score_s[row][col]
            elif backward is False:                                         # forward walk
                last_val = score_s[row][col]
                for n_r, n_c in ((row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)):
                    if -1 < n_r < len(grid) and -1 < n_c < len(grid[0]) and grid[row][col] < grid[n_r][n_c]:
                        stack.append((row, col, True))
                        stack.append((n_r, n_c, False))
            else:                                                           # backward walk
                score_s[row][col] += last_val + 1
                last_val = score_s[row][col]

    def countPaths(self, grid: list[list[int]]) -> int:
        rlt: int = len(grid) * len(grid[0])

        score_s = []
        for _ in range(len(grid)):
            score_s.append([0] * len(grid[0]))

        for r_idx in range(len(grid)):
            for c_idx in range(len(grid[0])):
                self._dfs(r_idx, c_idx, grid, score_s)

        for row in score_s:
            rlt += sum(row)

        return rlt % (10**9 + 7)


if __name__ == '__main__':
    tests = [
        ('test_00', ([[1, 1], [3, 4]],), 8),
        ('test_02', ([[1, 1, 1], [3, 4, 5], [1, 7, 8]],), 41),
        ('test_01', ([[1], [2]],), 3),
        ('test_15', ([[1,1,1],[1,1,1],[1,1,1]],), 9),
        ('test_03', ([[12469,18741,68716,30594,65029,44019,92944,84784,92781,5655,43120,81333,54113,88220,23446,6129,2904,48677,20506,79604,82841,3938,46511,60870,10825,31759,78612,19776,43160,86915,74498,38366,28228,23687,40729,42613,61154,22726,51028,45603,53586,44657,97573,61067,27187,4619,6135,24668,69634,24564,30255,51939,67573,87012,4106,76312,28737,7704,35798]],), 148),
        ('test_04', ([[73884,15322,92124,16515,54702,88526,61879,14125,21161,42701,35686,75932,8696],[59537,80396,65708,32310,46753,39759,4746,71413,84723,13233,23640,62230,11825],[6414,96122,64501,32523,55259,2935,44772,48912,26516,56256,69201,21079,52979],[50951,1748,42645,73435,81511,21445,26066,27605,40388,43702,47233,15333,86291],[87914,90237,95947,97341,93670,79822,32591,44096,55112,89104,36097,82759,15504],[3604,74013,74414,68295,58798,7050,71657,33463,38040,46180,61730,82754,57179],[86867,1972,13704,11581,99042,24825,77747,38671,40628,38626,54719,7366,36309],[69272,98273,16474,15204,40263,99956,36072,68173,77076,18094,97439,61968,7435],[95263,39616,37983,61376,256,7169,45149,94957,66151,13256,37776,25331,29659],[90001,12571,31093,46714,52347,44882,76055,53662,69928,37486,44020,2211,67466]],), 925),
    ]

    foo = Solution()
    method2test = Solution.countPaths
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
