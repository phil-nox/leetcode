# https://leetcode.com/problems/find-eventual-safe-states/description/
import time


class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        seen: list[int] = [0] * len(graph)                  # 0 - unseen,       1 - seen
                                                            # 2 - cycle         3 - safe

        count: list[int] = [-1] * len(graph)                # 0 - node is in final_state otherwise in process
        stack: list[tuple[int, bool]]
        last_val: int

        for idx in range(len(graph)):
            if seen[idx] != 0:
                continue

            stack, last_val = [(idx, True)], 3
            while stack:

                cur, forward = stack.pop()
                if forward:                                         # forward_walk
                    if seen[cur] == 0:                                  # node is unseen yet and has no_state
                        count[cur] = len(graph[cur])                    # set count of children
                        if not graph[cur]:
                            seen[cur] = last_val = 3
                            continue

                        seen[cur] = 1                                   # set node as seen
                        for nxt in graph[cur]:                          # add children to stack
                            stack.append((cur, False))
                            stack.append((nxt, True))
                        continue

                    if count[cur] == 0:                                 # if node is in final_state
                        last_val = seen[cur]                            # just copy status of the node
                        continue

                    seen[cur] = last_val = 2                            # if node is in process - it's cycle
                    continue

                count[cur] -= 1                                     # backward_walk
                if seen[cur] == 1 or last_val == 2:                     # update status to cycle 2 if cycle exist
                    seen[cur] = last_val
                last_val = seen[cur]

        return sorted([idx for idx, el in enumerate(seen) if el == 3])


if __name__ == '__main__':
    tests = [
        ('test_00', (__test_args__), 2),
    ]

    foo = Solution()
    method2test = Solution.eventualSafeNodes
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
