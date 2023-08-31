# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# git commit -m "2023_08_31 - 850 - medi -   19"
import time
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_s: list[Optional[ListNode]] = [None] * 31
        cur_val: int = 0
        cur_nd: Optional[ListNode] = head

        while cur_nd:
            node_s[cur_val] = cur_nd
            cur_val, cur_nd = cur_val + 1, cur_nd.next

        if cur_val - n - 1 == -1:                  # head_case
            return node_s[1]

        node_s[cur_val - n - 1].next = node_s[cur_val - n + 1]
        return head


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
