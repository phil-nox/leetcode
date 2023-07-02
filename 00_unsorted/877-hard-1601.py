# https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/description/
import time
from dataclasses import dataclass
from collections import deque
import copy


@dataclass(slots=True)
class Path:
    seq: list[int]
    seen: set[int]

    def sub_seq(self, elem: int) -> list[int]:
        for i in range(len(self.seq)):
            if self.seq[i] == elem:
                return self.seq[i:]
        return []   # will never happen


class Solution:

    def cycle_path_s(self, start: int, graph: dict[int, dict[int, int]]) -> list[list[int]]:
        rlt: list[list[int]] = []
        to_do = deque([Path(seq=[start], seen={start})])
        while to_do:
            the_path = to_do.popleft()
            for nxt in graph.get(the_path.seq[-1], dict()).keys():
                if nxt in the_path.seen:
                    rlt.append(the_path.sub_seq(nxt))
                    continue
                to_do.append(Path(seq=[*the_path.seq, nxt], seen=the_path.seen | {nxt}))
        return rlt

    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        rlt: int = 0
        process = deque([])
        graph: dict[int, dict[int, int]] = {idx: dict() for idx in range(n)}
        in_node_s: set[int] = set()                                             # node_s with in_edge

        for fr, to in requests:
            if fr == to:
                rlt += 1
                continue
            graph[fr][to] = graph[fr].get(to, 0) + 1
            in_node_s.add(to)
        for idx in range(n):
            if idx not in in_node_s:
                graph.pop(idx)

        process.append((rlt, graph, []))
        while process:
            cur_r, cur_g, cur_p = process.popleft()         # current result, graph, path

            if cur_p:
                for fr, to in zip(cur_p[:], [*cur_p[1:], cur_p[0]]):
                    cur_g[fr][to] -= 1
                    if cur_g[fr][to] == 0:
                        cur_g[fr].pop(to)
                        if not cur_g[fr]:
                            cur_g.pop(fr)

            if not cur_g:
                continue

            start, val = cur_g.popitem()                        # + - get some start node
            cur_g[start] = val                                  # |          restore dict
            path_s = self.cycle_path_s(start, cur_g)
            if not path_s and cur_g:
                cur_g.popitem()                                 # + - remove start node which give not path_s
                process.append((cur_r, cur_g, []))
                continue

            for l_path in path_s:
                rlt = max(rlt, cur_r + len(l_path))
                process.append((cur_r + len(l_path), copy.deepcopy(cur_g), l_path))
        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', (3, [[0, 1], [1, 2], [2, 0]]), 3),
        ('test_01', (5, [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]), 5),
        ('test_02', (3, [[0, 0], [1, 2], [2, 1]],), 3),
        ('test_03', (3, [[1, 2], [1, 2], [2, 2], [0, 2], [2, 1], [1, 1], [1, 2]],), 4),
        ('test_04', (2, [[1, 1], [1, 0], [0, 1], [0, 0], [0, 0], [0, 1], [0, 1], [1, 0], [1, 0], [1, 1], [0, 0], [1, 0]]), 11),
        ('test_05', (3, [[2, 2], [2, 0], [1, 1], [2, 1], [1, 1], [2, 2], [1, 0], [0, 2], [1, 2]]), 8),
        ('test_06', (14, [[10, 4], [2, 12], [12, 13], [6, 0], [5, 2], [5, 12], [9, 10], [10, 9], [11, 7]]), 2),
        ('test_07', (9, [[5, 3], [4, 6], [7, 6], [2, 5], [3, 3], [2, 1], [7, 7], [6, 4], [0, 3], [2, 7], [8, 0], [7, 6], [2, 3], [3, 8]]), 7),
    ]

    foo = Solution()
    method2test = Solution.maximumRequests
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
