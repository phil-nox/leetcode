# https://leetcode.com/problems/put-marbles-in-bags/description/
import time
from collections import deque


class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        if s.startswith('0') or s.endswith('0'):
            return -1
        vault = [
            '11110100001001',   # len = 14
            '110000110101',     # len = 12
            '1001110001',       # len = 10
            '1111101',          # len = 07     125
            '11001',            # len = 05      25
            '101',              # len = 03       5
            # '1',              # len = 01       1
        ]

        to_do = deque([(0, s)])                         # partition_counter and rest_of_string_to_process

        while to_do:
            count, cur = to_do.popleft()
            if not cur:
                return count                                                        # len(partition)

            for check in vault:
                if cur.startswith(check) and not cur[len(check):].startswith('0'):
                    to_do.append((count + 1, cur[len(check):]))                     # tuple(*partition, check)

            nxt = cur[1:]
            if nxt.startswith('0'):
                continue
            to_do.append((count + 1, nxt))                                          # tuple(*partition, '1')

        return -1
        

if __name__ == '__main__':
    tests = [
        ('test_00', ("1101",), 2),
        ('test_01', ("1011",), 2),
        ('test_02', ("111",), 3),
        ('test_03', ("0",), -1),
        ('test_04', ("101011",), -1),
    ]

    foo = Solution()
    method2test = Solution.minimumBeautifulSubstrings
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
