# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
import time
from typing import Optional

'''
preorder: https://i.ytimg.com/vi/WLvU5EQVZqY/maxresdefault.jpg
'''


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        rlt: list[int] = []
        stack: list[TreeNode] = []

        if root is None:
            return rlt
        stack.append(root)

        while len(stack) > 0:
            cur_node = stack.pop()
            rlt.append(cur_node.val)
            for child in (cur_node.right, cur_node.left):
                if child is not None:
                    stack.append(child)

        return rlt


if __name__ == '__main__':
    tests = []  # no_tests_sorry

    foo = Solution()
    method2test = Solution.preorderTraversal   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)

