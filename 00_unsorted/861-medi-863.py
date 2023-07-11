# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
import time
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        if k == 0:
            return [target.val]

        node2parent: dict[int, Optional[TreeNode]]
        stack: list[tuple[Optional[TreeNode], TreeNode]]
        wave: list[TreeNode]
        nxt_wave: list[TreeNode]
        seen: set[int]
                                                                    # +- dfs - create a node2parent dict
        node2parent, stack = dict(), [(None, root)]                 # |
        while stack:                                                # |
            par, cur = stack.pop()                                  # |
            node2parent[cur.val] = par                              # |
                                                                    # |
            for el in (cur.left, cur.right):                        # |
                if el is None:                                      # |
                    continue                                        # |
                stack.append((cur, el))                             # |

        wave, nxt_wave, seen = [target], [], set()                  # +- bfs - find result
        while wave:                                                 # |
            cur = wave.pop()                                        # |
            seen.add(cur.val)                                       # |
            for el in (cur.left, cur.right, node2parent[cur.val]):  # |
                if el is None or el.val in seen:                    # |
                    continue                                        # |
                nxt_wave.append(el)                                 # |
                                                                    # |
            if not wave and k == 1:                                 # +---- end condition
                return [node.val for node in nxt_wave]              # |
                                                                    # |
            if not wave:                                            # +---- next level of bfs
                wave, nxt_wave, k = nxt_wave, wave, k - 1           # |

        return []


if __name__ == '__main__':
    tests = [
        ('test_00', (__test_args__), 2),
    ]

    foo = Solution()
    method2test = Solution.distanceK
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
