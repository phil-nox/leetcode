# https://leetcode.com/problems/maximum-ice-cream-bars/description/
import time


class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        rlt = 0
        costs.sort()
        for el in costs:
            coins -= el
            if coins < 0:
                return rlt
            rlt += 1
        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([1, 3, 2, 4, 1], 7), 4),
        ('test_01', ([10, 6, 8, 7, 7, 8], 5), 0),
        ('test_02', ([1, 6, 3, 1, 2, 5], 20), 6),

    ]

    foo = Solution()
    method2test = Solution.maxIceCream   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)

