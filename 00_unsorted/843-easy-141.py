# https://leetcode.com/problems/linked-list-cycle/description/
# git commit -m "2023_09_04 - 843 - easy -  141"
import time
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        double_walk = walk = head

        while double_walk and double_walk.next:
            double_walk, walk = double_walk.next.next, walk.next
            if walk is double_walk:
                return True
        return False


if __name__ == '__main__':
    tests = [
        ('test_00', (), 2),
    ]

    foo = Solution()
    method2test = Solution.__init__
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
