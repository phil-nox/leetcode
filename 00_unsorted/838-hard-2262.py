# https://leetcode.com/problems/total-appeal-of-a-string/description/
import time


class Solution:
    def appealSum(self, s: str) -> int:
        seen = dict()
        prev, rlt = 0, 0

        for idx in range(0, len(s)):
            prev = prev + idx - seen.get(s[idx], -1)
            rlt += prev
            seen[s[idx]] = idx

        return rlt
        

if __name__ == '__main__':
    tests = [
        ('test_00', ('abbca',), 28),
    ]

    foo = Solution()
    method2test = Solution.appealSum
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
