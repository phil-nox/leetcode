# https://leetcode.com/problems/integer-to-roman/description/
# git commit -m "2023_08_31 - 851 - medi -   12"
import time


class Solution:
    def intToRoman(self, num: int) -> str:
        order_3: list[str] = ['', 'M', 'MM', 'MMM']
        order_2: list[str] = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        order_1: list[str] = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        order_0: list[str] = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

        return ''.join([
            order_3[num // 1000],
            order_2[num % 1000 // 100],
            order_1[num % 100 // 10],
            order_0[num % 10]
        ])
        

if __name__ == '__main__':
    tests = [
        ('test_00', (1994,), 'MCMXCIV'),
    ]

    foo = Solution()
    method2test = Solution.intToRoman
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
