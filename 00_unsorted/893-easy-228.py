# https://leetcode.com/problems/summary-ranges/description/
# timing 00:02:33
import time


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        rlt: list[str] = []

        if len(nums) == 0:
            return rlt

        low = top = nums[0]
        for el in nums[1:]:
            if el == top + 1:
                top = el
                continue
            rlt.append(str(low) if low == top else f'{str(low)}->{str(top)}')
            low = top = el

        rlt.append(str(low) if low == top else f'{str(low)}->{str(top)}')
        return rlt


if __name__ == '__main__':
    tests = [
        ('test_00', ([0, 1, 2, 4, 5, 7],), ["0->2", "4->5", "7"]),
    ]

    foo = Solution()
    method2test = Solution.summaryRanges

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
