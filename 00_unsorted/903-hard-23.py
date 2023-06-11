# https://leetcode.com/problems/merge-k-sorted-lists/description/
import time
import heapq
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    def __init__(self, root: ListNode):
        self.a_list = root

    def __lt__(self, other):
        return self.a_list.val < other.a_list.val

    def cut(self) -> ListNode:
        rlt = self.a_list
        self.a_list = rlt.next
        return rlt


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        rlt: Optional[ListNode] = None
        tail: Optional[ListNode] = None
        vault: list[Node] = []
        for el in lists:
            if el is not None:
                heapq.heappush(vault, Node(root=el))

        if vault:
            cur = heapq.heappop(vault)
            rlt = cur.cut()
            tail = rlt
            if cur.a_list is not None:
                heapq.heappush(vault, cur)

        while vault:
            cur = heapq.heappop(vault)
            tail.next = cur.cut()
            tail = tail.next
            if cur.a_list is not None:
                heapq.heappush(vault, cur)

        if tail:
            tail.next = None

        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([0, 1], 20), 2),
    ]

    foo = Solution()
    method2test = Solution.mergeKLists

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
