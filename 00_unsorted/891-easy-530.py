# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
# 00 : 17 : 52 # 2_attempts
# check 927-easy-783 !
import time

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


''' Bad Heap solution 
import heapq
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        rlt: int = abs(root.val - root.left.val) if root.left else abs(root.val - root.right.val)
        stack = [root]
        vault = []
        while stack:
            cur = stack.pop()
            heapq.heappush(vault, cur.val)
            for child in (cur.left, cur.right):
                if child:
                    stack.append(child)

        mem = heapq.heappop(vault)
        while vault:
            tmp = heapq.heappop(vault)
            diff = tmp - mem
            rlt = diff if diff < rlt else rlt
            mem = tmp

        return rlt
'''


# InOrder traversal     # https://t.ly/h--Q
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        rlt, prev = float('inf'), float('-inf')     # int,              int
        stack, forward = [root], True               # list[TreeNode],   bool
        while stack:
            cur: TreeNode = stack.pop()
            # dead_end case
            if cur is None:
                forward = False
                continue

            # forward_walk
            if forward:
                stack.extend((cur.right, cur, cur.left))    # inOrder traversal
                continue

            # backward_walk
            diff = cur.val - prev
            rlt = diff if diff < rlt else rlt
            prev = cur.val
            forward = True
        return rlt
        

if __name__ == '__main__':
    tests = []

    foo = Solution()
    method2test = Solution.getMinimumDifference
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
