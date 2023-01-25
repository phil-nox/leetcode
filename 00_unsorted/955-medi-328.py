# https://leetcode.com/problems/odd-even-linked-list/description/
import time
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenlist(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return head

        first_even, curnt, other = head.next, head, head.next   # 2, 1, 2
        cur_node, curnt_is_odd = first_even.next, True          # 3
        while cur_node is not None:
            curnt_is_odd = not curnt_is_odd
            curnt.next = cur_node                               # 1->3
            curnt = cur_node                                    # 3
            cur_node = cur_node.next                            # 4
            curnt, other = other, curnt                         # 2, 3

        end_of_odd, end_of_even = (curnt, other) if curnt_is_odd else (other, curnt)
        end_of_odd.next = first_even
        end_of_even.next = None
        return head





if __name__ == '__main__':
    tests = [
        ('test_00', ([0, 1], 20), 2),
    ]

    foo = Solution()
    method2test = Solution.oddEvenlist

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
