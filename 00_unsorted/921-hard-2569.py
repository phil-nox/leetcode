# https://leetcode.com/problems/handling-sum-queries-after-update/description/
import time
import data_for_922

from typing import Optional
from dataclasses import dataclass
from enum import Enum, auto

'''
import heapq

@classmethod
def debug(cls, root: 'SegNode'):
    wave: list['SegNode'] = [root]
    nxt_wave: list['SegNode'] = []
    prev: 'SegNode' = root
    line0, line1, line2 = [], [], []
    while wave:
        cur = heapq.heappop(wave)
        if cur.start - prev.start > 0:
            line0.append('             ' * (cur.start - prev.start - 1))
            line1.append('             ' * (cur.start - prev.start - 1))
            line2.append('             ' * (cur.start - prev.start - 1))
        line0.extend((' | ', f'[ {cur.start:02}-{cur.end:02} ] '))                          # 10
        line1.extend((' | ', f'on={cur.on:02}|{cur.count:02}=a'))                           # 10
        line2.extend((' | ', f'lazy=', '  +  ' if cur.lazy else '     '))                   # 10
        [heapq.heappush(nxt_wave, nd) for nd in (cur.right, cur.left) if nd]
        prev = cur
        if not wave:
            [print(''.join(el)) for el in (line0, line1, line2)]
            print()
            wave, nxt_wave = nxt_wave, wave
            line0, line1, line2 = [], [], []
            prev = wave[0] if wave else root
'''


class SegCompare(Enum):
    NOT = auto()
    PART = auto()
    FULL = auto()


@dataclass(slots=True)
class SegNode:
    start: int
    end: int
    on: int
    count: int
    lazy: bool = False
    left: Optional['SegNode'] = None
    right: Optional['SegNode'] = None

    def __hash__(self):
        return id(self)     # keep in mind https://stackoverflow.com/a/45476413

    def __lt__(self, other):
        return self.start < other.start

    @classmethod
    def create_tree(cls, array: list[int]) -> 'SegNode':
        wave: list['SegNode'] = [SegNode(start=idx, end=idx, on=el, count=1) for idx, el in enumerate(array)]
        nxt_wave: list['SegNode'] = []

        while len(wave) > 1:
            idx = 0
            while idx < len(wave):
                if idx + 1 < len(wave):
                    left, right = wave[idx], wave[idx+1]
                    tmp = SegNode(start=left.start, end=right.end, on=left.on+right.on, count=left.count+right.count)
                    tmp.left, tmp.right = left, right
                    idx += 2
                else:
                    tmp = wave[idx]
                    idx += 1
                nxt_wave.append(tmp)
            wave, nxt_wave = nxt_wave, []
        return wave[0]  # root

    def _compare(self, beg: int, end: int) -> SegCompare:
        if end < self.start or self.end < beg:
            return SegCompare.NOT
        if beg <= self.start and self.end <= end:
            return SegCompare.FULL
        return SegCompare.PART

    def _flip(self) -> int:
        self.on = self.count - self.on
        self.lazy = not self.lazy
        return self.on

    def _push_lazy(self):
        self.lazy = not self.lazy
        [el._flip() for el in (self.left, self.right) if el]

    def update(self, beg: int, end: int) -> None:         # apply to root
        state: SegCompare = self._compare(beg, end)
        if state == SegCompare.NOT:
            return
        if state == SegCompare.FULL:
            self._flip()
            return
        if self.lazy:
            self._push_lazy()

        stack: list['SegNode'] = [self]
        seen: set['SegNode'] = set()
        cur, prev = self, self

        while stack:
            prev, cur = cur, stack.pop()
            if cur in seen:
                cur.on += prev.on
                continue
            seen.add(cur)
            for el in (cur.left, cur.right):
                state = el._compare(beg, end)
                if state == SegCompare.NOT:
                    continue
                if state == SegCompare.FULL:
                    cur.on += -el.on + el._flip()
                    continue
                if el.lazy:
                    el._push_lazy()
                cur.on -= el.on
                stack.extend((cur, el))

    def total(self) -> int:     # apply to root
        return self.on


class Solution:
    def handleQuery(self, nums1: list[int], nums2: list[int], queries: list[list[int]]) -> list[int]:
        cur: int = sum(nums2)
        tree: SegNode = SegNode.create_tree(nums1)
        rlt: list[int] = []

        for com, val_a, val_b in queries:
            if com == 1:
                tree.update(val_a, val_b)
            elif com == 2:
                cur += tree.total() * val_a
            else:
                rlt.append(cur)
        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([1, 0, 1], [0, 0, 0], [[1, 1, 1], [2, 1, 0], [3, 0, 0]]), [3]),
        ('test_01', ([1], [5], [[2, 0, 0], [3, 0, 0]]), [5]),
        ('test_72', data_for_922.test_72, data_for_922.outpt_72),
    ]

    '''
    tree = SegNode.create_tree([0, 1, 0, 0, 1, 1, 1, 1, ])
    print('total=', tree.total())
    SegNode.debug(tree)

    SegNode.update(tree, (2, 3))
    print('total=', tree.total())
    SegNode.debug(tree)

    SegNode.update(tree, (2, 2))
    print('total=', tree.total())
    SegNode.debug(tree)
    
    quit()
    '''

    foo = Solution()
    method2test = Solution.handleQuery

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
