# https://leetcode.com/problems/string-to-integer-atoi/description/
import time


class Solution:
    def myAtoi(self, s: str) -> int:
        positive: bool = True
        rlt: int = 0

        # parsing
        idx: int = 0
        jdx: int = 0
        while idx < len(s) and s[idx] == ' ':
            idx += 1
        if idx < len(s) and s[idx] in ('-', '+'):
            positive = True if s[idx] == '+' else False
            idx += 1
        while idx < len(s) and s[idx] == '0':
            idx += 1
        while idx + jdx < len(s) and s[idx + jdx] in '0123456789':
            jdx += 1

        # to_int32
        if jdx > 10:    # 2147483647 or -2147483648
            return 2147483647 if positive else -2147483648

        jdx, power = jdx - 1, 1
        while jdx > -1 and power < 10**9:
            rlt += (ord(s[idx + jdx]) - 48) * power
            jdx, power = jdx - 1, power * 10

        if jdx > -1:    # power == 10**10
            if s[idx + jdx] not in '12' or (s[idx + jdx] == '2' and rlt > 147483647):
                return 2147483647 if positive else -2147483648
            rlt += (ord(s[idx + jdx]) - 48) * power
        return rlt if positive else -rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ('42',), 42),
        ('test_01', ('   -42',), -42),
        ('test_02', ('4193 with words',), 4193),
        ('test_03', ('0032',), 32),
        ('test_04', ('-0032',), -32),
        ('test_05', ('-2147483647',), -2147483647),
        ('test_06', ('-2147483648',), -2147483648),
        ('test_07', ('-2147483649',), -2147483648),
        ('test_08', ('-12147483649',), -2147483648),
        ('test_09', ('2147483646',), 2147483646),
        ('test_09', ('2147483647',), 2147483647),
        ('test_09', ('2147483648',), 2147483647),
        ('test_09', ('2147483649',), 2147483647),
        ('test_09', ('12147483646',), 2147483647),
        ('test_09', ('',), 0),
    ]

    foo = Solution()
    method2test = Solution.myAtoi

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
