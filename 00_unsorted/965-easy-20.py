# https://leetcode.com/problems/valid-parentheses/description/
import time


class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = list()
        for rune in s:
            if rune in '([{':
                stack.append(rune)
                continue
            if len(stack) == 0:
                return False
            check = (stack.pop(), rune)
            if check not in (('(', ')'), ('[', ']'), ('{', '}')):
                return False
        return len(stack) == 0


if __name__ == '__main__':
    tests = [
        ('test_00', ("()",), True),
        ('test_01', ("()[]{}",), True),
        ('test_02', ("(]",), False),
        ('test_03', ("(()",), False),
        ('test_04', (")",), False),
    ]

    foo = Solution()
    method2test = Solution.isValid   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
