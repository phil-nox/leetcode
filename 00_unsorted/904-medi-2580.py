# https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/description/
import time


class Solution:
    def countWays(self, ranges: list[list[int]]) -> int:
        ranges.sort(key=lambda x: x[0])
        groups = 1
        low, top = ranges[0]
        for n_low, n_top in ranges[1:]:
            if n_low <= top:
                top = max(top, n_top)
                continue
            groups += 1
            low, top = n_low, n_top
        return (2 ** groups) % (10 ** 9 + 7)


if __name__ == '__main__':
    tests = [
        ('test_00', ([[0, 0], [1, 2]],), 4),
        #('test_01', ([[0, 0], [8, 9], [12, 13], [1, 3]],), 16),
    ]

    foo = Solution()
    method2test = Solution.countWays

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
