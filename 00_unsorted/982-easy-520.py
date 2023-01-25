# https://leetcode.com/problems/detect-capital/description/
import time


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        first_is_cap = 64 < ord(word[0]) < 91
        count = 1 if first_is_cap else 0
        for el in word[1:]:
            cur_is_cap = 64 < ord(el) < 91
            if not first_is_cap and cur_is_cap:
                return False
            elif cur_is_cap:
                count += 1
        if not first_is_cap and count > 0:
            return False
        if first_is_cap and count not in (1, len(word)):
            return False
        return True


if __name__ == '__main__':
    tests = [
        ('test_00', ("USA",), True),
        ('test_01', ("FlaG",), False),
    ]

    foo = Solution()
    method2test = Solution.detectCapitalUse         # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)

