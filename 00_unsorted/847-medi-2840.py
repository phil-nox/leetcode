# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/description/
# git commit -m "2023_09_02 - 847 - medi - 2840"
import time
import collections


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if collections.Counter(s1[::2]) != collections.Counter(s2[::2]):
            return False
        if collections.Counter(s1[1::2]) != collections.Counter(s2[1::2]):
            return False
        return True
        

if __name__ == '__main__':
    tests = [
        ('test_00', ('abcdba', 'cabdab'), True),
    ]

    foo = Solution()
    method2test = Solution.checkStrings
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
