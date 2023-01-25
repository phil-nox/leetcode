# https://leetcode.com/problems/gas-station/description/
import time

'''
        # 4 - 1 # 3
        # 5 - 2 # 3
        # 1 - 3 # -2
        # 4 - 2 # -2
        # 3 - 5 # -2

        # 2 - 3 # -1
        # 3 - 4 # -1
        # 4 - 3 # 1

        # idx = 0 delta = -2
        # idx = 1 delta = -2

        # idx = 0 delta = -4
        # idx = 2 delta = -2

        # idx = 0 delta = -6
        # idx = 3 delta = 3
        # idx = 4 delta = 3

        #idx = 0 delta =-6
        #idx = 3 delta = 6
'''


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        neg_part, pos_part = 0, 0
        pos_idx = None

        for idx in range(len(gas)):
            diff = gas[idx] - cost[idx]

            if pos_idx is not None:
                pos_part += diff
                if pos_part < 0:
                    pos_idx, neg_part = None, neg_part + pos_part
            elif diff < 0:
                neg_part += diff
            else:
                pos_idx, pos_part = idx, diff

        if pos_idx is None or pos_part + neg_part < 0:
            return -1
        return pos_idx


if __name__ == '__main__':
    tests = [
        ('test_00', ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2],), 3),
        ('test_01', ([2, 3, 4], [3, 4, 3],), -1),
        ('test_03', ([7, 1, 0, 11, 4], [5, 9, 1, 2, 5],), 3),
    ]

    foo = Solution()
    method2test = Solution.canCompleteCircuit   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
