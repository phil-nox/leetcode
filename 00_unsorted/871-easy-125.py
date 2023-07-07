# https://leetcode.com/problems/valid-palindrome/description/
import time


class Solution:
    def isPalindrome(self, s: str) -> bool:
        vault: dict[int, int] = {idx: idx + 32 for idx in range(65, 91)}    # A-Z 2 a-z
        vault |= {idx: idx for idx in range(97, 123)}                       # a-z 2 a-z
        vault |= {idx: idx for idx in range(48, 58)}                        # 0-9 2 0-9  # was forgotten at first

        low, top = 0, len(s) - 1
        while low <= top:
            if ord(s[low]) not in vault:
                low += 1
                continue
            if ord(s[top]) not in vault:
                top -= 1
                continue

            if vault[ord(s[low])] != vault[ord(s[top])]:
                return False
            low, top = low + 1, top - 1

        return True


if __name__ == '__main__':
    tests = [
        ('test_00', ("A man, a plan, a canal: Panama",), True),
    ]

    foo = Solution()
    method2test = Solution.isPalindrome
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
