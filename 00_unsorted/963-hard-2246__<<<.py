# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/description/
import time
import heapq
from dataclasses import dataclass, field


@dataclass(slots=True)
class Node:
    idx:    int
    rune:   str
    adjs:   list[int] = field(default_factory=list)
    paths:  list[int] = field(init=False)

    def __post_init__(self):
        self.paths = [0]


class Solution:
    def longestPath(self, parent: list[int], s: str) -> int:
        graph: list[Node] = [Node(idx=idx, rune=el) for idx, el in enumerate(s)]

        for nd_a, nd_b in enumerate(parent):
            if nd_b == -1:
                continue
            graph[nd_a].adjs.append(nd_b)
            graph[nd_b].adjs.append(nd_a)

        seen:       set[int] = set()
        stack:      list[int] = [0]
        cur_node:   Node = graph[0]
        glob_min = 0

        while len(stack) > 0:
            prev_node = cur_node
            cur_node = graph[stack.pop()]

            # forward walk
            if cur_node.idx not in seen:
                seen.add(cur_node.idx)
                for adj in cur_node.adjs:
                    if adj not in seen:
                        stack.append(cur_node.idx)
                        stack.append(adj)
                continue

            # backward walk
            if prev_node.rune == cur_node.rune:
                continue

            heapq.heappush(cur_node.paths, prev_node.paths[0] - 1)
            top = cur_node.paths[0]
            sec_top = min(0, *cur_node.paths[1:3])
            glob_min = top + sec_top if top + sec_top < glob_min else glob_min

        return -glob_min + 1


if __name__ == '__main__':
    tests = [
        ('test_00', ([-1, 0, 0, 1, 1, 2], "abacbe"), 3),
        ('test_01', ([-1, 0, 0, 0], "aabc"), 3),
        ('test_02', ([-1, ], "a"), 1),
        ('test_03', ([-1, 0, 0, 1, 1, 3], "aabbcd"), 4),
        ('test_04', ([-1,137,65,60,73,138,81,17,45,163,145,99,29,162,19,20,132,132,13,60,21,18,155,65,13,163,125,102,96,60,50,101,100,86,162,42,162,94,21,56,45,56,13,23,101,76,57,89,4,161,16,139,29,60,44,127,19,68,71,55,13,36,148,129,75,41,107,91,52,42,93,85,125,89,132,13,141,21,152,21,79,160,130,103,46,65,71,33,129,0,19,148,65,125,41,38,104,115,130,164,138,108,65,31,13,60,29,116,26,58,118,10,138,14,28,91,60,47,2,149,99,28,154,71,96,60,106,79,129,83,42,102,34,41,55,31,154,26,34,127,42,133,113,125,113,13,54,132,13,56,13,42,102,135,130,75,25,80,159,39,29,41,89,85,19], "ajunvefrdrpgxltugqqrwisyfwwtldxjgaxsbbkhvuqeoigqssefoyngykgtthpzvsxgxrqedntvsjcpdnupvqtroxmbpsdwoswxfarnixkvcimzgvrevxnxtkkovwxcjmtgqrrsqyshxbfxptuvqrytctujnzzydhpal"), 17),
    ]

    foo = Solution()
    method2test = Solution.longestPath

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
