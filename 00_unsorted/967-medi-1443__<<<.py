# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/
import time
from dataclasses import dataclass, field

'''
    use DFS
    # forward walk - just add unseen nodes
    # backward walk - count SUBtree value
'''


@dataclass(slots=True)
class Node:
    idx:    int
    apple:  bool
    nxt:    list[int] = field(default_factory=list)
    count:  int = 0


class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        graph: list[Node] = [Node(idx=idx, apple=el) for idx, el in enumerate(hasApple)]
        for nd_a, nd_b in edges:
            graph[nd_a].nxt.append(nd_b)
            graph[nd_b].nxt.append(nd_a)

        cur_node:   Node = graph[0]
        stack:      list[int] = list()
        seen:       set[int] = set()
        stack.append(0)

        while len(stack) > 0:
            prev_node = cur_node
            cur_idx = stack.pop()
            cur_node: Node = graph[cur_idx]

            if cur_node.idx not in seen:    # forward walk
                for nxt_node in cur_node.nxt:
                    if nxt_node not in seen:
                        stack.append(cur_node.idx)
                        stack.append(nxt_node)
                seen.add(cur_node.idx)
            else:                           # backward walk
                if prev_node.count > 0 or prev_node.apple is True:
                    cur_node.count += prev_node.count + 1
        return cur_node.count * 2


if __name__ == '__main__':
    tests = [
        ('test_00', (7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False, False, True, False, True, True, False]), 8),
        ('test_01', (7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False, False, True, False, False, True, False]), 6),
        ('test_02', (7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False, False, False, False, False, False, False]), 0),
    ]

    foo = Solution()
    method2test = Solution.minTime   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
