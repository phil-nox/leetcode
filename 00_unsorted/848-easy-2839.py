# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/description/
# git commit -m "2023_09_02 - 848 - easy - 2839"
import time


class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return {s1[0], s1[2]} == {s2[0], s2[2]} and {s1[1], s1[3]} == {s2[1], s2[3]}
        

if __name__ == '__main__':
    tests = [
        ('test_00', ('abcd', 'cdab'), True),
    ]

    foo = Solution()
    method2test = Solution.canBeEqual
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
