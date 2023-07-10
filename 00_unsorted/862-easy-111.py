# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
import time
from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        to_do = deque([(1, root)])
        while to_do:
            level, cur = to_do.popleft()
            nxt_s = tuple((level + 1, el) for el in (cur.left, cur.right) if el is not None)
            if not nxt_s:
                return level
            to_do.extend(nxt_s)
        return 0  # will never happen
        

if __name__ == '__main__':
    tests = [
        ('test_00', (__test_args__), 2),
    ]

    foo = Solution()
    method2test = Solution.minDepth
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
