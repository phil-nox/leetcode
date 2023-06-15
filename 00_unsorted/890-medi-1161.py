# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/
# 00 : 05 : 11
import time
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        cur_sum, level, rlt, max_sum = 0, 1, 1, (-10**5 * 10**4)  # task boundary
        nxt_wave, wave = [], [root] if root else []

        while wave:
            cur_node: TreeNode = wave.pop()
            cur_sum += cur_node.val
            if cur_node.left:
                nxt_wave.append(cur_node.left)
            if cur_node.right:
                nxt_wave.append(cur_node.right)
            if not wave:    # next level
                if max_sum < cur_sum:
                    rlt, max_sum = level, cur_sum
                nxt_wave, wave = wave, nxt_wave
                cur_sum, level = 0, level + 1
        return rlt


if __name__ == '__main__':
    tests = []

    foo = Solution()
    method2test = Solution.maxLevelSum
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
