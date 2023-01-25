# https://leetcode.com/problems/daily-temperatures/description/
from typing import List, Optional, Any
from dataclasses import dataclass


@dataclass(slots=True)
class Node:
    idx: int
    temp: int
    nxt: Optional[Any] = None  # Optional[Node]


class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        rlt = [0] * len(temperatures)
        first_node = None
        for idx, val in enumerate(temperatures):
            new_node = Node(idx, val)

            if first_node is None:
                first_node = new_node
                continue

            cur_node = first_node
            while cur_node is not None and cur_node.temp < new_node.temp:
                rlt[cur_node.idx] = idx - cur_node.idx
                nxt_node = cur_node.nxt
                cur_node.nxt = None
                cur_node = nxt_node

            new_node.nxt = cur_node
            first_node = new_node
        return rlt


if __name__ == '__main__':
    foo = Solution()

    for name, inpt, outpt in [
        ('test_00', [73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ('test_01', [30, 40, 50, 60], [1, 1, 1, 0]),
        ('test_02', [30, 60, 90], [1, 1, 0]),
    ]:
        if name == 'test_0':
            print(foo.dailyTemperatures(inpt))
            quit()
        assert foo.dailyTemperatures(inpt) == outpt, print('👉', name)
