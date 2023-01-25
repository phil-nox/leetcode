# https://leetcode.com/problems/maximum-tastiness-of-candy-basket/description/
import time
from typing import List

'''
0. How much does it cost to validate a solution for a specific case (specific k)?
        -> O(N)

1. Do the solutions have some correlation with the order? 
    Ex.: if k1 is valid solution then k0 is valid if k0 < k1
    Ex.: if k3 is not_valid solution then k4 is not_valid if k4 > k1
        -> So binary search can be apply -> Total complexity will be O(NlogN)
'''


class Solution:

    def _solution4diff_exist(self, price: List[int], k: int, diff: int) -> bool:
        nxt_val = price[0] + diff    # array should is sorted, take min value
        check_k = k - 1
        for el in price[1:]:
            if el >= nxt_val:
                nxt_val = el + diff
                if (check_k := check_k - 1) < 1:
                    return True
        return False

    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        btm, top = 0, price[-1] - price[0] + 1      # minimal possible diff and max pos. diff + 1
        prev_diff, cur_diff = btm, top              # just (prev_diff != cur_diff) should be True at this point
        while prev_diff != cur_diff:                # why this work: 2 == 2 + (3-2)//2
            prev_diff, cur_diff = cur_diff, btm + (top - btm) // 2  # prioritise min boarder
            if self._solution4diff_exist(price, k, cur_diff):
                btm = cur_diff
            else:
                top = cur_diff
        return cur_diff


if __name__ == '__main__':
    tests = [
        ('test_00', ([13, 5, 1, 8, 21, 2], 3), 8),
        ('test_01', ([1, 3, 1], 2), 2),
        ('test_02', ([7, 7, 7, 7], 2), 0),
    ]

    foo = Solution()
    method2test = Solution.maximumTastiness   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        rlt = method2test(foo, *inpt)
        assert rlt == outpt, print(f'Problem ⚠️ {name} - {rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)

