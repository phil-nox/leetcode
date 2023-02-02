# https://leetcode.com/problems/merge-two-sorted-lists/description/
import time
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val:   int = val
        self.next:  'ListNode' = next


class Solution:
    def mergeTwolists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if None in (list1, list2):
            return list2 if list1 is None else list1

        rlt = list1 if list1.val < list2.val else list2
        cur, n1, n2 = (rlt, list1.next, list2) if list1.val < list2.val else (rlt, list1, list2.next)
        while None not in (n1, n2):
            cur.next = n1 if n1.val < n2.val else n2
            cur, n1, n2 = (cur.next, n1.next, n2) if n1.val < n2.val else (cur.next, n1, n2.next)
        if (None, None) != (n1, n2):
            cur.next = n2 if n1 is None else n1
        return rlt


if __name__ == '__main__':
    pass
