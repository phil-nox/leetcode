# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/
import time

'''
class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        vault: dict[int, int] = dict()

        for el in arr:
            nxt = el + difference
            cur = vault.pop(el) + 1 if el in vault else 1
            vault[nxt] = cur if cur > vault.get(nxt, 0) else vault.get(nxt, 0)

        return max(vault.values())
'''

from collections import defaultdict


class Solution:                                                         # copy of another user's solution
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        seen = defaultdict(int)
        for el in arr:
            seen[el] = seen[el - difference] + 1
        return max(seen.values())


if __name__ == '__main__':
    tests = [
        ('test_00', ([1, 5, 7, 8, 5, 3, 4, 2, 1], -2), 4),
    ]

    foo = Solution()
    method2test = Solution.longestSubsequence
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
