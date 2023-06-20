# https://leetcode.com/problems/jump-game-iv/description/
import data_for_886
import time


class Solution:
    def minJumps(self, arr: list[int]) -> int:
        if len(arr) < 3:
            return 0 if len(arr) == 1 else 1

        teleport: dict[int, set[int]] = dict()                                  # number2index_s
        for idx, num in enumerate(arr):
            tmp = teleport.get(num, set())
            tmp.add(idx)
            teleport[num] = tmp

        graph: dict[int, set[int]] = {idx: set() for idx in range(len(arr))}    # index2index_s
        for idx in range(len(arr)):
            if idx - 1 > -1:
                graph[idx].add(idx - 1)
            if idx + 1 < len(arr):
                graph[idx].add(idx + 1)

        dfs_level = 0
        seen_node, seen_num = {0}, set()
        nxt_wave, wave = [], [0]

        while wave:
            cur = wave.pop()
            node_to_process = graph[cur]
            if arr[cur] not in seen_num:                # number2index_s use without repeat
                node_to_process |= teleport[arr[cur]]   # |
            seen_num.add(arr[cur])                      # |
            for node in node_to_process:
                if node == len(arr) - 1:    # done if end_node in next_wave
                    return dfs_level + 1    # |
                if node in seen_node:                   # index process without repeat
                    continue                            # |
                seen_node.add(node)                     # |
                nxt_wave.append(node)
            if not wave:                    # dfs_next_level
                nxt_wave, wave = [], nxt_wave
                dfs_level += 1
        return len(arr)


if __name__ == '__main__':
    tests = [
        ('test_00', ([100, -23, -23, 404, 100, 23, 23, 23, 3, 404],), 3),
        ('test_01', ([7],), 0),
        ('test_02', ([7, 6, 9, 6, 9, 6, 9, 7],), 1),
        ('test_03', ([7, 7, 2, 1, 7, 7, 7, 3, 4, 1],), 3),
        ('test_04', ([80, -86, 40, 12, 40, -98, 12, -86, -79, -4, -79, 71, 44, -43, -9, -88, 88, -43, 31, 4, 71, -86, 55, -9, -65],), 5),
        data_for_886.test_21,
        data_for_886.test_05,
        data_for_886.test_29,
    ]

    foo = Solution()
    method2test = Solution.minJumps

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
