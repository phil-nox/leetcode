# https://leetcode.com/problems/add-two-numbers-ii/description/
import time
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack_a: list[int] = []
        stack_b: list[int] = []
        rest: int = 0
        rlt: Optional[ListNode] = None

        for fr, to in ((l1, stack_a), (l2, stack_b)):
            while fr:
                to.append(fr.val)
                fr = fr.next

        while stack_a and stack_b:
            rest, tmp = divmod(stack_a.pop() + stack_b.pop() + rest, 10)
            rlt = ListNode(tmp, rlt)

        to_finish = stack_a if len(stack_a) > len(stack_b) else stack_b
        while to_finish:
            rest, tmp = divmod(to_finish.pop() + rest, 10)
            rlt = ListNode(tmp, rlt)

        if rest:
            rlt = ListNode(1, rlt)

        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([7,2,4,3], [5,6,4]), [7,8,0,7]),
    ]

    foo = Solution()
    method2test = Solution.__init__
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
