# https://leetcode.com/problems/categorize-box-according-to-criteria/description/
import time


class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        heavy = False if mass < 100 else True
        bulky = any([el >= 10000 for el in [length, width, height]])
        bulky = True if bulky else length*width*height >= 10**9
        if heavy and bulky:
            return "Both"
        if not heavy and not bulky:
            return "Neither"
        return "Bulky" if bulky else "Heavy"


if __name__ == '__main__':
    tests = [
        ('test_00', (1000, 35, 700, 300), "Heavy"),
        ('test_01', (200, 50, 800, 50), "Neither"),
    ]

    foo = Solution()
    method2test = Solution.categorizeBox   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
