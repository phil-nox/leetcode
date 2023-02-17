# https://leetcode.com/problems/palindrome-number/description/
import time


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 1:
            return False if x < 0 else True
        order_r, order_l = 10**10, 1    # int32  #-2**31 <= x <= 2**31 - 1 # 2147483648 # 10**10
        while x // order_r == 0:
            order_r = order_r // 10
        while order_r > order_l:
            if (x // order_r) % 10 != (x // order_l) % 10:
                return False
            order_r, order_l = order_r // 10, order_l * 10
        return True


if __name__ == '__main__':
    tests = [
        ('test_00', (121,), True),
        ('test_01', (-121,), False),
        ('test_02', (10,), False),
        ('test_03', (1,), True),
        ('test_04', (111,), True),
        ('test_05', (1001,), True),
        ('test_06', (1701,), False),
        ('test_07', (0,), True),
    ]

    foo = Solution()
    method2test = Solution.isPalindrome

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
