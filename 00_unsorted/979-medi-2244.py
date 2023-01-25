# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/description/
import time

'''
    divmod
2 -> 0, 2 -> 1 [2]
3 -> 1, 0 -> 1 [3]

4 -> 1, 1 -> 2 [2,2]
5 -> 1, 2 -> 2 [3,2]
6 -> 2, 0 -> 2 [3,3]

7 -> 2, 1 -> 3 [3,2,2]
8 -> 2, 2 -> 3 [3,3,2]
9 -> 3, 0 -> 3 [3,3,3]

10 -> 3, 1 -> 4 [3,3,2,2]
11 -> 3, 2 -> 4 [3,3,3,2]
12 -> 4, 0 -> 4 [3,3,3,3]

13 -> 4, 1 -> 5 [3,3,3,2,2]  
'''


class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        rlt = 0
        vault = dict()
        for el in tasks:
            vault[el] = vault.get(el, 0) + 1

        for item in vault.values():
            if item == 1:
                return -1
            div, rem = divmod(item, 3)
            rlt = rlt + div if rem == 0 else rlt + div + 1
        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([2, 2, 3, 3, 2, 4, 4, 4, 4, 4],), 4),
        ('test_01', ([2, 3, 3],), -1),
        ('test_02', ([2, 2],), 1),
        ('test_03', ([2, 2, 2],), 1),
        ('test_04', ([2, 2, 2, 2],), 2),
        ('test_05', ([2, 2, 2, 2, 2],), 2),
        ('test_06', ([2, 2, 2, 2, 2, 2],), 2),
    ]

    foo = Solution()
    method2test = Solution.minimumRounds   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
