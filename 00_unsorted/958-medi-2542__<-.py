# https://leetcode.com/problems/maximum-subsequence-score/description/
import time
import heapq


class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        mul_max: list[tuple[int, int]] = []
        for sum_val, mul_val in zip(nums1, nums2):
            heapq.heappush(mul_max, (-mul_val, -sum_val))

        check: list[int] = []
        cur_mul = 0
        for _ in range(k):
            cur_mul, val = heapq.heappop(mul_max)
            heapq.heappush(check, -val)

        sum_val = sum(check)
        rlt = -cur_mul * sum_val
        while len(mul_max) > 0:
            cur_mul, val = heapq.heappop(mul_max)
            sum_val -= heapq.heappop(check)
            sum_val -= val                  # val is negative_to_original in heap. so this is '+='
            heapq.heappush(check, -val)
            tmp = -cur_mul * sum_val
            rlt = rlt if rlt > tmp else tmp

        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([1, 3, 3, 2], [2, 1, 3, 4], 3), 12),
        ('test_01', ([4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1), 30),
        ('test_02', ([2, 1, 14, 12], [11, 7, 13, 6], 3), 168),
    ]

    foo = Solution()
    method2test = Solution.maxScore   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
