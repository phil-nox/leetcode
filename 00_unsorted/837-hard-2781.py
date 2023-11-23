# https://leetcode.com/problems/length-of-the-longest-valid-substring/description/
import time

'''
class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        bad = set(forbidden)
        seen = set()
        rlt, left = 0, -1

        for idx in range(len(word)):

            if idx - left > 10 and word[idx - 9 : idx + 1] in seen:
                rlt = max(rlt, idx - left)
                continue

            for low in range(idx, max(idx - 10, left), -1):
                if word[low : idx + 1] in forbidden:
                    left = low
                    break

            if idx - left > 10:
                seen.add(str(word[idx - 9 : idx + 1]))

            rlt = max(rlt, idx - left)
        return rlt
'''


# this is NOT my solution
class Solution:
    def longestValidSubstring(self, word: str, forbidden: list[str]) -> int:
        bad: set[str] = set(forbidden)
        seen: set[str] = set()
        rlt: int = 0
        top: int = len(word) - 1

        for low in range(len(word) - 1, -1, -1):

            if top - low + 1 > 10 and word[low: low + 10] in seen:
                rlt = max(rlt, top - low + 1)
                continue

            for k in range(low, min(low + 10, top + 1)):
                if word[low: k + 1] in bad:
                    top = k - 1
                    break

            if top - low + 1 > 10:
                seen.add(word[low: low + 10])

            rlt = max(rlt, top - low + 1)
        return rlt
        

if __name__ == '__main__':
    tests = [
        ('test_00', ('cbaaaabc', ['aaa', 'cb']), 4),
    ]

    foo = Solution()
    method2test = Solution.longestValidSubstring
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
