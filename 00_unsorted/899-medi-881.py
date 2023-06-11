# https://leetcode.com/problems/boats-to-save-people/description/
import time
from collections import deque


class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        vault: deque = deque(sorted(people))
        rlt: int = 0
        while vault:
            cur = vault.pop()
            if vault and vault[0] + cur <= limit:
                vault.popleft()
            rlt += 1
        return rlt
        

if __name__ == '__main__':
    tests = [
        ('test_00', ([1, 2], 3), 1),
    ]

    foo = Solution()
    method2test = Solution.numRescueBoats

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
