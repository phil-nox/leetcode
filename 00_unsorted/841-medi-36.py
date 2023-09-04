# https://leetcode.com/problems/valid-sudoku/description/
# git commit -m "2023_09_04 - 841 - medi -   36"
import time


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        vault, old_len = set(), 0

        for l_idx in range(9):
            for c_idx in range(9):
                val = board[l_idx][c_idx]
                if val == '.':
                    continue

                vault.add((l_idx, -1, val))
                vault.add((-1, c_idx, val))
                vault.add((l_idx // 3, c_idx // 3, val))

                if len(vault) != old_len + 3:
                    return False
                old_len = len(vault)
        return True


''' # first_try
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_l = [set() for _ in range(9)]
        check_c = [set() for _ in range(9)]
        check_b = [set() for _ in range(9)]

        for l_idx in range(9):
            for c_idx in range(9):
                val = board[l_idx][c_idx]
                if val == '.':
                    continue

                b_idx = 3 * (l_idx // 3) + c_idx // 3
                if val in check_l[l_idx] or val in check_c[c_idx] or val in check_b[b_idx]:
                    return False

                check_l[l_idx].add(val)
                check_c[c_idx].add(val)
                check_b[b_idx].add(val)

        return True
'''


if __name__ == '__main__':
    tests = [
        ('test_00', (), 2),
    ]

    foo = Solution()
    method2test = Solution.isValidSudoku
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
