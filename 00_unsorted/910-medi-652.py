# https://leetcode.com/problems/find-duplicate-subtrees/description/
import time
from typing import Optional, Any
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> list[Optional[TreeNode]]:
        rlt: list[TreeNode] = list()

        book: dict[int, Any] = dict()
        seen: dict[int, TreeNode] = dict()
        stack: list[TreeNode] = [root] if root else []

        prev, cur = root, root
        countdown: dict[int, int] = dict()
        samecount: dict[str, int] = dict()

        while stack:
            prev, cur = cur, stack.pop()

            # forward walk
            if id(cur) not in seen:
                seen[id(cur)] = cur
                for el in (cur.left, cur.right):
                    if el:
                        stack.extend([cur, el])
                        countdown[id(cur)] = countdown.get(id(cur), 0) + 1
                if (cur.left, cur.right) == (None, None):
                    stack.append(cur)
                    countdown[id(cur)] = countdown.get(id(cur), 0) + 1
                continue

            # backward walk
            note = book.get(id(cur), (None, cur.val, None))
            if prev == cur.left:
                note = (book.get(id(prev)), cur.val, note[2])
            if prev == cur.right:
                note = (note[0], cur.val, book.get(id(prev)))
            book[id(cur)] = note

            countdown[id(cur)] -= 1
            if countdown[id(cur)] == 0:
                samecount[note] = samecount.get(note, 0) + 1
                if samecount[note] == 2:
                    rlt.append(seen[id(cur)])

        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([0, 1], 20), 2),
    ]

    foo = Solution()
    method2test = Solution.findDuplicateSubtrees

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
