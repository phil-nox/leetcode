# https://leetcode.com/problems/minimum-size-subarray-sum/description/
import time


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        rlt = limit_val = 10**6
        cur = nums[0]

        m_low, m_top, low, top = -1, -1, 0, 1

        while not (low == m_low and top == m_top):
            m_low, m_top = low, top

            while cur < target and top < len(nums):
                cur, top = cur + nums[top], top + 1

            while cur >= target and low < len(nums):
                rlt = min(rlt, top - low)
                cur, low = cur - nums[low], low + 1

        return rlt if rlt != limit_val else 0


if __name__ == '__main__':
    tests = [
        ('test_00', (7, [2, 3, 1, 2, 4, 3],), 2),
        ('test_01', (4, [1, 4, 4],), 1),
        ('test_02', (11, [1, 1, 1, 1, 1, 1, 1, 1],), 0),
        ('test_03', (11, [1, 2, 3, 4, 5],), 3),
    ]

    foo = Solution()
    method2test = Solution.minSubArrayLen
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
