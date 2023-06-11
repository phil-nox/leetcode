# https://leetcode.com/problems/construct-quad-tree/description/
import time

'''

[0,0] - [0,1]
  |       |
[1,0] - [1,1]


[0 , 0]  -  [0 ,15]
   |           |
[15, 0]  -  [15,15]

[0,0] - [0, 7]
'''


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: list[list[int]]) -> Node:
        root = Node(val=1, isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
        to_do: list[tuple[Node, int, int, int, int]] = [(root, 0, len(grid), 0, len(grid))]

        while to_do:
            input()
            print(len(to_do))
            [print(el) for el in to_do]
            cur, row_s, row_e, col_s, col_e = to_do.pop()
            print('👇')
            [print(el) for el in to_do]
            print('\t', row_s, row_e, col_s, col_e)
            cur.val = grid[row_s][col_s]
            for r in range(row_s, row_e):
                for c in range(col_s, col_e):
                    if cur.val != grid[r][c]:
                        cur.isLeaf = False
                        break
                if not cur.isLeaf:
                    break
            print('\t', cur.isLeaf)

            if cur.isLeaf:
                continue

            # not_leaf
            cur.topLeft = Node(val=1, isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
            to_do.append((cur.topLeft, row_s, (row_e - row_s) // 2 + row_s, col_s, (col_e - col_s) // 2 + col_s))

            cur.topRight = Node(val=1, isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
            to_do.append((cur.topRight, row_s, (row_e - row_s) // 2 + row_s, (col_e - col_s) // 2 + col_s, col_e))

            cur.bottomLeft = Node(val=1, isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
            to_do.append((cur.bottomLeft, (row_e - row_s) // 2 + row_s, row_e, col_s, (col_e - col_s) // 2 + col_s))

            cur.bottomRight = Node(val=1, isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
            to_do.append((cur.bottomRight, (row_e - row_s) // 2 + row_s, row_e, (col_e - col_s) // 2 + col_s, col_e))

        return root


if __name__ == '__main__':
    tests = [
        ('test_00', ([[1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1]],), 2),
    ]

    foo = Solution()
    method2test = Solution.construct

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
