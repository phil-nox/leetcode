# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# git commit -m "2023_09_04 - 842 - medi -   17"
import time


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        vault: dict[str, str] = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        rlt: list[str] = []
        stack: list[str] = [el for el in reversed(vault[digits[0]])] if digits else []
        while stack:
            cur = stack.pop()
            if len(cur) == len(digits):
                rlt.append(cur)
                continue
            for el in reversed(vault[digits[len(cur)]]):
                stack.append(cur + el)

        return rlt
        

if __name__ == '__main__':
    tests = [
        ('test_00', ('23',), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    ]

    foo = Solution()
    method2test = Solution.letterCombinations
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
