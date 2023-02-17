# https://leetcode.com/problems/shortest-path-with-alternating-colors/description/
import time
from dataclasses import dataclass, field


@dataclass(slots=True)
class Node:
    idx: int
    depth: int = -1
    red: set[int] = field(default_factory=set)
    blu: set[int] = field(default_factory=set)


class Solution:

    def _dfs(self, graph: list[Node], red_first: bool) -> None:
        cur: list[Node] = [graph[0]]
        nxt: list[Node] = list()
        depth: int = 0
        seen_as_red: set[int] = set()
        seen_as_blu: set[int] = set()

        seen_as_red.add(0) if red_first else seen_as_blu.add(0)
        while len(cur) > 0:
            while len(cur) > 0:
                nd = cur.pop()
                nd.depth = depth if nd.depth == -1 else min(depth, nd.depth)
                seen, edges = (seen_as_blu, nd.blu) if red_first else (seen_as_red, nd.red)
                for nx_nd in edges:
                    if nx_nd not in seen:
                        seen.add(nx_nd)
                        nxt.append(graph[nx_nd])
            cur, nxt, red_first, depth = nxt, cur, not red_first, depth + 1

    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        graph: list[Node] = [Node(idx=idx) for idx in range(n)]
        for start, end in redEdges:
            graph[start].red.add(end)
        for start, end in blueEdges:
            graph[start].blu.add(end)

        self._dfs(graph, True)
        self._dfs(graph, False)

        return [el.depth for el in graph]


if __name__ == '__main__':
    tests = [
        ('test_00', (3, [[0, 1], [1, 2]], []), [0, 1, -1]),
        ('test_01', (3, [[0, 1]], [[2, 1]]), [0, 1, -1]),
    ]

    foo = Solution()
    method2test = Solution.shortestAlternatingPaths

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
