# https://leetcode.com/problems/same-tree/description/
import time
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack_p = []
        stack_q = []

        if p is None or q is None:
            return True if p is None and q is None else False
        if p.val != q.val:
            return False

        stack_p.append(p)
        stack_q.append(q)
        while len(stack_p) > 0:
            cur_p_node, cur_q_node = stack_p.pop(), stack_q.pop()
            for el_p, el_q in ((cur_p_node.right, cur_q_node.right), (cur_p_node.left, cur_q_node.left)):
                if el_p is None and el_q is not None or el_p is not None and el_q is None:
                    return False
                if el_p is None and el_p is None:
                    continue
                if el_p.val != el_q.val:
                    return False
                stack_p.append(el_p)
                stack_q.append(el_q)

        return True


if __name__ == '__main__':
    tests = []  # no_tests_sorry

    foo = Solution()
    method2test = Solution.isSameTree   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
