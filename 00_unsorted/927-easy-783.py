# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
import time


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        rlt, prev = None, None              # int,              TreeNode
        stack, seen = [root], set()         # list[TreeNode],   set[TreeNode]
        while stack:
            cur: TreeNode = stack.pop()
            # forward walk
            if cur not in seen:
                seen.add(cur)
                stack.extend((cur.right,) if cur.right else ())     # InOrder traversal     # https://t.ly/h--Q
                stack.append(cur)                                   # InOrder traversal
                stack.extend((cur.left,) if cur.left else ())       # InOrder traversal
                continue
            # backward walk
            if prev is not None:
                diff = cur.val - prev.val
                rlt = diff if (rlt is None or diff < rlt) else rlt
            prev = cur
        return rlt


if __name__ == '__main__':
    tests = []

    foo = Solution()
    method2test = Solution.minDiffInBST

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
