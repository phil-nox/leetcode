# https://leetcode.com/problems/reverse-integer/description/
import time

''' With_array
class Solution:
    # -2**31     -> -2.147.483.648
    #  2**31 - 1 ->  2.147.483.647  -reverse-> 7.463.847.412 not_possible
    def reverse(self, x: int) -> int:
        if x == 0 or x == -2147483648:  # -2**31 can be reverse to positive
            return 0
        neg, x, tmp = (False, x, []) if x > 0 else (True, -x, [])
        while x != 0:
            x, rest = divmod(x, 10)
            tmp.append(rest)

        rlt = tmp[0]
        for el in tmp[1:9]:
            rlt = rlt * 10 + el

        if len(tmp) < 10:
            return -rlt if neg else rlt
        if rlt > 214748364:     # 214748364_
            return 0
        rlt = rlt * 10 + tmp[9]
        return -rlt if neg else rlt
'''


class Solution:
    # -2**31     -> -2147483648
    #  2**31 - 1 ->  2.147.483.647  -reverse-> 7.463.847.412 not_possible
    def reverse(self, x: int) -> int:
        if x == 0 or x == -2147483648:                              # -2**31 can be reverse to positive
            return 0
        neg, x, count = (False, x, 1) if x > 0 else (True, -x, 1)
        x, rlt = divmod(x, 10)
        while x != 0 and count != 9:
            x, el = divmod(x, 10)
            rlt, count = rlt * 10 + el, count + 1
        if count == 9 and x != 0:
            if rlt > 214748364:                                     # 214748364_
                return 0
            rlt = rlt * 10 + x
        return -rlt if neg else rlt


if __name__ == '__main__':
    tests = [
        ('test_00', (123,), 321),
        ('test_01', (-123,), -321),
        ('test_02', (120,), 21),
        ('test_03', (1000000000,), 1),
        ('test_04', (1987654321,), 1234567891),
        ('test_05', (1000000001,), 1000000001),
        ('test_06', (1000000002,), 2000000001),
        ('test_07', (1000000009,), 0),
        ('test_08', (1000000013,), 0),
        ('test_09', (1000000012,), 2100000001),
        ('test_10', (463847412,), 214748364),
        ('test_11', (1534236469,), 0),

    ]

    foo = Solution()
    method2test = Solution.reverse

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
