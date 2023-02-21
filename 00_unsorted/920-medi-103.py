# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
import time
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        wave: list[TreeNode] = [root] if root else []
        nxt_wave: list[TreeNode] = []
        left_2_right: bool = True
        rlt: list[list[int]] = []
        level: list[int] = []
        child_order: tuple[Optional[TreeNode], Optional[TreeNode]]
        while wave:
            cur: TreeNode = wave.pop()
            level.append(cur.val)
            child_order = (cur.left, cur.right) if left_2_right else (cur.right, cur.left)
            nxt_wave.extend(nd for nd in child_order if nd)
            if not wave:
                rlt.append(level)
                wave, nxt_wave, left_2_right, level = nxt_wave, wave, not left_2_right, []
        return rlt


if __name__ == '__main__':
    tests = []

    foo = Solution()
    method2test = Solution.zigzagLevelOrder

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
