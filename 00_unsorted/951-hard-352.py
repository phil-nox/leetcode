# https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/
import time
from dataclasses import dataclass


@dataclass(slots=True)
class Interval:
    start: int
    end: int
    reg_idx: int

    def __lt__(self, other: 'Interval'):
        return self.start < other.start

    def __len__(self):
        return self.end - self.start

    def merge(self, other: 'Interval'):
        self.start = self.start if self.start < other.start else other.start
        self.end = self.end if self.end > other.end else other.end

    def update(self, value: int):
        if value < self.start:
            self.start = value
            return
        self.end = value


class SummaryRanges:

    def __init__(self):
        self.registry: dict[int, Interval] = dict()
        self.reg_top_idx: int = 0
        self.data: dict[int, Interval] = dict()

    def addNum(self, value: int) -> None:
        # case: already seen
        if value in self.data:
            return

        check_adjacent = ((value - 1) in self.data, (value + 1) in self.data)
        # case: create a new Interval (False, False)
        if True not in check_adjacent:
            tmp = Interval(start=value, end=value, reg_idx=self.reg_top_idx)
            self.registry[self.reg_top_idx] = tmp
            self.reg_top_idx += 1
            self.data[value] = tmp
            return

        # case: merge two Interval (True, True)
        if False not in check_adjacent:
            small, big, val_to_replace = self.data[value-1], self.data[value+1], value-1
            if len(small) > len(big):
                small, big, val_to_replace = big, small, value+1

            big.merge(small)

            self.data[value] = big
            step = 1 if val_to_replace > value else -1
            while self.data.get(val_to_replace, None) is small:
                self.data[val_to_replace] = big
                val_to_replace += step

            self.registry.pop(small.reg_idx)
            return

        # case: add value to existed Interval (True, False) or (False, True)
        tmp = self.data[value-1] if (value-1) in self.data else self.data[value+1]
        self.data[value] = tmp
        tmp.update(value)

    def getIntervals(self) -> list[list[int]]:
        return [[el.start, el.end] for el in sorted(self.registry.values())]


if __name__ == '__main__':
    time_diff = -time.perf_counter()

    foo = SummaryRanges()

    foo.addNum(6)
    print(foo.getIntervals(), [[6, 6]])
    assert foo.getIntervals() == [[6, 6]]

    foo.addNum(6)
    print(foo.getIntervals(), [[6, 6]])
    assert foo.getIntervals() == [[6, 6]]

    foo.addNum(0)
    print(foo.getIntervals(), [[0, 0], [6, 6]])
    assert foo.getIntervals() == [[0, 0], [6, 6]]

    foo.addNum(4)
    print(foo.getIntervals(), [[0, 0], [4, 4], [6, 6]])
    assert foo.getIntervals() == [[0, 0], [4, 4], [6, 6]]

    foo.addNum(8)
    print(foo.getIntervals(), [[0, 0], [4, 4], [6, 6], [8, 8]])
    assert foo.getIntervals() == [[0, 0], [4, 4], [6, 6], [8, 8]]

    foo.addNum(7)
    print(foo.getIntervals(), [[0, 0], [4, 4], [6, 8]])
    assert foo.getIntervals() == [[0, 0], [4, 4], [6, 8]]

    foo.addNum(6)
    print(foo.getIntervals(), [[0, 0], [4, 4], [6, 8]])
    assert foo.getIntervals() == [[0, 0], [4, 4], [6, 8]]

    foo.addNum(4)
    print(foo.getIntervals(), [[0, 0], [4, 4], [6, 8]])
    assert foo.getIntervals() == [[0, 0], [4, 4], [6, 8]]

    foo.addNum(7)
    print(foo.getIntervals(), [[0, 0], [4, 4], [6, 8]])
    assert foo.getIntervals() == [[0, 0], [4, 4], [6, 8]]

    foo.addNum(5)
    print(foo.getIntervals(), [[0, 0], [4, 8]])
    assert foo.getIntervals() == [[0, 0], [4, 8]]


    '''
    foo.addNum(1)
    print(foo.getIntervals(), [[1, 1]])
    assert foo.getIntervals() == [[1, 1]]

    foo.addNum(3)
    print(foo.getIntervals(), [[1, 1], [3, 3]])
    assert foo.getIntervals() == [[1, 1], [3, 3]]

    foo.addNum(7)
    print(foo.getIntervals(), [[1, 1], [3, 3], [7, 7]])
    assert foo.getIntervals() == [[1, 1], [3, 3], [7, 7]]

    foo.addNum(2)
    print(foo.getIntervals(), [[1, 3], [7, 7]])
    assert foo.getIntervals() == [[1, 3], [7, 7]]

    foo.addNum(6)
    print(foo.getIntervals(), [[1, 3], [6, 7]])
    assert foo.getIntervals() == [[1, 3], [6, 7]]

    foo.addNum(4)
    print(foo.getIntervals(), [[1, 4], [6, 7]])
    assert foo.getIntervals() == [[1, 4], [6, 7]]

    foo.addNum(9)
    print(foo.getIntervals(), [[1, 4], [6, 7], [9, 9]])
    assert foo.getIntervals() == [[1, 4], [6, 7], [9, 9]]

    foo.addNum(5)
    print(foo.getIntervals(), [[1, 7], [9, 9]])
    assert foo.getIntervals() == [[1, 7], [9, 9]]
    '''

    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
