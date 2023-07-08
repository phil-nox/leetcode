# https://leetcode.com/problems/put-marbles-in-bags/description/
import time


class Solution:
    def relocateMarbles(self, nums: list[int], moveFrom: list[int], moveTo: list[int]) -> list[int]:
        marble_s = set(nums)
        for fr, to in zip(moveFrom, moveTo):
            marble_s.remove(fr)
            marble_s.add(to)
        return sorted(marble_s)
        

if __name__ == '__main__':
    tests = [
        ('test_00', ([1, 6, 7, 8], [1, 7, 2], [2, 9, 5]), [5, 6, 8, 9]),
    ]

    foo = Solution()
    method2test = Solution.relocateMarbles
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
