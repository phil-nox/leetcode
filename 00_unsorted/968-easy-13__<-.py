# https://leetcode.com/problems/roman-to-integer/description/
import time


class Solution:
    def romanToInt(self, s: str) -> int:
        single = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        double = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        rlt, idx = 0, -1
        while (idx := idx + 1) < len(s):
            if s[idx] in 'IXC' and idx + 1 < len(s) and s[idx:idx+2] in double:
                rlt += double[s[idx:idx+2]]
                idx += 1
                continue
            rlt += single[s[idx]]
        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ("III",), 3),
        ('test_01', ("LVIII",), 58),
        ('test_02', ("MCMXCIV",), 1994),
        ('test_03', ("MIV",), 1004),
        ('test_03', ("MX",), 1010),
    ]

    foo = Solution()
    method2test = Solution.romanToInt   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
