# https://leetcode.com/problems/reward-top-k-students/description/
# https://leetcode.com/contest/biweekly-contest-94/problems/reward-top-k-students/
import time
from typing import List
import heapq


class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        vault = list()
        feed_pos, feed_neg = set(positive_feedback), set(negative_feedback)
        for rep, idx in zip(report, student_id):
            score = 0
            for word in rep.split():
                if word in feed_pos:
                    score -= 3
                elif word in feed_neg:
                    score += 1
            heapq.heappush(vault, (score, idx))

        rlt = list()
        for _ in range(k):
            rlt.append(heapq.heappop(vault)[1])
        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00',
         (["smart","brilliant","studious"], ["not"], ["this student is studious","the student is smart"], [1,2], 2),
         [1, 2]),
        ('test_01',
         (["smart", "brilliant", "studious"], ["not"], ["this student is not studious","the student is smart"], [1, 2], 2),
         [2, 1]),
    ]

    foo = Solution()
    method2test = Solution.topStudents   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)

