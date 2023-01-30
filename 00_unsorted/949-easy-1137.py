# https://leetcode.com/problems/n-th-tribonacci-number/description/
import time


class Solution:
    def tribonacci(self, n: int) -> int:
        idx, vault, rlt = 0, [0, 0, 1], n
        while (n := n - 1) > 0:
            rlt = sum(vault)
            vault[idx], idx = (rlt, idx + 1) if idx < 2 else (rlt, 0)
        return rlt
        

if __name__ == '__main__':
    tests = [
        ('test_00', (4,), 4),
        ('test_01', (25,), 1389537),
        ('test_02', (37, ), 2082876103)
    ]

    foo = Solution()
    method2test = Solution.tribonacci

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
