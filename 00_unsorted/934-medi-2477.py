# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/description/
import time
from dataclasses import dataclass, field


@dataclass(slots=True)
class Node:
    idx: int
    edges: list['Node'] = field(default_factory=list)
    rider: int = 1


class Solution:

    def minimumFuelCost(self, roads: list[list[int]], seats: int) -> int:
        graph: dict[int, Node] = {0: Node(idx=0)}
        for idx, jdx in roads:
            nd_i, nd_j = graph.get(idx, Node(idx=idx)), graph.get(jdx, Node(idx=jdx))
            nd_i.edges.append(nd_j)
            nd_j.edges.append(nd_i)
            graph[idx], graph[jdx] = nd_i, nd_j

        stack: list[Node] = [graph[0]]
        seen: set[int] = set()
        prev_nd: Node = graph[0]
        rlt: int = 0
        while len(stack) > 0:
            cur: Node = stack.pop()
            if cur.idx not in seen:     # forward walk
                seen.add(cur.idx)
                for nxt_nd in cur.edges:
                    if nxt_nd.idx not in seen:
                        stack.extend((cur, nxt_nd))
                prev_nd = cur
                continue
                                        # backward walk
            if prev_nd.idx == 0:
                prev_nd = cur
                continue
            rlt += prev_nd.rider // seats
            rlt += 1 if prev_nd.rider % seats != 0 else 0
            cur.rider += prev_nd.rider
            prev_nd = cur

        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([[0, 1], [0, 2], [0, 3]], 5), 3),
        ('test_01', ([[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2), 7),
        ('test_02', ([], 1), 0),
    ]

    foo = Solution()
    method2test = Solution.minimumFuelCost

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
