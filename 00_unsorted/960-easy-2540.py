# https://leetcode.com/problems/minimum-common-value/description/
import time


class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        it_1, it_2 = iter(nums1), iter(nums2)
        candidate, search, other = (nums1[0], it_2, it_1) if nums1[0] > nums2[0] else (nums2[0], it_1, it_2)
        while (check := next(search, None)) is not None:
            if check == candidate:
                return candidate
            if check < candidate:
                continue
            candidate, search, other = check, other, search
        return -1


if __name__ == '__main__':
    tests = [
        ('test_00', ([0, 1], 20), 2),               # test_case_from_leetcode
    ]

    foo = Solution()
    method2test = Solution.getCommon   # the_method_from_leetcode

    time_diff = -time.perf_counter()
    for name, inpt, outpt in tests:
        test_rlt = method2test(foo, *inpt)
        assert test_rlt == outpt, print(f'Problem ⚠️ {name} - {test_rlt} vs {outpt}')
    time_diff += time.perf_counter()
    print('⏱ ️', time_diff)
