# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/
import time


class Solution:

    def walk(self, edges: list[int], start: int) -> dict[int]:
        seen, rlt = {start}, {start: 0}
        nxt = edges[start]
        idx = 0
        while nxt != -1 and nxt not in seen:
            seen.add(nxt)
            idx += 1
            rlt[nxt] = idx
            nxt = edges[nxt]
        return rlt

    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        path1, path2 = self.walk(edges, node1), self.walk(edges, node2)
        rlt, dist = -1, None
        small, big = (path1, path2) if len(path1) < len(path2) else (path2, path1)
        for node, moves1 in sorted(small.items()):
            moves2 = big.get(node, None)
            if moves2 is None:
                continue
            if dist is None:
                rlt, dist = node, max(moves1, moves2)
                continue
            rlt, dist = (node, max(moves1, moves2)) if max(moves1, moves2) < dist else (rlt, dist)
        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([2, 2, 3, -1], 0, 1), 2),
        ('test_01', ([1, 2, -1], 0, 2), 2),
    ]

    foo = Solution()
    method2test = Solution.closestMeetingNode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
