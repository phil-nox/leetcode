# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/
import time

'''
1
2 diff 1
rlt 1

1
3 diff 2
rlt 2

2
3 diff 1
rlt 1

2
4 diff 2
rlt 1
'''


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        rlt = 0 if low % 2 == 0 else 1
        rlt += (high-low) // 2
        rlt += 1 if low % 2 == 0 and (high-low) % 2 != 0 else 0
        return rlt
    

if __name__ == '__main__':
    tests = [
        ('test_00', (3, 7), 3),
        ('test_01', (8, 10), 1),
        ('test_02', (3, 8), 3),
        ('test_03', (3, 9), 4),
        ('test_04', (2, 8), 3),
        ('test_05', (2, 7), 3),
        ('test_06', (2, 6), 2),
        ('test_07', (0, 0), 0),
        ('test_08', (0, 1), 1),
        ('test_09', (3, 4), 1),
        ('test_10', (4, 5), 1),
    ]

    foo = Solution()
    method2test = Solution.countOdds

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
