# https://leetcode.com/problems/permutation-in-string/description/
import time


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        window = dict()
        for el in s1:
            window[el] = window.get(el, 0) - 1
        for el in s2[:len(s1)]:
            window[el] = window.get(el, 0) + 1
        if all(item == 0 for item in window.values()):
            return True

        for idx in range(len(s1), len(s2)):
            old, nxt = s2[idx-len(s1)], s2[idx]
            window[nxt] = window.get(nxt, 0) + 1
            window[old] = window.get(old, 0) - 1
            if all(item == 0 for item in window.values()):
                return True

        return False


if __name__ == '__main__':
    tests = [
        ('test_00', ("ab", "eidbaooo"), True),
        ('test_01', ("ab", "eidboaoo"), False),
        ('test_77', ("adc", "dcda"), True),
        ('test_83', ("abcdxabcde", "abcdeabcdx"), True),
    ]

    foo = Solution()
    method2test = Solution.checkInclusion

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
