# https://leetcode.com/problems/find-the-town-judge/description/
import time


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n == 1:  # trust list is empty so 1 is an answer
            return 1
        trusted_people: dict[int, set[int]] = dict()
        people_who_trust: set[int] = set()

        check_set = set(range(1, n+1))
        for somebody, trusted_human in trust:
            tmp = trusted_people.get(trusted_human, set())
            tmp.add(somebody)
            trusted_people[trusted_human] = tmp

            people_who_trust.add(somebody)

        for candidate, trusted_by in trusted_people.items():
            if trusted_by == (check_set - {candidate}) and candidate not in people_who_trust:
                return candidate
        return -1


if __name__ == '__main__':
    tests = [
        ('test_00', (2, [[1, 2]]), 2),
        ('test_01', (3, [[1, 3], [2, 3]]), 3),
        ('test_02', (3, [[1, 3], [2, 3], [3, 1]]), -1),
        ('test_03', (1, []), 1),
    ]

    foo = Solution()
    method2test = Solution.findJudge

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
