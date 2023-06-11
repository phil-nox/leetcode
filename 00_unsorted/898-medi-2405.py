# https://leetcode.com/problems/optimal-partition-of-string/description/
import time


class Solution:
    def partitionString(self, s: str) -> int:
        vault: set[str] = set()
        rlt: int = 1  # last one will not count
        for el in s:
            if el in vault:
                rlt += 1
                vault = set(el)
                continue
            vault.add(el)
        return rlt
        

if __name__ == '__main__':
    tests = [
        ('test_00', ('abacaba',), 4),
    ]

    foo = Solution()
    method2test = Solution.partitionString

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
