# https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/
import time
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        close_to_end: bool = False
        wave: list[TreeNode] = [root] if root else []
        nxt_wave: list[TreeNode] = []

        while wave:
            for el in wave:
                if el is None:
                    close_to_end = True
                    continue
                if close_to_end:
                    return False
                nxt_wave.extend((el.left, el.right))
            wave, nxt_wave = nxt_wave, []
        return True


if __name__ == '__main__':
    tests = []

    foo = Solution()
    method2test = Solution.isCompleteTree

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
