# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
import time
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        rlt, nxt_wave, wave = 0, [], [root] if root else []
        while wave:
            cur = wave.pop()
            nxt_wave.extend(el for el in (cur.left, cur.right) if el is not None)
            if not wave:
                rlt, nxt_wave, wave = rlt + 1, wave, nxt_wave
        return rlt


if __name__ == '__main__':
    tests = []

    foo = Solution()
    method2test = Solution.maxDepth

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
