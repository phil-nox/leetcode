# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
import time


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx = -1
        while (idx := idx + 1) < len(haystack) - len(needle) + 1:
            jdx = 0
            while jdx < len(needle) and haystack[idx + jdx] == needle[jdx]:
                jdx += 1
            if jdx == len(needle):
                return idx
        return -1
    

if __name__ == '__main__':
    tests = [
        ('test_00', ("sadbutsad", "sad"), 0),
        ('test_01', ("leetcode", "leeto"), -1),
        ('test_02', ("leetcode", "tco"), 3),
        ('test_03', ("aaa", "aaaa"), -1),
        ('test_04', ("a", "a"), 0),
    ]

    foo = Solution()
    method2test = Solution.strStr

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
