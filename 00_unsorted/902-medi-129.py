# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
import time
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def path2num(num_stack: list[int]) -> int:
        rlt = 0
        for el in num_stack:
            rlt += el
            rlt *= 10
        return rlt // 10

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        rlt: int = 0
        num_stack: list[int] = []
        walk_stack: list[TreeNode] = []
        seen: set[int] = set()

        if root:
            walk_stack.append(root)

        while walk_stack:
            cur = walk_stack.pop()
            if id(cur) not in seen:                         # forward walk
                num_stack.append(cur.val)                   # leaf
                if (cur.right, cur.left) == (None, None):
                    rlt += self.path2num(num_stack)
                    num_stack.pop()
                    continue

                seen.add(id(cur))                           # not_leaf
                walk_stack.append(cur)
                if cur.right:
                    walk_stack.append(cur.right)
                if cur.left:
                    walk_stack.append(cur.left)
                continue

            num_stack.pop()                                 # backward walk
        return rlt


if __name__ == '__main__':
    tests = [
    ]

    foo = Solution()
    method2test = Solution.sumNumbers

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
