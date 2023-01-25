# https://leetcode.com/problems/number-of-good-paths/description/
import time
import data_for_961
import heapq
from typing import Optional
from dataclasses import dataclass, field


@dataclass(slots=True)
class Node:
    idx: int
    val: int
    adjs: list[int] = field(default_factory=list)
    subtree: Optional['HeapOfTupleWithReference'] = None


@dataclass(slots=True)
class HeapOfTupleWithReference:
    vault: list[list[int, int]] = field(default_factory=list)
    links: dict[int, list[int, int]] = field(default_factory=dict)

    def top(self):
        if len(self.vault) == 0:
            return None
        return self.vault[0][0]

    def pop(self):
        rlt = heapq.heappop(self.vault)
        del self.links[rlt[0]]
        return rlt

    def push(self, key: int, count: int):
        target = self.links.get(key, None)
        if target is None:
            target = [key, count]
            self.links[key] = target
            heapq.heappush(self.vault, target)
            return
        target[1] += count

    def merge(self, other: Optional['HeapOfTupleWithReference']) -> 'HeapOfTupleWithReference':
        if other is None:
            return self
        small, big = (self, other) if len(self.vault) < len(other.vault) else (other, self)
        while len(small.vault) > 0:
            big.push(*small.pop())
        return big


class Solution:

    def numberOfGoodPaths(self, vals: list[int], edges: list[list[int]]) -> int:
        graph: list[Node] = [Node(idx=idx, val=el) for idx, el in enumerate(vals)]
        for nd_a, nd_b in edges:
            graph[nd_a].adjs.append(nd_b)
            graph[nd_b].adjs.append(nd_a)

        seen: set[int] = set()
        stack: list[int] = [0]
        cur_node = graph[0]
        rlt: int = 0

        while len(stack) > 0:
            prev_node, cur_node = cur_node, graph[stack.pop()]

            if cur_node.idx not in seen:  # forward walk
                seen.add(cur_node.idx)
                for el in cur_node.adjs:
                    if el not in seen:
                        stack.append(cur_node.idx)
                        stack.append(el)
                continue

            # backward walk
            prev_fast = HeapOfTupleWithReference() if prev_node.subtree is None else prev_node.subtree
            prev_fast.push(prev_node.val, 1)

            while len(prev_fast.vault) > 0 and prev_fast.top() < cur_node.val:
                _, count = prev_fast.pop()
                rlt += ((count - 1) * count) // 2

            cur_node.subtree = prev_fast.merge(cur_node.subtree)

        if cur_node.subtree is None:
            cur_node.subtree = HeapOfTupleWithReference()
        cur_node.subtree.push(cur_node.val, 1)
        while len(cur_node.subtree.vault) > 0:
            _, count = cur_node.subtree.pop()
            rlt += ((count - 1) * count) // 2

        return rlt + len(vals)


if __name__ == '__main__':
    tests = [
        ('test_00', ([1, 3, 2, 1, 3], [[0, 1], [0, 2], [2, 3], [2, 4]]), 6),
        ('test_01', ([1, 1, 2, 2, 3], [[0, 1], [1, 2], [2, 3], [2, 4]]), 7),
        ('test_02', ([1], []), 1),
        (
        'test_53', ([2, 4, 1, 2, 2, 5, 3, 4, 4], [[0, 1], [2, 1], [0, 3], [4, 1], [4, 5], [3, 6], [7, 5], [2, 8]]), 11),
        data_for_961.test_123,
    ]

    foo = Solution()
    method2test = Solution.numberOfGoodPaths

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)