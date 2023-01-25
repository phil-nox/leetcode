# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/description/
import time
from collections import Counter
from dataclasses import dataclass, field


@dataclass(slots=True)
class Node:
    idx: int
    rune: str
    edges: set[int] = field(default_factory=set)
    subtree: Counter = field(init=False)

    def __post_init__(self):
        self.subtree = Counter({self.rune: 1})


class Solution:
    def countSubTrees(self, n: int, edges: list[list[int]], labels: str) -> list[int]:
        graph: list[Node] = [Node(idx=idx, rune=el) for idx, el in enumerate(labels)]
        for nd_a, nd_b in edges:
            graph[nd_a].edges.add(nd_b)
            graph[nd_b].edges.add(nd_a)

        seen: set[int] = set()
        stack: list[int] = [0]
        cur_node: Node = graph[0]

        while len(stack) > 0:
            prev_node = cur_node
            cur_node = graph[stack.pop()]

            if cur_node.idx not in seen:                # forward walk
                seen.add(cur_node.idx)
                for neighbour in cur_node.edges:
                    if neighbour not in seen:
                        stack.append(cur_node.idx)
                        stack.append(neighbour)
                continue

            cur_node.subtree.update(prev_node.subtree)  # backward walk

        return [node.subtree[node.rune] for node in graph]


if __name__ == '__main__':
    tests = [
        ('test_00', (7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], "abaedcd"), [2, 1, 1, 1, 1, 1, 1]),
        ('test_01', (4, [[0, 1], [1, 2], [0, 3]], "bbbb"), [4, 2, 1, 1]),
        ('test_02', (5, [[0, 1], [0, 2], [1, 3], [0, 4]], "aabab"), [3, 2, 1, 1, 1]),
    ]

    foo = Solution()
    method2test = Solution.countSubTrees   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
