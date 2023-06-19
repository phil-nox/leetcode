# https://leetcode.com/problems/find-the-highest-altitude/description/
# 00 : 01 : 45
import time


class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        top = cur = 0
        for el in gain:
            cur += el
            top = cur if cur > top else top
        return top
        

if __name__ == '__main__':
    tests = [
        ('test_00', (__test_args__), 2),
    ]

    foo = Solution()
    method2test = Solution.largestAltitude
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
