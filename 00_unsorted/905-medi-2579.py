# https://leetcode.com/problems/count-total-number-of-colored-cells/description/
import time


class Solution:
    def coloredCells(self, n: int) -> int:
        rlt = 1
        for idx in range(1, n):
            rlt += idx * 4
        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', (1,), 1),
        ('test_00', (2,), 5),
        ('test_00', (3,), 13),
    ]

    foo = Solution()
    method2test = Solution.coloredCells

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
