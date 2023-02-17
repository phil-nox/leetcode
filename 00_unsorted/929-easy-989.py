# https://leetcode.com/problems/add-to-array-form-of-integer/description/
import time


class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        rlt, idx, rest = [], len(num) - 1, 0
        while idx > -1 or k > 0 or rest != 0:
            val_a, idx = (num[idx], idx - 1) if idx > -1 else (0, -1)
            val_b, k = (k % 10, k // 10) if k > 0 else (0, 0)
            rest, cur = divmod(val_a + val_b + rest, 10)
            rlt.append(cur)
        return rlt[::-1]


if __name__ == '__main__':
    tests = [
        ('test_00', ([1, 2, 0, 0], 34), [1, 2, 3, 4]),
        ('test_01', ([2, 7, 4], 181), [4, 5, 5]),
        ('test_02', ([2, 1, 5], 806), [1, 0, 2, 1]),
        ('test_03', ([0], 0), [0]),
        ('test_03', ([1], 0), [1]),
        ('test_03', ([0], 1), [1]),
        ('test_04', ([9, 9, 9], 1), [1, 0, 0, 0]),
    ]

    foo = Solution()
    method2test = Solution.addToArrayForm

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
