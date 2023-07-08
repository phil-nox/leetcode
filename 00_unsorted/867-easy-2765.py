# https://leetcode.com/problems/put-marbles-in-bags/description/
import time


class Solution:
    def alternatingSubarray(self, nums: list[int]) -> int:
        rlt = -1
        tmp, cur, nxt = 1, nums[0] + 1, nums[0]

        for idx in range(1, len(nums)):
            if nums[idx] == cur:
                tmp, cur, nxt = tmp + 1, nxt, cur
                continue
            rlt = max(tmp, rlt)
            tmp, cur, nxt = (1, nums[idx] + 1, nums[idx])
            if nums[idx] - 1 == nums[idx - 1]:
                tmp, cur, nxt = (2, nums[idx - 1], nums[idx])
        rlt = max(tmp, rlt)

        return rlt if rlt > 1 else -1
        

if __name__ == '__main__':
    tests = [
        ('test_00', ([2, 3, 4, 3, 4],), 4),
        ('test_01', ([21, 9, 5],), -1),
    ]

    foo = Solution()
    method2test = Solution.alternatingSubarray
    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
