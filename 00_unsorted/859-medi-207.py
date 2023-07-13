# https://leetcode.com/problems/course-schedule/description/
import time


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph:      dict[int, set[int]] = {idx: set() for idx in range(numCourses)}
        seen:       list[int]           = [-1] * numCourses         # (-1) - unseen, (0) - ok, (> 0) - not_ok
        stack:      list[int]           = []
        back_val:   int                 = 0                         # value of previous node for backward_walk

        for fr, to in prerequisites:
            graph[fr].add(to)

        for idx in range(numCourses):                               # +-iterate all nodes
            if seen[idx] > 0:                                       # |     if node is seen & not_ok - fail
                return False                                        # |
            if seen[idx] == 0:                                      # |     if node is seen & ok - move on
                continue                                            # |
            stack.append(idx)                                       # |     process the node

            while stack:                                            # +- dfs (processing the node)
                cur = stack.pop()                                   # |
                                                                    # |
                if seen[cur] == -1:                                     # +- forward_walk
                    seen[cur] = len(graph[cur])                         # |  back_val = 0 in case no_child
                    for nxt in graph[cur]:                              # |
                        stack.append(cur)                               # |
                        stack.append(nxt)                               # |
                    continue                                            # |

                if back_val == 0 and seen[cur] > 0:                     # +- backward_walk
                    seen[cur] -= 1                                      # |
                back_val = seen[cur]                                    # |

        return not any(seen)                                        # +- all nodes must be seen & ok


if __name__ == '__main__':
    tests = [
        ('test_00', (__test_args__), 2),
    ]

    foo = Solution()
    method2test = Solution.canFinish
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
