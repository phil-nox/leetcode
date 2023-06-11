# https://leetcode.com/problems/split-with-minimum-sum/description/
import time
import heapq


class Solution:
    def splitNum(self, num: int) -> int:
        total = [el for el in str(num)]
        heapq.heapify(total)
        a, b = [], []
        cur = a
        while total:
            cur.append(heapq.heappop(total))
            cur = b if cur is a else a
        return int(''.join(a)) + int(''.join(b))


if __name__ == '__main__':
    tests = [
        ('test_00', (4325,), 59),
    ]

    foo = Solution()
    method2test = Solution.splitNum

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
