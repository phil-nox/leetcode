# https://leetcode.com/problems/swap-nodes-in-pairs/description/
# git commit -m "2023_09_03 - 844 - medi -   24"
import time
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        rlt = head.next
        head.next = head.next.next
        rlt.next = head

        cur = head
        while cur.next and cur.next.next:
            swap_a, swap_b = cur.next, cur.next.next
            cur.next = swap_b
            swap_a.next = swap_b.next
            swap_b.next = swap_a
            cur = swap_a

        return rlt
        

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
