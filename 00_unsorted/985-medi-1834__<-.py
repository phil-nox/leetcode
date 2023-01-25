# https://leetcode.com/problems/single-threaded-cpu/description/
import time
from dataclasses import dataclass
import heapq


@dataclass(frozen=True, slots=True)
class Task:
    idx:            int
    enqueue_t:      int
    processing_t:   int

    def __lt__(self, other):
        return (self.processing_t, self.idx) < (other.processing_t, other.idx)


class Solution:

    def _fetch_task(self, queue: list[Task], task_at_work: list[Task], timeline: int):
        for _ in range(len(queue)):
            if queue[-1].enqueue_t <= timeline:
                heapq.heappush(task_at_work, queue.pop())
            else:
                break

    def _cold_start(self, queue: list[Task], task_at_work: list[Task]) -> int:
        timeline: int = queue[-1].enqueue_t
        self._fetch_task(queue, task_at_work, timeline)
        return timeline

    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        queue: list[Task] = [Task(idx, el[0], el[1]) for idx, el in enumerate(tasks)]
        queue.sort(key=lambda el: el.enqueue_t, reverse=True)

        rlt: list[int] = []
        task_at_work: list[Task] = []

        timeline: int = self._cold_start(queue, task_at_work)

        while len(task_at_work) > 0:
            task_todo = heapq.heappop(task_at_work)
            rlt.append(task_todo.idx)
            timeline += task_todo.processing_t               # close to _cold_start logic
            self._fetch_task(queue, task_at_work, timeline)

            if len(queue) > 0 and len(task_at_work) == 0:    # idle case
                timeline = self._cold_start(queue, task_at_work)

        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([[1, 2], [2, 4], [3, 2], [4, 1]],), [0, 2, 3, 1]),
        ('test_01', ([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]],), [4, 3, 2, 0, 1]),
        ('test_02',
         ([[19, 13], [16, 9], [21, 10], [32, 25], [37, 4], [49, 24], [2, 15],
           [38, 41], [37, 34], [33, 6], [45, 4], [18, 18], [46, 39], [12, 24]],),
         [6, 1, 2, 9, 4, 10, 0, 11, 5, 13, 3, 8, 12, 7]),
        ('test_03', ([[5, 2], [7, 2], [9, 4], [6, 3], [5, 10], [1, 1]],), [5, 0, 1, 3, 2, 4])
    ]

    foo = Solution()
    method2test = Solution.getOrder   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
