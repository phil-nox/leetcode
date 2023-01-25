# https://leetcode.com/problems/all-paths-from-source-to-target/description/
import time
from dataclasses import dataclass, field


@dataclass(slots=True)
class Path:
    idx: int
    previous: list[int] = field(default_factory=list)


class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        cur_level, nxt_level, rlt = list(), list(), list()
        cur_level.append(Path(idx=0))

        while len(cur_level) != 0:
            for path in cur_level:
                cur_prev = path.previous[:]
                cur_prev.append(path.idx)

                if path.idx == len(graph) - 1:
                    rlt.append(cur_prev)
                    continue

                for nxt_node in graph[path.idx]:
                    nxt_level.append(Path(idx=nxt_node, previous=cur_prev[:]))
            cur_level, nxt_level = nxt_level, []

        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([[1, 2], [3], [3], []],), [[0, 1, 3], [0, 2, 3]]),
        ('test_01', ([[4, 3, 1], [3, 2, 4], [3], [4], []],), [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]),
    ]

    foo = Solution()
    method2test = Solution.allPathsSourceTarget   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert {tuple(el) for el in test_rlt} == {tuple(el) for el in outpt}, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
