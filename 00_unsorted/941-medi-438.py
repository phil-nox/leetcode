# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
import time


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        win: dict[str, int] = dict()
        for el in p:
            win[el] = win.get(el, 0) - 1
        for el in s[:len(p)]:
            win[el] = win.get(el, 0) + 1
        rlt = [0] if all(el == 0 for el in win.values()) else []
        for idx in range(len(p), len(s)):
            old, nxt = s[idx - len(p)], s[idx]
            win[old] = win.get(old, 0) - 1
            win[nxt] = win.get(nxt, 0) + 1
            if all(el == 0 for el in win.values()):
                rlt.append(idx + 1 - len(p))
        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ("cbaebabacd", "abc"), [0, 6]),
        ('test_01', ("abab", "ab"), [0, 1, 2]),
    ]

    foo = Solution()
    method2test = Solution.findAnagrams

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
