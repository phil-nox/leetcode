# https://leetcode.com/problems/invert-binary-tree/description/
import time
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        wave: list[TreeNode] = [root] if root else []
        nxt_wave: list[TreeNode] = []
        while wave:
            cur = wave.pop()
            nxt_wave.extend(nd for nd in (cur.left, cur.right) if nd)
            cur.left, cur.right = cur.right, cur.left
            if not wave:
                wave, nxt_wave = nxt_wave, wave
        return root


if __name__ == '__main__':
    tests = []

    foo = Solution()
    method2test = Solution.invertTree

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
