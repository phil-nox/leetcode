# https://leetcode.com/problems/minimize-deviation-in-array/description/
import time
import heapq
import tmp


class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:
        highs: list[int] = []
        low: int = nums[0] * 2                  # in case nums[0] is odd
        diff: int = 10**9

        for el in nums:                         # highs - an array of max possible values
            el = el if el % 2 == 0 else el * 2
            low = min(low, el)
            heapq.heappush(highs, -el)

        while highs[0] % 2 == 0:                # start reduce highest max one-by-one in heap_order
            cur = -heapq.heappop(highs)
            diff = min(diff, cur - low)         # refresh diff
            cur //= 2
            low = min(low, cur)                 # refresh min
            heapq.heappush(highs, -cur)

        diff = min(diff, -highs[0] - low)       # refresh diff with non-reducible maximum (can't be divided by 2)
        return diff


if __name__ == '__main__':
    tests = [
        ('test_00', ([1, 2, 3, 4],), 1),
        ('test_01', ([4, 1, 5, 20, 3],), 3),
        ('test_02', ([2, 10, 8],), 3),
        ('test_03', ([50, 67, 50],), 17),
        ('test_04', ([64, 67, 31],), 5),
        ('test_05', ([3, 5],), 1),
        ('test_06', ([10, 4, 3],), 2),  # 5, 4, 6
        ('test_07', (tmp.test_73,), tmp.rlt_73),    # Expected 99366288
    ]

    foo = Solution()
    method2test = Solution.minimumDeviation

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
