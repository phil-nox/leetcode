# https://leetcode.com/problems/asteroid-collision/description/
import time


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        right = []
        rlt = []

        for el in asteroids:
            if el < 0 and not right:
                rlt.append(el)
                continue
            if el > 0:
                right.append(el)
                continue

            while right:
                if right[-1] > -el:
                    el = 0
                    break
                if right[-1] == -el:
                    right.pop()
                    el = 0
                    break
                right.pop()

            if el:
                rlt.append(el)

        return [*rlt, *right]
        

if __name__ == '__main__':
    tests = [
        ('test_00', ([5, 10, -5],), [5, 10]),
    ]

    foo = Solution()
    method2test = Solution.asteroidCollision
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
