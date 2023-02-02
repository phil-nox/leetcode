# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
import time


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        small, big = (str1, str2) if len(str1) < len(str2) else (str2, str1)
        while True:
            if not big.startswith(small):
                return ''
            if (rest := big[len(small):]) == '':
                break
            small, big = (rest, small) if len(rest) < len(small) else (small, rest)

        while big != '':
            if not big.startswith(small):
                return ''
            big = big[len(small):]
        return small


if __name__ == '__main__':
    tests = [
        ('test_00', ("ABCABC", "ABC"), "ABC"),
        ('test_01', ("ABABAB", "ABAB"), "AB"),
        ('test_02', ("LEET", "CODE"), ""),
        ('test_04', ("ABABABAB", "ABAB"), "ABAB"),
        ('test_05', ("ABABAD", "ABAB"), ""),
    ]

    foo = Solution()
    method2test = Solution.gcdOfStrings

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
